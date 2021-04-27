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

def sort_members(members, sort_by):

    # Remove members without key
    if sort_by:
        for member in members:
            if sort_by not in member:
                members.remove(member)

    if sort_by:
        if sort_by == "seniority":
            members.sort(key=lambda x: int(x[sort_by]), reverse=True)
        elif sort_by == "missed_votes_pct":
            members.sort(key=lambda x: x[sort_by], reverse=True)
        else:
            members.sort(key=lambda x: x[sort_by])

    return members

