from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required
from .. request import get_quotes
from . import main

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

