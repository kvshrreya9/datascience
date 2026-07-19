from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open("iris_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        sepal_length = float(request.form["sl"])
        sepal_width = float(request.form["sw"])
        petal_length = float(request.form["pl"])
        petal_width = float(request.form["pw"])

        prediction = model.predict([[
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]])

        flower = prediction[0]

        # Change these names if your dataset uses different labels
        if "setosa" in flower.lower():
            image = "setosa.webp"

        elif "versicolor" in flower.lower():
            image = "versicolor.webp"

        elif "virginica" in flower.lower():
            image = "virginica.webp"

        else:
            image = "iris.webp"

        return render_template(
            "results.html",
            result=flower,
            image=image
        )

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    app.run(debug=True)