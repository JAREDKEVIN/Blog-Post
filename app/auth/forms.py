from flask_wtf import FlaskForm
from sqlalchemy.orm import query
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import  Required, Email, EqualTo
from wtforms.validators import ValidationError
from ..models import User
from wtforms.fields.html5 import EmailField

class RegistrationForm(FlaskForm):
    username=StringField('Input your preferred username', validators=[Required()])
    email=EmailField('Your email address', validators=[Required(), Email()])
    password=PasswordField('Create your password', validators=[Required(), EqualTo('password_confirm', message='passwords must match')])
    password_confirm=PasswordField('confirm the password you\'ve created', validators=[Required()])
    submit=SubmitField('Sign up')

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('There is already an account with that email. Please use another email.')
    
    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('The username you have used has already been taken. use another one.')

class LoginForm(FlaskForm):
    email=EmailField('You email address', validators=[Required(), Email()])
    password=PasswordField('Input your password', validators=[Required()])
    remember=BooleanField('Want your password remembered?')
    submit=SubmitField('sign In')