from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# db.create_all()
# db.session.add(Books(title="Harry Potter", author="J.K. Rowling", rating=9.3))
# db.session.commit()


# import sqlite3
# db = sqlite3.connect("day63/books-collection.db")
# cursor = db.cursor()
# cursor.execute(
#     """CREATE TABLE books
#     (id INTEGER PRIMARY KEY,
#     title varchar(250) NOT NULL UNIQUE,
#     author varchar(250) NOT NULL,
#     rating FLOAT NOT NULL)"""
# )
# all_books = []


@app.route("/")
def home():
    all_books = db.session.query(Books).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # all_books.append(
        #     {
        #         "title": request.form["title"],
        #         "author": request.form["author"],
        #         "rating": request.form["rating"],
        #     }
        # )
        db.session.add(
            Books(
                title=request.form["title"],
                author=request.form["author"],
                rating=request.form["rating"],
            )
        )
        db.session.commit()

        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    book = Books.query.get(book_id)
    if request.method == "POST":
        book.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", book=book)


@app.route("/delete/<int:book_id>")
def delete(book_id):
    book = Books.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
