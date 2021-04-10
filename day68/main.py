import os
from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    flash,
    send_from_directory,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
# db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/")
def home():
    return render_template(
        "index.html", logged_in=current_user.is_authenticated
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if User.query.filter_by(email=request.form.get("email")).first():
            flash("email already exists")
            return redirect(url_for("login"))
        else:
            hashed_pass = generate_password_hash(
                request.form.get("password"),
                method="pbkdf2:sha256",
                salt_length=8,
            )
            new_user = User(
                email=request.form.get("email"),
                password=hashed_pass,
                name=request.form.get("name"),
            )
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("secrets"))
    return render_template(
        "register.html", logged_in=current_user.is_authenticated
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form.get("email")).first()
        if not user:
            flash("User or Password incorect")
        elif check_password_hash(user.password, request.form.get("password")):
            login_user(user)
            return redirect(url_for("secrets"))
        else:
            flash("User or Password incorect")
    return render_template(
        "login.html", logged_in=current_user.is_authenticated
    )


@app.route("/secrets")
@login_required
def secrets():
    return render_template(
        "secrets.html",
        logged_in=current_user.is_authenticated,
        name=current_user.name,
    )


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/download")
@login_required
def download():
    return send_from_directory("static", filename="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)