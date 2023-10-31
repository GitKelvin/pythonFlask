'''
Store page templates in this file
URL paths are defined here
'''

from flask import Blueprint

views = Blueprint('views', __name__)

# Decorator
@views.route('/')
def home():
    return "<h1> Test </h1>"
