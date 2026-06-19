# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/form")
def form():
    return render_template("forms.html")

@app.route("/greet", methods=["POST"])
def greet():
    name = request.form["username"]
    return render_template("greeting.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)