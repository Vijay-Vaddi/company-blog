from flask import redirect, render_template, url_for, request, Blueprint, flash
from flask_login import login_required, login_user, logout_user, current_user
from company_blog.users.forms import LoginForm, RegistrationForm, UpdateUserForm
from company_blog.models import User, BlogPost
from company_blog.users.picture_handler import add_profile_pic
from company_blog import db

users = Blueprint('users', __name__)

# Register User
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

# Login User
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

# Logout User
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))
    # why use redirect and not render_temp

# Update Account
@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateUserForm()

    if form.validate_on_submit(): 
        
        if form.profile_pic.data:
            username = current_user.username
            pic = add_profile_pic(form.profile_pic.data, username)
            current_user.profile_pic = pic

        # if form.email.data:
            # check if email unique
        current_user.email = form.email.data
        
        # if form.username.data:
        current_user.username = form.username.data
        
        db.session.commit()

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    # if they're not submitting anything we're grabbing their current info. 
    # why we're doing this? 
    
    profile_pic = url_for('static', filename ='profile_pics/'+current_user.profile_pic)
    # to pass a profile pic, grab the whatever value from the current users profile_pic value, either default or already updated. 
    #what does url_for does here? 
    return render_template('account.html', form=form, profile_pic=profile_pic) 

# User Posts
@users.route("/<username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    # grab whatever page you're currently on, its connected to the page call showing certain no. of posts per page.  
    user = User.query.filter_by(username=username).first_or_404()
    blog_posts = BlogPost.query.filter_by(author=user).order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)

    return render_template('user_blog_post.html', user=user, blog_posts=blog_posts)                





# users list of blog posts
