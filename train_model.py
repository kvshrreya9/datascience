import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("iris.csv")


X = data.drop(["Id", "Species"], axis=1)
y = data["Species"]

model = RandomForestClassifier()

model.fit(X, y)

pickle.dump(model, open("iris_model.pkl", "wb"))
print("Features used:")
print(X.columns)
print("Shape:", X.shape)

print("Model Saved Successfully")