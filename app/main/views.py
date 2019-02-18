from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required
from .. request import get_quotes
from . import main
from ..models import Writer

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

@main.route('/user/<w_id>')
def profile(w_id):
    writer = Writer.query.filter_by(id = w_id).first()

    if writer is None:
        abort(404)

    return render_template("profile/profile.html", writer = writer)