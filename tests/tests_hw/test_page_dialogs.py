from pages.modal_dialogs import ModalDialogPage


def test_modal_elements(browser):
    modal_dialog = ModalDialogPage(browser)
    modal_dialog.visit()
    assert modal_dialog.check_menu_buttons_count(expected_count=5)


def test_navigation_modal(browser):
    modal_dialog = ModalDialogPage(browser)
    modal_dialog.visit()
    browser.refresh()
    modal_dialog.go_to_home()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert browser.current_url == 'https://demoqa.com/'
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)
