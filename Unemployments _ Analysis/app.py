from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

# Read Dataset
data = pd.read_csv("Unemployment in India.csv")

# Remove empty state names
data = data.dropna(subset=["Region"])

# Get all states
states = sorted(data["Region"].unique())


@app.route("/")
def home():
    return render_template(
        "index.html",
        states=states
    )


@app.route("/analyze", methods=["POST"])
def analyze():

    state = request.form["state"]

    state_data = data[data["Region"] == state]

    avg_rate = round(
        state_data[" Estimated Unemployment Rate (%)"].mean(),
        2
    )

    max_rate = round(
        state_data[" Estimated Unemployment Rate (%)"].max(),
        2
    )

    min_rate = round(
        state_data[" Estimated Unemployment Rate (%)"].min(),
        2
    )

    employed = int(
        state_data[" Estimated Employed"].mean()
    )

    # Create Graph
    plt.figure(figsize=(10, 5))

    plt.plot(
        range(len(state_data)),
        state_data[" Estimated Unemployment Rate (%)"],
        marker="o",
        linewidth=3
    )

    plt.grid(True)

    plt.xlabel("Months")
    plt.ylabel("Unemployment Rate (%)")
    plt.title(f"{state} Unemployment Trend")

    plt.tight_layout()

    plt.savefig("static/graph.png")

    plt.close()

    return render_template(
        "results.html",
        state=state,
        avg_rate=avg_rate,
        max_rate=max_rate,
        min_rate=min_rate,
        employed=employed
    )


if __name__ == "__main__":
    app.run(debug=False)