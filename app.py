# The main application
# Houses all API calls and routes between the HTML pages

from flask import Flask, request, render_template, redirect, json, url_for
from flask_restful import Resource, Api
from get_current_members import get_house, get_senators
app = Flask(__name__)
CONGRESS_API_KEY = 'fTgijhbaKjHp3PMYYv8lBR45m16pI1pbgdBedAWB'

############# *** THE HOMEPAGE *** #############
@app.route('/')
def homepage():
    return render_template("homepage.html")

############# *** GET CURRENT MEMBERS *** #############
@app.route('/get_all_current')
def current_members():
    house_members = get_house()
    senate_members = get_senators()
    return render_template("current_members.html", house=house_members[0]['members'], senate=senate_members[0]['members'])