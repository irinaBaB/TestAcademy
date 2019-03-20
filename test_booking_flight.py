
import unittest
from flight_details import Flight
from flight_details import Payment
from application import Application


class BookFlight(unittest.TestCase):

    def setUp(self):
        self.app = Application()

    def test_booking_flight(self):
        self.app.login(username="mercury", password="mercury")
        self.app.select_flight(Flight(departure_from="Frankfurt",
                                      fromdate="17",
                                      arriving_to="Paris",
                                      returnmonth="April",
                                      returndate="12"))
        self.app.book_flight(Payment(firstname="Scarlett",
                                     lastname="Harrisson",
                                     mealpreference="Vegetarian",
                                     cardtype="Visa",
                                     cardnumber="5678934756759",
                                     dateexpiration="02",
                                     yearexpiration="2010",
                                     cc_firstname="Scarlett",
                                     cc_lastname="Harrisson",
                                     address="12 Normanby road",
                                     city="Wellingto",
                                     zipcode="3192",
                                     country="NEW ZEALAND"))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
