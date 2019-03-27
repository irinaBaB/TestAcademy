# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest


class TestFlightBooking(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='drivers/chromedriver')
        self.driver.implicitly_wait(30)

    def test_flight_booking(self):
        driver = self.driver
        driver.get("http://newtours.demoaut.com/mercurysignon.php")
        driver.find_element_by_name("userName").click()
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys("mercury")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("mercury")
        driver.find_element_by_name("login").click()
        driver.find_element_by_name("tripType").click()
        driver.find_element_by_xpath("//select[@name='passCount']").click()
        driver.find_element_by_name("passCount").click()
        driver.find_element_by_name("fromPort").click()
        Select(driver.find_element_by_name("fromPort")).select_by_visible_text("London")
        driver.find_element_by_name("fromMonth").click()
        Select(driver.find_element_by_name("fromMonth")).select_by_visible_text("April")
        driver.find_element_by_name("fromDay").click()
        Select(driver.find_element_by_name("fromDay")).select_by_visible_text("7")
        driver.find_element_by_name("toPort").click()
        Select(driver.find_element_by_name("toPort")).select_by_visible_text("New York")
        driver.find_element_by_name("toMonth").click()
        Select(driver.find_element_by_name("toMonth")).select_by_visible_text("April")
        driver.find_element_by_name("toDay").click()
        Select(driver.find_element_by_name("toDay")).select_by_visible_text("20")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Airline:'])[1]/preceding::input[2]").click()
        driver.find_element_by_name("airline").click()
        Select(driver.find_element_by_name("airline")).select_by_visible_text("Blue Skies Airlines")
        driver.find_element_by_name("findFlights").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Blue Skies Airlines 361'])[1]/preceding::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Blue Skies Airlines 631'])[1]/preceding::input[1]").click()
        driver.find_element_by_name("reserveFlights").click()
        driver.find_element_by_name("passFirst0").click()
        driver.find_element_by_name("passFirst0").clear()
        driver.find_element_by_name("passFirst0").send_keys("helen")
        driver.find_element_by_name("passLast0").clear()
        driver.find_element_by_name("passLast0").send_keys("conor")
        driver.find_element_by_name("pass.0.meal").click()
        Select(driver.find_element_by_name("pass.0.meal")).select_by_visible_text("Vegetarian")
        driver.find_element_by_name("creditCard").click()
        Select(driver.find_element_by_name("creditCard")).select_by_visible_text("Visa")
        driver.find_element_by_name("creditnumber").click()
        driver.find_element_by_name("creditnumber").clear()
        driver.find_element_by_name("creditnumber").send_keys("4678576578")
        driver.find_element_by_name("cc_exp_dt_mn").click()
        Select(driver.find_element_by_name("cc_exp_dt_mn")).select_by_visible_text("07")
        driver.find_element_by_name("cc_exp_dt_yr").click()
        Select(driver.find_element_by_name("cc_exp_dt_yr")).select_by_visible_text("2010")
        driver.find_element_by_name("cc_frst_name").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Billing Address'])[1]/following::tr[1]").click()
        driver.find_element_by_name("billAddress1").clear()
        driver.find_element_by_name("billAddress1").send_keys("12 Normanbyroad")
        driver.find_element_by_name("billCity").click()
        driver.find_element_by_name("billCity").clear()
        driver.find_element_by_name("billCity").send_keys("auckland")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='State/Province:'])[1]/following::td[1]").click()
        driver.find_element_by_name("billState").click()
        driver.find_element_by_name("billState").clear()
        driver.find_element_by_name("billState").send_keys("")
        driver.find_element_by_name("billZip").click()
        driver.find_element_by_name("billZip").clear()
        driver.find_element_by_name("billZip").send_keys("3192")
        driver.find_element_by_name("billCountry").click()
        Select(driver.find_element_by_name("billCountry")).select_by_visible_text("NEW ZEALAND")
        driver.find_element_by_name("buyFlights").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='$588 USD'])[1]/following::img[4]").click()
    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
