import os

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import NumberRange, Optional, DataRequired
import requests

from dotenv import load_dotenv

load_dotenv()

TMDB_API_BASE_URL = "https://api.themoviedb.org/3"
TMDB_IMG_URL = "https://www.themoviedb.org/t/p/w300_and_h450_bestv2"

app = Flask(__name__)

# app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Bootstrap(app)
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.Text, nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


class UpdateForm(FlaskForm):
    rating = DecimalField(
        label="Your Rating out of 10, eg. 7.5",
        validators=[Optional(), NumberRange(min=0, max=10)],
    )
    review = StringField("Your Review")
    submit = SubmitField("Submit")


class AddMovieForm(FlaskForm):
    movie_title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField("Submit")


def imdb_get(endpoint, params={}):
    url = TMDB_API_BASE_URL + endpoint
    if "api_key" not in params:
        params["api_key"] = os.getenv("TMDB_API_KEY")
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def get_imdb_movies_by_title(title):
    movie_list = []
    endpoint = "/search/movie"
    params = {"query": title}
    response = imdb_get(endpoint, params)
    movie_list.extend(response["results"])
    return movie_list


def get_imdb_movie_by_id(movie_id):
    endpoint = f"/movie/{movie_id}"
    response = imdb_get(endpoint)
    return response


@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating).all()
    for i, movie in enumerate(movies):
        movie.ranking = len(movies) - i
    db.session.commit()
    return render_template("index.html", movies=movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = UpdateForm()
    movie_id = request.args.get("movie_id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        if form.rating.data:
            movie.rating = form.rating.data
        if form.review.data:
            movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("movie_id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        movies = get_imdb_movies_by_title(form.movie_title.data)
        return render_template("select.html", movies=movies)
    return render_template("add.html", form=form)


@app.route("/add_movie/<int:movie_id>")
def add_movie(movie_id):
    imdb_movie = get_imdb_movie_by_id(movie_id)
    new_movie = Movie(
        title=imdb_movie["original_title"],
        year=imdb_movie["release_date"][:4],
        description=imdb_movie["overview"],
        img_url=(f"{TMDB_IMG_URL}/{imdb_movie['poster_path']}"),
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit", movie_id=new_movie.id))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
