from congress import Congress 
congress = Congress('fTgijhbaKjHp3PMYYv8lBR45m16pI1pbgdBedAWB')

def get_senators():
    members = congress.members.filter('senate')
    print("Senators Grabbed")
    return(members)

def get_house():
    members = congress.members.filter('house')
    print("House Grabbed")
    return(members)

def filter_members(members, state, party):
    
    # Filter by state
    if state:
        results = list(filter(lambda x: x['state'] == state, members[0]['members']))
    else:
        results = members[0]['members']

    # Filter by party
    if party:
        if party == 'R' or party == 'D':
            results = list(filter(lambda x: x['party'] == party, results))
        else:
            results = list(filter(lambda x: x['party'] != 'R' and x['party'] != 'D', results))

    # Only include those in office
    results = list(filter(lambda x: x['in_office'] == True, results))

    return results

