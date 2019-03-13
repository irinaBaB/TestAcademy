
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://newtours.demoaut.com/")
        #Login
        driver.find_element_by_link_text("SIGN-ON").click()
        driver.find_element_by_name("userName").click()
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys("mercury")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("mercury")
        driver.find_element_by_name("login").click()
        driver.find_element_by_name("passCount").click()
        Select(driver.find_element_by_name("passCount")).select_by_visible_text("2")
        driver.find_element_by_name("fromPort").click()
        Select(driver.find_element_by_name("fromPort")).select_by_visible_text("Frankfurt")
        driver.find_element_by_name("fromMonth").click()
        driver.find_element_by_name("fromDay").click()
        Select(driver.find_element_by_name("fromDay")).select_by_visible_text("17")
        driver.find_element_by_name("toPort").click()
        Select(driver.find_element_by_name("toPort")).select_by_visible_text("Paris")
        driver.find_element_by_name("toMonth").click()
        Select(driver.find_element_by_name("toMonth")).select_by_visible_text("April")
        driver.find_element_by_name("toDay").click()
        Select(driver.find_element_by_name("toDay")).select_by_visible_text("12")
        driver.find_element_by_name("findFlights").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Blue Skies Airlines 361'])[1]/preceding::td[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Blue Skies Airlines 361'])[1]/preceding::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Blue Skies Airlines 631'])[1]/preceding::input[1]").click()
        driver.find_element_by_name("reserveFlights").click()
        driver.find_element_by_name("passFirst0").click()
        driver.find_element_by_name("passFirst0").clear()
        driver.find_element_by_name("passFirst0").send_keys("Scarlett")
        driver.find_element_by_name("passLast0").clear()
        driver.find_element_by_name("passLast0").send_keys("Harrisson")
        driver.find_element_by_name("pass.0.meal").click()
        Select(driver.find_element_by_name("pass.0.meal")).select_by_visible_text("Vegetarian")
        driver.find_element_by_name("creditCard").click()
        Select(driver.find_element_by_name("creditCard")).select_by_visible_text("Visa")
        driver.find_element_by_name("creditnumber").click()
        driver.find_element_by_name("creditnumber").clear()
        driver.find_element_by_name("creditnumber").send_keys("5678934756759")
        driver.find_element_by_name("cc_exp_dt_mn").click()
        Select(driver.find_element_by_name("cc_exp_dt_mn")).select_by_visible_text("02")
        driver.find_element_by_name("cc_exp_dt_yr").click()
        Select(driver.find_element_by_name("cc_exp_dt_yr")).select_by_visible_text("2010")
        driver.find_element_by_name("cc_frst_name").click()
        driver.find_element_by_name("cc_frst_name").clear()
        driver.find_element_by_name("cc_frst_name").send_keys("Scarlett")
        driver.find_element_by_name("cc_last_name").clear()
        driver.find_element_by_name("cc_last_name").send_keys("Harrisson")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Address:'])[1]/following::td[1]").click()
        driver.find_element_by_name("billAddress1").click()
        driver.find_element_by_name("billAddress1").clear()
        driver.find_element_by_name("billAddress1").send_keys("12 Normanby road")
        driver.find_element_by_name("billCity").clear()
        driver.find_element_by_name("billCity").send_keys("Wellingto")
        driver.find_element_by_name("billState").clear()
        driver.find_element_by_name("billState").send_keys("")
        driver.find_element_by_name("billZip").click()
        driver.find_element_by_name("billZip").clear()
        driver.find_element_by_name("billZip").send_keys("3192")
        driver.find_element_by_xpath("//div").click()
        driver.find_element_by_name("billCountry").click()
        Select(driver.find_element_by_name("billCountry")).select_by_visible_text("NEW ZEALAND")
        driver.find_element_by_name("buyFlights").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='$1177 USD'])[1]/following::img[4]").click()

    
    def tearDown(self):
        self.driver.quit()
        # self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
