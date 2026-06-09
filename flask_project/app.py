from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/about")
def about():
    return "I am Michael, a CS student at KNUST!"

@app.route("/contact")
def contact():
    return "Contact me at michael@email.com"

@app.route("/user/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return f"{a} + {b} = {a + b}"



@app.route("/profile/<name>")
def profile(name):
    return render_template("profile.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)