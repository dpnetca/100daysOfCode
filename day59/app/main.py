import requests
from flask import Flask, render_template

app = Flask(__name__)


POSTS = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()


@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html", posts=POSTS)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:post_id>")
def post(post_id):
    # if post_id > 0 and post_id <= len(POSTS):
    #     post = POSTS[post_id - 1]
    # else:
    #     post = ""

    post = None
    for p in POSTS:
        if p["id"] == post_id:
            post = p
            break

    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
