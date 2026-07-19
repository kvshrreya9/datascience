import pandas as pd
import pickle

from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv("car data.csv")

data = data.drop("Car_Name", axis=1)

data = pd.get_dummies(data)

X = data.drop("Selling_Price", axis=1)

y = data["Selling_Price"]

model = RandomForestRegressor()

model.fit(X, y)

pickle.dump(
    model,
    open("car_model.pkl", "wb")
)

print("Model Saved")