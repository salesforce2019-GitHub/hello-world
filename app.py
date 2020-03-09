# app.py
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

