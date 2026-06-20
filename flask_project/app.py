# app.py
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)


@app.route("/form")
def form():
    return render_template("forms.html")

@app.route("/greet", methods=["POST"])
def greet():
    name = request.form["username"]
    phone = str(request.form["phone"])
    new_contact = Contact(name=name, phone=phone)
    db.session.add(new_contact)
    db.session.commit()
    return render_template("greeting.html", name=name, phone=phone)
   


if __name__ == "__main__":
    app.run(debug=True)


