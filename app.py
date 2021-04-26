# The main application
# Houses all API calls and routes between the HTML pages

from flask import Flask, request, render_template, redirect, json, url_for
from flask_restful import Resource, Api
app = Flask(__name__)

@app.route('/') # The homepage
def homepage():
    return render_template("homepage.html")