from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import InputRequired,Length

class BlogForm(FlaskForm):
    title= StringField('Blog Title',validators=[InputRequired()], render_kw={"placeholder": "Enter your blog title"})
    pitch= TextAreaField('Input your blog', validators=[InputRequired(), Length(min=10, max=100)], render_kw={"placeholder": "Your blog should not exceed 100 characters"})
    submit = SubmitField('Post')