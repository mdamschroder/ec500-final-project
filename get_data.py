from get_current_members import get_house, get_senators, get_member
import threading

CURRENT_SESSION = 117
all_senators = []
all_reps = []

# Get all senators info
def get_all_senators():
    global all_senators

    if len(all_senators) == 0:

        senators = get_senators()
        senators = senators[0]['members']

        for senator in senators:
            all_senators.append(get_member(senator['id']))


# Returns party line voting percentage for given party
def party_line_data(session, party):

    global all_members
    if not isinstance(session, int):
        session = int(session)

    if not all_senators:
        get_all_senators()

    data = []
    for i in range(CURRENT_SESSION - session + 1):
        data.append([session+i, 0, 0])

    # Compile data
    for congress in data:
        for member in all_senators:
            if party:
                if member['current_party'] != party:
                    continue
            for role in member['roles']:
                if int(role['congress']) == congress[0]:
                    congress[1] += role['total_votes'] * role['votes_with_party_pct']
                    congress[2] += role['total_votes']

    for congress in data:
        congress[1] = float(congress[1]/congress[2])
        congress.remove(congress[2])

    return [i for i in reversed(data)]


# Returns dw nominate scores for specified chamber
def dw_nominate(chamber):

    if chamber == "House":
        members = get_house()[0]['members']
    elif chamber == "Senate":
        members = get_senators()[0]['members']
    else:
        members = get_house()[0]['members']
        members += get_senators()[0]['members']

    data = []
    for member in members:
        if 'dw_nominate' in member and member['dw_nominate']:
            data.append([member['first_name'] + ' ' + member['last_name'], member['dw_nominate']])

    return data


# Returns seniority and dw-nominate data for all congress members
def seniority_data():

    members = get_house()[0]['members']
    members += get_senators()[0]['members']

    data = []
    for member in members:
        if 'seniority' in member and member['seniority'] and 'dw_nominate' in member and member['dw_nominate']:
            data.append([member['first_name'] + ' ' + member['last_name'], member['dw_nominate'], member['seniority']])

    return data


# Returns party-line voting and dw-nominate data for all congress members
def dw_line_data():

    members = get_house()[0]['members']
    members += get_senators()[0]['members']

    data = []
    for member in members:
        if 'votes_with_party_pct' in member and member['votes_with_party_pct'] and 'dw_nominate' in member and member['dw_nominate']:
            data.append([member['first_name'] + ' ' + member['last_name'], member['dw_nominate'], member['votes_with_party_pct']])

    return data
