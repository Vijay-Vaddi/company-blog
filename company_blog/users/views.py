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
    
    return render_template('register.html', form=form)

# login
@users.route('/login', methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Login success')
            
            next = request.args.get('next')

            if next == None or not next[0]=='/':
                next = url_for('core.index')

            return redirect(next)

    return render_template('login.html', form=form)            

        




# logout
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))
# why use redirect and not render_temp

# account
# users list of blog posts
