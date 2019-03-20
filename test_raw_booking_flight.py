
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from flight_details import Flight
from flight_details import Payment

class BookFlight(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(100)

    def test_booking_flight(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="mercury", password="mercury")
        self.select_flight(wd, Flight(departure_from="Frankfurt",
                           fromdate="17",
                           arriving_to="Paris",
                           returnmonth="April",
                           returndate="12"))
        self.book_flight(wd, Payment(firstname="Scarlett",
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
        self.confirm_purchase(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='$1177 USD'])[1]/following::img[4]").click()

    def confirm_purchase(self, wd):
        wd.find_element_by_name("buyFlights").click()

    def book_flight(self, wd, payment):
        #enter the passnger details
        wd.find_element_by_name("reserveFlights").click()
        wd.find_element_by_name("passFirst0").click()
        wd.find_element_by_name("passFirst0").clear()
        wd.find_element_by_name("passFirst0").send_keys(payment.firstname)
        wd.find_element_by_name("passLast0").clear()
        wd.find_element_by_name("passLast0").send_keys(payment.lastname)
        #select meal preference
        wd.find_element_by_name("pass.0.meal").click()
        Select(wd.find_element_by_name("pass.0.meal")).select_by_visible_text(payment.mealpreference)
        #enter credit card details
        wd.find_element_by_name("creditCard").click()
        Select(wd.find_element_by_name("creditCard")).select_by_visible_text(payment.cardtype)
        wd.find_element_by_name("creditnumber").click()
        wd.find_element_by_name("creditnumber").clear()
        wd.find_element_by_name("creditnumber").send_keys(payment.cardnumber)
        wd.find_element_by_name("cc_exp_dt_mn").click()
        Select(wd.find_element_by_name("cc_exp_dt_mn")).select_by_visible_text(payment.dateexpiration)
        wd.find_element_by_name("cc_exp_dt_yr").click()
        Select(wd.find_element_by_name("cc_exp_dt_yr")).select_by_visible_text(payment.yearexpiration)
        wd.find_element_by_name("cc_frst_name").click()
        wd.find_element_by_name("cc_frst_name").clear()
        wd.find_element_by_name("cc_frst_name").send_keys(payment.cc_firstname)
        wd.find_element_by_name("cc_last_name").clear()
        wd.find_element_by_name("cc_last_name").send_keys(payment.cc_lastname)
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Address:'])[1]/following::td[1]").click()
        wd.find_element_by_name("billAddress1").click()
        wd.find_element_by_name("billAddress1").clear()
        wd.find_element_by_name("billAddress1").send_keys(payment.address)
        wd.find_element_by_name("billCity").clear()
        wd.find_element_by_name("billCity").send_keys(payment.city)
        wd.find_element_by_name("billState").clear()
        wd.find_element_by_name("billState").send_keys("")
        wd.find_element_by_name("billZip").click()
        wd.find_element_by_name("billZip").clear()
        wd.find_element_by_name("billZip").send_keys(payment.zipcode)
        wd.find_element_by_xpath("//div").click()
        wd.find_element_by_name("billCountry").click()
        Select(wd.find_element_by_name("billCountry")).select_by_visible_text(payment.country)

    def select_flight(self, wd, flight_details):
        #select flight from
        wd.find_element_by_name("fromPort").click()
        Select(wd.find_element_by_name("fromPort")).select_by_visible_text(flight_details.departure_from)
        wd.find_element_by_name("fromMonth").click()
        wd.find_element_by_name("fromDay").click()
        Select(wd.find_element_by_name("fromDay")).select_by_visible_text(flight_details.fromdate)
        #select flight to
        wd.find_element_by_name("toPort").click()
        Select(wd.find_element_by_name("toPort")).select_by_visible_text(flight_details.arriving_to)
        wd.find_element_by_name("toMonth").click()
        Select(wd.find_element_by_name("toMonth")).select_by_visible_text(flight_details.returnmonth)
        wd.find_element_by_name("toDay").click()
        Select(wd.find_element_by_name("toDay")).select_by_visible_text(flight_details.returndate)
        wd.find_element_by_name("findFlights").click()
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Blue Skies Airlines 361'])[1]/preceding::td[1]").click()
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Blue Skies Airlines 361'])[1]/preceding::input[1]").click()
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Blue Skies Airlines 631'])[1]/preceding::input[1]").click()

    def login(self, wd, username, password):
        wd.find_element_by_link_text("SIGN-ON").click()
        wd.find_element_by_name("userName").click()
        wd.find_element_by_name("userName").clear()
        wd.find_element_by_name("userName").send_keys(username)
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_name("login").click()
        wd.find_element_by_name("passCount").click()
        Select(wd.find_element_by_name("passCount")).select_by_visible_text("2")

    def open_home_page(self, wd):
        wd.get("http://newtours.demoaut.com/")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
