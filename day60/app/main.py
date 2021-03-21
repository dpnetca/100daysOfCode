import os
import smtplib
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


POSTS = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()


def send_email(
    message,
    sender=os.getenv("EMAIL_ADDRESS"),
    email_username=os.getenv("EMAIL_ADDRESS"),
    email_password=os.getenv("EMAIL_PASSWORD"),
    recipient=os.getenv("EMAIL_ADDRESS"),
    subject="Contact Form Submission",
):

    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = os.getenv("SMTP_PORT", "25")
    with smtplib.SMTP(host=smtp_host, port=smtp_port) as smtp:
        smtp.login(user=email_username, password=email_password)
        smtp.sendmail(
            from_addr=sender,
            to_addrs=recipient,
            msg=(
                f"From:{sender}\n"
                f"To:{recipient}\n"
                f"Subject:{subject}\n\n"
                f"{message}"
            ),
        )


@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html", posts=POSTS)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html", methods=["GET", "POST"])
def contact():
    contact_header = "Contact Me"
    if request.method == "POST":
        contact_header = "Successfully sent your message"
        message = (
            "You have recieved a new message:\n\n"
            f"From: {request.form['name']} <{request.form['email']}>\n"
            f"Tel: {request.form['tel']}\n"
            f"Message: \n{request.form['message']}"
        )
        send_email(
            message=message,
            sender=request.form["email"],
        )

    return render_template("contact.html", contact_header=contact_header)


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
