from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import InputRequired,Length

class BlogForm(FlaskForm):
    title= StringField('Blog Title',validators=[InputRequired()], render_kw={"placeholder": "Enter your blog title"})
    blog= TextAreaField('Input your blog', validators=[InputRequired(), Length(min=10, max=500)], render_kw={"placeholder": "Your blog should not exceed 500 characters"})
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    name = StringField('', validators=[InputRequired()], render_kw={"placeholder": "Enter your name"})
    comment = StringField('', validators=[InputRequired()], render_kw={"placeholder": "Post your comment"})
    submit = SubmitField('Post')

