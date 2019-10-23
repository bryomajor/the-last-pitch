from flask import render_template
from . import main

@main.route('/', methods = ['GET', 'POST'])
def index():
    '''
    View root page function that returns the index page and it's data
    '''
    title = 'Home'

    return render_template('home.html', title = title)