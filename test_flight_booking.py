# -*- coding: utf-8 -*-

import unittest
from flight_details import Booking
from flight_details import Payment
from application import Application

class TestFlightBooking(unittest.TestCase):

    def setUp(self):
        self.app = Application()

    def test_flight_booking(self):
        self.app.login(username="mercury", password="mercury")
        self.app.flight_booking(Booking(from_port="London",
                                departure_month="April",
                                departure_date="7",
                                to_port="New York",
                                return_month= "April",
                                return_date= "20"))
        self.app.flight_purchase(Payment(pas_first_name="helen",
                                 pas_last_name="conor",
                                 meal_option="Vegetarian",
                                 cc_type="Visa",
                                 cc_number="4678576578",
                                 cc_exp_month="07",
                                 cc_exp_year="2010",
                                 bill_address="12 Normanbyroad",
                                 city="auckland",
                                 zip_code="3192",
                                 country="NEW ZEALAND"))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
