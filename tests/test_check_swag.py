from pages.swag_labs import SwagLabs


def test_check_icon_exist(browser):
    page = SwagLabs(browser)
    page.visit()
    assert page.exist_icon()


def test_check_username_field_exist(browser):
    page = SwagLabs(browser)
    page.visit()
    assert page.exist_username_field()


def test_check_password_field_exist(browser):
    page = SwagLabs(browser)
    page.visit()
    assert page.exist_password_field()
