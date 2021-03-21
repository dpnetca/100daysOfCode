from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    return f"<h1>Name: {username}, Password: {password}"


if __name__ == "__main__":
    app.run(debug=True)
