from flask import render_template,request,redirect,url_for,abort,flash,session
from flask_login import login_required,current_user
from .. request import get_quotes
from . import main
from ..models import Writer,Blog,Comment
from .forms import BlogForm,CommentForm
from .. import db

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    myquote = get_quotes()

    quote = myquote['quote']
    quote_author = myquote['author']

    return render_template('index.html',quote = quote, quote_author =  quote_author)

@main.route('/user/<w_id>',methods = ['GET','POST'])
def profile(w_id):
    writer = Writer.query.filter_by(id = w_id).first()

    if writer is None:
        abort(404)

    bform = BlogForm()
    if bform.validate_on_submit():
        newtitle = bform.title.data
        newblog = bform.blog.data

        new_blog = Blog(title = newtitle, blog = newblog, writer_id = writer.id)

        #update the blog
        new_blog.save_blog()

        return redirect(url_for('main.blogs'))

    return render_template("profile/profile.html", writer = writer, blog_form = bform)

@main.route('/blogs', methods = ['GET','POST'])
def blogs():
    blogs = Blog.query.order_by(Blog.timestamp.desc()).all()

    return render_template('blogs.html', blogs = blogs)

@main.route('/blog/<b_id>',methods = ['GET','POST'])
def oneblog(b_id):
    blog = Blog.query.filter_by(id = b_id).first()

    cform = CommentForm()
    if cform.validate_on_submit():
        comment = Comment(body=cform.body.data, blog=blog, b_id=current_user._get_current_object())
        db.session.add(comment)
        flash('Your comment has been published.')
        return redirect(url_for('.oneblog', id=blog.id ))

    return render_template('oneblog.html', blog = blog, comment_form = cform)



