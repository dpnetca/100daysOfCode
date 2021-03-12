from flask import Flask


def make_bold(f):
    def wrapper():
        return f"<b> {f()} </b>"

    return wrapper


def make_emphasis(f):
    def wrapper():
        return f"<em> {f()} </em>"

    return wrapper


def make_underline(f):
    def wrapper():
        return f"<u> {f()} </u>"

    return wrapper


app = Flask(__name__)


@app.route("/")
def index():
    return (
        "<h1 style='text-align: center'>Hello World</h1>"
        "<p>this is a paragraph</p>"
        "<img src='https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif'"
        " width=200>"
    )


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!"


@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}"


@app.route("/username/<name>/<int:age>")
def greet_age(name, age):
    return f"Hello {name}, you are {age} years old"


if __name__ == "__main__":
    app.run(debug=True)
