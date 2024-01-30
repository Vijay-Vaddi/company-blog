from flask import redirect, render_template, url_for, request, Blueprint, flash
from flask_login import login_required, login_user, logout_user, current_user
from company_blog.users.forms import LoginForm, RegistrationForm, UpdateUserForm
from company_blog.models import User, BlogPost
from company_blog.users.picture_handler import add_profile_pic
from company_blog import db

users = Blueprint('users', __name__)

# register
@users.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        name = form.username.data
        email = form.email.data
        password = form.password.data

        new_user = User(name,email,password)
        db.session.add(new_user)
        db.session.commit()
        flash('Thanks for registering') 
        return redirect(url_for('users.login'))
    
    return render_template('register.html')






# login
# logout
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))
# why use redirect and not render_temp

# account
# users list of blog posts
