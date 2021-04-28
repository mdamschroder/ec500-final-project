from congress import Congress 
congress = Congress('fTgijhbaKjHp3PMYYv8lBR45m16pI1pbgdBedAWB')

def get_bills(chamb):

    bills = congress.bills.recent(chamber=chamb, type='active')
    return(bills)


def sort_bills(bills, sort_by):

    if sort_by:
        for bill in bills:
            if sort_by not in bill:
                bills.remove(bill)

    if sort_by:
        bills.sort(key=lambda x: x[sort_by])

    return bills
