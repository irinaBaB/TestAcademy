
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest


class BookFlight(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_booking_flight(self):
        wd = self.wd
        wd.get("http://newtours.demoaut.com/")
        #Login
        wd.find_element_by_link_text("SIGN-ON").click()
        wd.find_element_by_name("userName").click()
        wd.find_element_by_name("userName").clear()
        wd.find_element_by_name("userName").send_keys("mercury")
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("mercury")
        wd.find_element_by_name("login").click()
        wd.find_element_by_name("passCount").click()
        Select(wd.find_element_by_name("passCount")).select_by_visible_text("2")
        wd.find_element_by_name("fromPort").click()
        Select(wd.find_element_by_name("fromPort")).select_by_visible_text("Frankfurt")
        wd.find_element_by_name("fromMonth").click()
        wd.find_element_by_name("fromDay").click()
        Select(wd.find_element_by_name("fromDay")).select_by_visible_text("17")
        wd.find_element_by_name("toPort").click()
        Select(wd.find_element_by_name("toPort")).select_by_visible_text("Paris")
        wd.find_element_by_name("toMonth").click()
        Select(wd.find_element_by_name("toMonth")).select_by_visible_text("April")
        wd.find_element_by_name("toDay").click()
        Select(wd.find_element_by_name("toDay")).select_by_visible_text("12")
        wd.find_element_by_name("findFlights").click()
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Blue Skies Airlines 361'])[1]/preceding::td[1]").click()
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Blue Skies Airlines 361'])[1]/preceding::input[1]").click()
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Blue Skies Airlines 631'])[1]/preceding::input[1]").click()
        wd.find_element_by_name("reserveFlights").click()
        wd.find_element_by_name("passFirst0").click()
        wd.find_element_by_name("passFirst0").clear()
        wd.find_element_by_name("passFirst0").send_keys("Scarlett")
        wd.find_element_by_name("passLast0").clear()
        wd.find_element_by_name("passLast0").send_keys("Harrisson")
        wd.find_element_by_name("pass.0.meal").click()
        Select(wd.find_element_by_name("pass.0.meal")).select_by_visible_text("Vegetarian")
        wd.find_element_by_name("creditCard").click()
        Select(wd.find_element_by_name("creditCard")).select_by_visible_text("Visa")
        wd.find_element_by_name("creditnumber").click()
        wd.find_element_by_name("creditnumber").clear()
        wd.find_element_by_name("creditnumber").send_keys("5678934756759")
        wd.find_element_by_name("cc_exp_dt_mn").click()
        Select(wd.find_element_by_name("cc_exp_dt_mn")).select_by_visible_text("02")
        wd.find_element_by_name("cc_exp_dt_yr").click()
        Select(wd.find_element_by_name("cc_exp_dt_yr")).select_by_visible_text("2010")
        wd.find_element_by_name("cc_frst_name").click()
        wd.find_element_by_name("cc_frst_name").clear()
        wd.find_element_by_name("cc_frst_name").send_keys("Scarlett")
        wd.find_element_by_name("cc_last_name").clear()
        wd.find_element_by_name("cc_last_name").send_keys("Harrisson")
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Address:'])[1]/following::td[1]").click()
        wd.find_element_by_name("billAddress1").click()
        wd.find_element_by_name("billAddress1").clear()
        wd.find_element_by_name("billAddress1").send_keys("12 Normanby road")
        wd.find_element_by_name("billCity").clear()
        wd.find_element_by_name("billCity").send_keys("Wellingto")
        wd.find_element_by_name("billState").clear()
        wd.find_element_by_name("billState").send_keys("")
        wd.find_element_by_name("billZip").click()
        wd.find_element_by_name("billZip").clear()
        wd.find_element_by_name("billZip").send_keys("3192")
        wd.find_element_by_xpath("//div").click()
        wd.find_element_by_name("billCountry").click()
        Select(wd.find_element_by_name("billCountry")).select_by_visible_text("NEW ZEALAND")
        wd.find_element_by_name("buyFlights").click()
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='$1177 USD'])[1]/following::img[4]").click()

    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
