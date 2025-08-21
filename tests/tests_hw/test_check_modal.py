from pages.modal_dialogs import ModalDialogPage
import pytest
import time


def test_check_Small_and_Larg(browser):
    modal_page = ModalDialogPage(browser)
    modal_page.visit()
    if not modal_page.equal_url():
        pytest.skip("404 code error.")

    assert modal_page.small_modalButton.exist()
    assert modal_page.large_modalButton.exist()

    modal_page.small_modalButton.click()
    time.sleep(2)
    assert modal_page.close_small_modalButton.exist()
    modal_page.close_small_modalButton.click()
    time.sleep(2)
    assert not modal_page.close_small_modalButton.exist()

    modal_page.large_modalButton.click()
    time.sleep(2)
    assert modal_page.close_large_modalButton.exist()
    modal_page.close_large_modalButton.click()
    time.sleep(2)
    assert not modal_page.close_large_modalButton.exist()
