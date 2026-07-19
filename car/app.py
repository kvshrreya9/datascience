from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained model
model = pickle.load(open("car_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    present_price = float(request.form["present_price"])
    kms = int(request.form["kms"])
    owner = int(request.form["owner"])
    year = int(request.form["year"])

    fuel = request.form["fuel"]
    seller = request.form["seller"]
    transmission = request.form["transmission"]

    input_data = pd.DataFrame([{
        "Year": year,
        "Present_Price": present_price,
        "Driven_kms": kms,
        "Owner": owner,

        "Fuel_Type_CNG": 1 if fuel == "CNG" else 0,
        "Fuel_Type_Diesel": 1 if fuel == "Diesel" else 0,
        "Fuel_Type_Petrol": 1 if fuel == "Petrol" else 0,

        "Selling_type_Dealer": 1 if seller == "Dealer" else 0,
        "Selling_type_Individual": 1 if seller == "Individual" else 0,

        "Transmission_Automatic": 1 if transmission == "Automatic" else 0,
        "Transmission_Manual": 1 if transmission == "Manual" else 0
    }])

    try:
        prediction = model.predict(input_data)

        price = round(float(prediction[0]), 2)

        if price > 8:
            recommendation = "High Resale Value"
        elif price > 4:
            recommendation = "Moderate Resale Value"
        else:
            recommendation = "Low Resale Value"

        return render_template(
            "results.html",
            price=price,
            present_price=present_price,
            fuel=fuel,
            transmission=transmission,
            owner=owner,
            year=year,
            recommendation=recommendation
        )

    except Exception as e:
        return f"<h2>Error:</h2><p>{e}</p>"


if __name__ == "__main__":
    app.run(debug=True)