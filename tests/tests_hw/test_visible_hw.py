import time
import pytest
from pages.accordion import AccordionPage


def test_visible_accordion(browser):
    accordion_page = AccordionPage(browser)

    accordion_page.visit()

    assert accordion_page.section1_content.visible()
    assert accordion_page.section1_heading.visible()

    accordion_page.section1_heading.click()

    time.sleep(2)

    assert not accordion_page.section1_content.visible()


def test_visible_accordion_default(browser):
    accordion_page = AccordionPage(browser)

    accordion_page.visit()

    assert not accordion_page.section2_content_p1.visible()
    assert not accordion_page.section2_content_p2.visible()
    assert not accordion_page.section3_content.visible()
