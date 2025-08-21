from pages.alert_page import AlertPage
import time


def test_check_alert(browser):
    alertPage = AlertPage(browser)
    alertPage.visit()
    alertPage.alert_button .click()
    time.sleep(5)
    assert alertPage.alert()