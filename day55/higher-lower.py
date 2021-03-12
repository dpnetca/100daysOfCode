import random
from flask import Flask


app = Flask(__name__)

NUM = random.randint(0, 9)


@app.route("/")
def index():
    return (
        "<h1>Guess a number between 0 and 9</h1>"
        "<img src='https://media.giphy.com/media/UDU4oUJIHDJgQ/giphy.gif'>"
        f"<p>hint: {NUM}</p>"
    )


@app.route("/<int:number>")
def guess(number):
    if number == NUM:
        html = (
            "<h1 style='color: green'>You Found Me</h1>"
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
        )
    elif number > NUM:
        html = (
            "<h1 style='color: purple'>Too high, try again!</h1>"
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm"
            "/giphy.gif'>"
        )
    elif number < NUM:
        html = (
            "<h1 style='color: red'>Too low, try again!</h1>"
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
        )
    else:
        html = "Well this is embarassing...something went wrong"
    return html


if __name__ == "__main__":
    app.run(debug=True)
