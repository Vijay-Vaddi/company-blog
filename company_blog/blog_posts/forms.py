from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class BlogPostForm(FlaskForm):
    title = StringField('Title of the blog', validators=[DataRequired()])
    content = TextAreaField('Blog content', validators=[DataRequired()])
    submit = SubmitField('Post')

