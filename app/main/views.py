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
    return render_template('index.html')

@main.route('/quotes/')
def quote():
    quote = get_quotes()
    title = 'Random Quotes'
    return render_template('quotes.html', title = title, quote = quote)

