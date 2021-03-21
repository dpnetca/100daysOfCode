from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField(label="email", validators=[DataRequired(), Email()])
    password = PasswordField(
        label="password", validators=[DataRequired(), Length(min=8)]
    )
    submit = SubmitField(label="Log In")
