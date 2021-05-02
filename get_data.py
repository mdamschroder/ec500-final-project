from get_current_members import get_house, get_senators, get_member


CURRENT_SESSION = 117
all_members = None

# Returns party line voting percentage for given party
def party_line_data(session, party):

    global all_members
    if not isinstance(session, int):
        session = int(session)

    if not all_members:
        # Get all congress members
        members = get_house()
        members = members[0]['members']
        senators = get_senators()
        members = senators[0]['members']
    
        all_members = []
        for member in members:
            all_members.append(get_member(member['id']))

    data = []
    for i in range(CURRENT_SESSION - session + 1):
        data.append([session+i, 0, 0])

    # Compile data
    for congress in data:
        for member in all_members:
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