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