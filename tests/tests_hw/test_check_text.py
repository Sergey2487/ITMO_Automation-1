from pages.demoqa import DemoQaPage
from pages.elements_page import ElementsPage
import time

from conftest import browser


def test_check_footer(browser):
    demo_qa_page = DemoQaPage(browser)
    demo_qa_page.visit()
    time.sleep(3)
    assert demo_qa_page.text_footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_check_text_please(browser):
    demo_qa_page = DemoQaPage(browser)
    el_page = ElementsPage(browser)

    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()

    assert el_page.text_please.get_text() == 'Please select an item from left to start practice.'
