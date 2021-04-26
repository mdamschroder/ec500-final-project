# The main application
# Houses all API calls and routes between the HTML pages

from flask import Flask, request, render_template, redirect, json, url_for
from flask_restful import Resource, Api
from get_current_members import get_house, get_senators, filter_members
from get_bills import get_bills
app = Flask(__name__)
CONGRESS_API_KEY = 'fTgijhbaKjHp3PMYYv8lBR45m16pI1pbgdBedAWB'

############# *** THE HOMEPAGE *** #############
@app.route('/')
def homepage():
    return render_template("homepage.html")

############# *** GET CURRENT MEMBERS *** #############
@app.route('/current_members')
def current_members():

    state = request.args.get("state")
    party = request.args.get("party")

    # Get members
    house_members = get_house()
    senate_members = get_senators()

    # Filter members
    house_members = filter_members(house_members, state, party)
    senate_members = filter_members(senate_members, state, party)

    return render_template("current_members.html", house=house_members, senate=senate_members)

@app.route('/get_bills')
def recent_bills():
    house_bills = get_bills('house')
    senate_bills = get_bills('senate')
    return render_template("recent_bills.html", house_bills=house_bills['bills'], senate_bills=senate_bills['bills'])