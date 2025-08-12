import pandas as pd
import flask
from sklearn.linear_model import LinearRegression   # pip install scikit-learn
from sklearn.metrics import mean_squared_error

df = pd.read_csv(r"DBS_SingDollar.csv")
sgd_col_y = df["SGD"]
dbs_col_x = df.loc[:, ["DBS"]]

model = LinearRegression()
model.fit(dbs_col_x, sgd_col_y)
coefficient = model.coef_
intercept = model.intercept_

rmse = mean_squared_error(sgd_col_y, model.predict(dbs_col_x)) ** 0.5
print(rmse)


