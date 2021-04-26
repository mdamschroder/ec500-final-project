from congress import Congress 
congress = Congress('fTgijhbaKjHp3PMYYv8lBR45m16pI1pbgdBedAWB')

def get_bills(chamb):
    bills = congress.bills.recent(chamber=chamb)
    return(bills)