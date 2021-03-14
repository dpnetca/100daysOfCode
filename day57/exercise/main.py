import random
import requests

from datetime import datetime
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    random_number = random.randint(1, 10)
    year = datetime.now().year
    return render_template("index.html", num=random_number, year=year)


@app.route("/guess/<name>")
def guess(name):
    response = requests.get(f"https://api.agify.io/?name={name}")
    age = response.json()["age"]

    response = requests.get(f"https://api.genderize.io/?name={name}")
    gender = response.json()["gender"]
    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route("/blog/<int:post_num>")
def get_blog(post_num):
    response = requests.get("https://api.npoint.io/5abcca6f4e39b4955965")
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts, post_num=post_num)


if __name__ == "__main__":
    app.run(debug=True)
