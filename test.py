import pandas as pd

data = pd.read_csv("car data.csv")

print(data["Fuel_Type"].unique())

print(data["Selling_type"].unique())

print(data["Transmission"].unique())