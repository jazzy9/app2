from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


#--this is form for users to register & create their password and username --#
class RegistrationForm(FlaskForm):
#making sure the user name is between 2-20 characters
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max = 20)])
#making sure users input email in the right format
    email = StringField('Email',validators =[DataRequired(),Email()])
#making sure users choose password when registering
    password = PasswordField('Password', validators= [DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators = [DataRequired(), EqualTo('password')])
#submit button for so that users can send their info
    submit = SubmitField('Sign Up')

#-- this is login form allowing people to login with just their email --#
class LoginForm(FlaskForm):
#making sure users input email in the right format
    email = StringField('Email',validators =[DataRequired(),Email()])
#making sure users choose password when registering
    password = PasswordField('Password', validators= [DataRequired()])
#adding a remember field to allow users to stay logged in for a while, and storing a cookie --
    remember = BooleanField('Remember Me')
#submit button for so that users can send their info
    submit = SubmitField('Login')
