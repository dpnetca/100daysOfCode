import requests
from flask import Flask, render_template
from post import Post

response = requests.get("https://api.npoint.io/5abcca6f4e39b4955965")
posts = [
    Post(post["id"], post["title"], post["subtitle"], post["body"])
    for post in response.json()
]

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=posts)


@app.route("/<int:num>")
def blog_post(num):
    post = None
    for p in posts:
        if p.id == num:
            post = p
            break
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
