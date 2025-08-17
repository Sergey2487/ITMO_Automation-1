from pages.login_form_validate import LoginFormValidate


def test_login_form_validate(browser):
    page = LoginFormValidate(browser)
    page.visit()

    assert not page.model_dialog.exist()

    assert page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert page.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert page.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert page.user_email.get_dom_attribute(
        'pattern') == r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight-500);")
    page.btn_submit.click()

    assert page.user_form.get_dom_attribute('class') == 'was-validated'
