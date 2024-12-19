# -*- coding: utf-8 -*-
"""machine_learning_youtube.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13Nvzbb3kT4IbveU9GOQC4-Gdb0zKAqbj
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/union_all.csv')
df.head()

df.info()

X = df[["likes", "comment_count"]]
y = df["view_count"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

from sklearn.linear_model import LinearRegression

model = LinearRegression().fit(X_train_scaled, y_train)

from sklearn.metrics import mean_squared_error, mean_absolute_error

r2 = model.score(X_train_scaled, y_train)
from sklearn.metrics import mean_squared_error, mean_absolute_error

r2 = model.score(X_train_scaled, y_train)
train_pred_model = model.predict(X_train_scaled)

mse = mean_squared_error(y_true=y_train, y_pred=train_pred_model)
mae = mean_absolute_error(y_true=y_train, y_pred=train_pred_model)

print(f"{r2=}")
print(f"{mse=}")
print(f"{mae=}")

import numpy as np

new = np.array([[7757, 141]])

new_scaled = scaler.transform(new)

prediction_views = model.predict(new_scaled)

prediction_views

#Calcul des gains estimés (the average made from ads is $1 per 1000 views)
pred_earning = prediction_views / 1000
pred_earning

f'{pred_earning[0]:.2f}$'

# C'est important que l'utilisateur mette les deux valeurs séparées par un vergule

data = input("Please give number of likes and number of comments")

input_numeric = [float(i) for i in data.split(",")]

new = np.array([input_numeric])

new_scaled = scaler.transform(new)

prediction = model.predict(new_scaled)

prediction

model.predict([[-1.63768542e-01, -2.07492331e-01]])

pred_model = model.predict(X_test_scaled)

r2 = model.score(X_test_scaled, y_test)
mse = mean_squared_error(y_true=y_test, y_pred=pred_model)
mae = mean_absolute_error(y_true=y_test, y_pred=pred_model)

print(f"{r2=}")
print(f"{mse=}")
print(f"{mae=}")

model_2 = LinearRegression()
model_2.fit(X_train_scaled, y_train)

test_pred_model_2 = model_2.predict(X_test_scaled)
r2 = model_2.score(X_test_scaled, y_test)
mse = mean_squared_error(y_true=y_test, y_pred=test_pred_model_2)
mae = mean_absolute_error(y_true=y_test, y_pred=test_pred_model_2)

print(f"{r2=}")
print(f"{mse=}")
print(f"{mae=}")

model_2.coef_

import plotly.express as px
fig = px.bar(x=X.columns, y=model_2.coef_)
fig.show()

import plotly.express as px
fig = px.scatter(df, "likes", "comment_count")
fig.show()

df

