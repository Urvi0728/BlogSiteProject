from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo, ValidationError
from blog.models import User, Post

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=3, max=40)])

    email = StringField('E-mail', validators=[DataRequired(), Email()])

    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()

        if user:
            raise ValidationError("Username already taken")

    def validate_email(self, email):
        user = User.query.filter_by(username = email.data).first()

        if user:
            raise ValidationError("Email already taken")


class LoginForm(FlaskForm):

    email = StringField('E-mail',validators=[DataRequired(), Email()])

    password = PasswordField('Password',validators=[DataRequired()])

    remember = BooleanField('Remember me')

    submit = SubmitField("Login")


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content' , validators=[DataRequired()])
    submit = SubmitField('Post')
