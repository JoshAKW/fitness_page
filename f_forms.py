from flask import Blueprint
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired,  Email, EqualTo, Length
from wtforms.widgets import TextArea
from flask_ckeditor import CKEditorField


webforms = Blueprint('webforms', __name__)


# create a Form Class

# Create a search form
class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField("Submit")

# post form


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    # content = StringField("Content", validators=[
    #                       DataRequired()], widget=TextArea())
    content = CKEditorField("Content", validators=[
        DataRequired()])
    author = StringField("Author")
    slug = StringField("Slug", validators=[DataRequired()])
    submit = SubmitField("Submit")


class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[Email(), DataRequired()])
    favorite_color = StringField("Favorite Color")
    password_hash = PasswordField('Password', validators=[DataRequired(), EqualTo(
        'password_hash2', message='Passwords must match!')])
    password_hash2 = PasswordField(
        'Confirm Password', validators=[DataRequired()])
    submit = SubmitField("Submit")


class AnatomyForm(FlaskForm):
    name = StringField("What Anatomy are you interested in?",
                       validators=[DataRequired()])
    submit = SubmitField("Submit")


class PasswordForm(FlaskForm):
    email = StringField("What's Your email?", validators=[DataRequired()])
    password_hash = StringField(
        "What's Your password?", validators=[DataRequired()])
    submit = SubmitField("Submit")


# Create Login Form
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

# Create a workout form


class WorkoutForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    exercise1 = StringField("Exercise", validators=[DataRequired()])
    exercise2 = StringField("Exercise")
    exercise3 = StringField("Exercise")
    exercise4 = StringField("Exercise")
    exercise5 = StringField("Exercise")
    exercise6 = StringField("Exercise")
    exercise7 = StringField("Exercise")
    exercise8 = StringField("Exercise")
    exercise9 = StringField("Exercise")
    exercise10 = StringField("Exercise")
    exercise11 = StringField("Exercise")
    exercise12 = StringField("Exercise")
    submit = SubmitField("Submit")
