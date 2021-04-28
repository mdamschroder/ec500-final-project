# The main application
# Houses all API calls and routes between the HTML pages

from flask import Flask, request, render_template, redirect, json, url_for
from flask_restful import Resource, Api
from get_current_members import get_house, get_senators, filter_members, sort_members, get_member
from get_bills import get_bills, sort_bills
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
    sort_by = request.args.get("sort")

    # Get members
    house_members = get_house()
    senate_members = get_senators()

    # Filter members
    house_members = filter_members(house_members, state, party)
    senate_members = filter_members(senate_members, state, party)

    # Sort members
    house_members = sort_members(house_members, sort_by)
    senate_members = sort_members(senate_members, sort_by)

    return render_template("current_members.html", house=house_members, senate=senate_members, sort_by=sort_by)

############# *** MEMBER PAGE *** #############
@app.route('/member/<id>')
def member_info(id=None):

    info = get_member(id)
    
    # Collect voting data for party line voting graph
    data = "";
    for role in info['roles']:
        if 'votes_with_party_pct' in role:
            data+=role['congress']
            data+=','
            data+=str(role['votes_with_party_pct'])
            data+=','
    data = data[:len(data) - 1]

    return render_template("member.html", info=info, votes=data, len=len(info['roles']))

############# *** THE BILLS PAGE *** #############
@app.route('/get_bills')
def recent_bills():

    party = request.args.get("party")
    sort_by = request.args.get("sort")

    # Get bills
    house_bills = get_bills('house')
    senate_bills = get_bills('senate')

    house_bills = house_bills['bills']
    senate_bills = senate_bills['bills']

    # Filter bills
    if party:
        house_bills = list(filter(lambda x: x['sponsor_party'] == party, house_bills))
        senate_bills = list(filter(lambda x: x['sponsor_party'] == party, senate_bills))

    # Sort bills
    house_bills = sort_bills(house_bills, sort_by)
    senate_bills = sort_bills(senate_bills, sort_by)


    return render_template("recent_bills.html", house_bills=house_bills, senate_bills=senate_bills, sort_by=sort_by)