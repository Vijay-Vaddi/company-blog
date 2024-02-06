from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
# is going to allow user update/upload png/jpeg file  

from company_blog.models import User
from flask_login import current_user

class LoginForm(FlaskForm):
    
    email = StringField('Email Address:', validators=[Email(), DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Login')

    
class RegistrationForm(FlaskForm):
    
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[Email(),DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password', message="Passwords do not match")])
    submit = SubmitField('Register')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(f"Username taken!")
    

    def validate_email(self, field):       
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already registered!")
        

class UpdateUserForm(FlaskForm):

    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username:', validators=[DataRequired()])
    email = EmailField('Email:', validators=[Email(),DataRequired()])
    profile_pic = FileField('Update profile picture', validators=[FileAllowed(['jpg', 'jgep', 'png', 'gif'])])    
    submit = SubmitField('Save changes')

    # is data required while updating profile?
    # to ensure the updated username, email does not taken by other users
    def validate_username(self, field):
        if field.data!=current_user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError(f"Username taken!")
    

    def validate_email(self, field):
        if field.data!=current_user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already registered!")
    
