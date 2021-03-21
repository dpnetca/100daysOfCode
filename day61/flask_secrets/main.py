from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from login_form import LoginForm

app = Flask(__name__)
Bootstrap(app)

app.secret_key = "thisshouldnotbehere"
admin_user = "admin@email.com"
admin_password = "12345678"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if (
            form.email.data == admin_user
            and form.password.data == admin_password
        ):
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
