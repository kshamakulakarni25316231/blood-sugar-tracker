from flask import Flask, render_template, request, redirect
import pandas as pd
import os

app = Flask(__name__)

FILE = "data.csv"

columns = [
    "date",
    "before_breakfast",
    "after_breakfast",
    "before_lunch",
    "after_lunch",
    "before_dinner",
    "after_dinner"
]

# Create CSV if it doesn't exist
if not os.path.exists(FILE):
    pd.DataFrame(columns=columns).to_csv(FILE, index=False)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        data = {
            "date": request.form["date"],
            "before_breakfast": request.form["before_breakfast"],
            "after_breakfast": request.form["after_breakfast"],
            "before_lunch": request.form["before_lunch"],
            "after_lunch": request.form["after_lunch"],
            "before_dinner": request.form["before_dinner"],
            "after_dinner": request.form["after_dinner"]
        }

        pd.DataFrame([data]).to_csv(FILE, mode="a", header=False, index=False)

        return redirect("/")

    df = pd.read_csv(FILE).fillna("")

    return render_template("index.html", tables=df.values.tolist())


@app.route("/clear", methods=["POST"])
def clear_records():

    pd.DataFrame(columns=columns).to_csv(FILE, index=False)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)