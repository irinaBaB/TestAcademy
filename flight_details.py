
class Payment:

    def __init__(self,firstname, lastname, mealpreference, cardtype, cardnumber, dateexpiration, yearexpiration,
                    cc_firstname, cc_lastname, address, city, zipcode, country,):
        self.firstname = firstname
        self.lastname = lastname
        self.mealpreference = mealpreference
        self.cardtype = cardtype
        self.cardnumber = cardnumber
        self.dateexpiration = dateexpiration
        self.yearexpiration = yearexpiration
        self.cc_firstname = cc_firstname
        self.cc_lastname = cc_lastname
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.country = country


class Flight:

    def __init__(self,departure_from, fromdate, arriving_to, returnmonth, returndate):
        self.departure_from = departure_from
        self.fromdate = fromdate
        self.arriving_to = arriving_to
        self.returnmonth = returnmonth
        self.returndate = returndate

