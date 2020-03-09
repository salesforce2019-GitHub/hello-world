# app.py
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def index():
    ### return "<h1>Welcome to our server - ashish !!</h1>"
 user = {'username': 'Miguel'}
    ## return render_template('index.html', title='Home', user=user)
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
