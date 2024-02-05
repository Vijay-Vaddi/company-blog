from company_blog.blog_posts.forms import BlogPostForm
from flask import Blueprint, redirect, request, render_template, url_for, flash, abort
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
@blog_posts.route('/<int:blog_post_id>')
# @login_required work on this? 
def view_blog(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    return render_template('blog_post.html', post=blog_post, title = blog_post.title,
                           date=blog_post.date)

# update blog
@blog_posts.route('/<int:blog_post_id>/update', methods=['GET', 'POST'])
@login_required
def update(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    
    if blog_post.author!=current_user:
        abort(403)
        
    form = BlogPostForm()
      
    if form.validate_on_submit():
        blog_post.title = form.title.data
        blog_post.text = form.content.data
        db.session.commit()
        flash('Blog post updated')

        return redirect(url_for('blog_posts.view_blog', blog_post_id=blog_post.id))

    # to see the original content initially, keep the data originally filled in for them
    elif request.method == 'GET':
        form.content.data = blog_post.text
        form.title.data = blog_post.title

    return render_template('create_post.html', title='Updating', form=form)

@blog_posts.route('<int:blog_post_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_post(blog_post_id):

    delete_post = BlogPost.query.get_or_404(blog_post_id)
    
    if delete_post.author != current_user:
        abort(403)

    db.session.delete(delete_post)
    db.session.commit()
    flash('Blog post deleted')

    return redirect(url_for('core.index'))



