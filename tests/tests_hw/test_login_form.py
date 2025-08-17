from pages.login_form_validate import LoginFormValidate
import time


def test_login_form(browser):
    login_form = LoginFormValidate(browser)
    login_form.visit()
    assert not login_form.model_dialog.exist()

    time.sleep(2)
    login_form.first_name.send_keys("Sergey")
    login_form.last_name.send_keys("Dod")
    login_form.user_email.send_keys("ddddd@mail.ru")
    login_form.current_address.send_keys("123456")
    login_form.gender_radio_1.click_force()
    login_form.user_number.send_keys("12341234123")
    time.sleep(5)
    login_form.hobbies.click_force()
    time.sleep(10)
    login_form.btn_submit.click_force()
    time.sleep(20)

    assert login_form.model_dialog.exist()
    login_form.btn_close_model.click_force()


def test_login_form2(browser):
    login_form = LoginFormValidate(browser)
    login_form.visit()
    assert not login_form.model_dialog.exist()

    time.sleep(10)
    login_form.state_dropdown_btn.click()
    time.sleep(10)

    if login_form.state_first_item.visible():
        login_form.state_first_item.click()
    time.sleep(10)
    login_form.city_dropdown_btn.click()
    if login_form.city_first_item.visible():
        login_form.city_first_item.click()
    time.sleep(10)

    assert not login_form.model_dialog.exist()

