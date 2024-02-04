from company_blog.blog_posts.forms import BlogPostForm
from flask import Blueprint, redirect, request, render_template, url_for, flash
from flask_login import login_required, current_user
from company_blog import db
from company_blog.models import BlogPost, User

blog_post = Blueprint('blog_post', __name__)

@blog_post.route('/add_blog', methods=['GET', 'POST'])
@login_required
def add_blog():
    
    form = BlogPostForm()

    if form.validate_on_submit():
        pass

@blog_post.route('/edit_blog', methods=['GET', 'POST'])
@login_required
def edit_blog():
    pass





