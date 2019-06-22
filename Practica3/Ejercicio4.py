import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, cross_val_score
import statistics

import numpy as np

csv_data = pd.read_csv('Auto.csv', sep=',', usecols=['horsepower', 'mpg'])
x = pd.to_numeric(csv_data['horsepower'], errors='coerce')
y = np.array(csv_data['mpg'][x.notnull()])
x = np.array(x[x.notnull()])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=30)

mejor_modelo = 0
mejor_varianza = 1
mejor_score = 0

x_train_reshape = x_train.reshape(-1, 1)
x_test_reshape = x_test.reshape(-1, 1)

for i in range(1, 6):
    model = Pipeline([('poly', PolynomialFeatures(degree=i)), ('linear', LinearRegression(fit_intercept=False))])
    scores = cross_val_score(model, x_train_reshape, y_train, cv=5)
    varianza = statistics.variance(scores)
    score_medio = sum(scores) / len(scores)
    print('Polinoio grado:', i, ' Score:', score_medio, ' Varianza: ', varianza)
    if varianza < 0.01 and score_medio > mejor_score:
        mejor_modelo = i
        mejor_varianza = varianza
        mejor_score = score_medio

if mejor_modelo == 0:
    raise Exception('Ningun modelo es confiable')

model = Pipeline([('poly', PolynomialFeatures(degree=mejor_modelo)), ('linear', LinearRegression(fit_intercept=False))])

model.fit(x_train_reshape, y_train)
score = model.score(x_test_reshape, y_test)
print('Polinomio con mejor ajuste: ', mejor_modelo, '\nScore medio en CV: ', mejor_score, '\nScore en test: ', score)

if abs(mejor_score - score) > 0.1:
    print('El modelo no es confiable')
else:
    print('El modelo es confiable')

f1 = plt.figure(1)
f1.canvas.set_window_title('Autos')
plt.xlabel('horsepower')
plt.ylabel('gml')
plt.scatter(x_test, y_test)
x_test_ordered = np.sort(x_test)
plt.plot(x_test_ordered, model.predict(x_test_ordered.reshape(-1, 1)), color='red')
plt.show()
