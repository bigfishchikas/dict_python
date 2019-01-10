from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class Postform(FlaskForm):
    username = StringField('Username',         
            validators = [DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password',         
            validators = [DataRequired()])
    submit = SubmitField('Sign in ')