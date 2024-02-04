from company_blog.blog_posts.forms import BlogPostForm
from flask import Blueprint, redirect, request, render_template, url_for, flash
from flask_login import login_required, current_user
from company_blog import db
from company_blog.models import BlogPost

blog_posts = Blueprint('blog_posts', __name__)

# add blog post
@blog_posts.route('/create_blog', methods=['GET', 'POST'])
@login_required
def create_blog():
    
    form = BlogPostForm()

    if form.validate_on_submit():
        print('inside blog valid')        
        post = BlogPost(title = form.title.data,
                        text = form.content.data,
                        user_id = current_user.id)
       
        db.session.add(post)
        db.session.commit()
        flash('Successfully posted')
        return redirect(url_for('core.index'))
        
    return render_template('create_blog.html', form=form)


# view 
@blog_posts.route('/view_blogs')
@login_required
def view_blogs():
    pass
    # page = request.args.get('page', 1, type=int)

    # posts = BlogPost.query.filter_by(author=current_user.id).order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
    # return render_template('view_blogs.html', posts=posts)

# update blog
@blog_posts.route('/edit_blog', methods=['GET', 'POST'])
@login_required
def edit_blog():
    pass





