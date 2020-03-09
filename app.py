# app.py
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route('/index/', methods=['POST'])
def index():
   return "Hello, World!"
