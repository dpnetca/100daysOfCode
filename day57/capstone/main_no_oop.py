import requests
from flask import Flask, render_template


app = Flask(__name__)

DATA_API = "https://api.npoint.io/5abcca6f4e39b4955965"


@app.route("/")
def home():
    response = requests.get(DATA_API)
    posts = response.json()
    return render_template("index.html", posts=posts)


@app.route("/<int:num>")
def blog_post(num):
    response = requests.get(DATA_API)
    posts = response.json()
    post = None
    for p in posts:
        if p["id"] == num:
            post = p
            break
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
