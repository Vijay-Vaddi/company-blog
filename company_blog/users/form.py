from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
# is going to allow user update/upload png/jpeg file  

from company_blog.models import User
from flask_login import current_user

class LoginForm(FlaskForm):
    
    login_id = EmailField('Login ID:', validators=[Email(), DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Login')

    
class RegistrationForm(FlaskForm):

    username = StringField('Username:', validators=[DataRequired()])
    email = EmailField('Email:', validators=[Email(),DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password', message='Password does not match')])
    submit = SubmitField('Register')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(f"Username taken!")
    

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already registered!")
        

class UpdateUserForm(FlaskForm):

    username = StringField('Username:', validators=[DataRequired()])
    email = EmailField('Email:', validators=[Email(),DataRequired()])
    profile_pic = FileField('Update profile picture', validators=[FileAllowed(['jpg', 'jgep', 'png', 'gif'])])    
    submit = SubmitField('Save changes')

    # to ensure the updated username, email does not taken by other users
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(f"Username taken!")
    

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already registered!")
    
