
import pytest
from flight_details import Flight
from flight_details import Payment
from application import Application
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_booking_flight(app):
    app.login(username="mercury", password="mercury")
    app.select_flight(Flight(departure_from="Frankfurt",
                             fromdate="17",
                             arriving_to="Paris",
                             returnmonth="April",
                             returndate="12"))
    app.book_flight(Payment(firstname="Scarlett",
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
    assert(app.is_text_present("itinerary has been booked!"))

    assert(app.if_regex_present("Your \W +itinerary has been booked!"))


    app.logout()
