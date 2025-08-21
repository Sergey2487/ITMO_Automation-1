from pages.links_page import LinksPage
import time

def test_links(browser):
    links_page = LinksPage(browser)

    links_page.visit()
    assert links_page.linkHome.exist()
    assert links_page.linkHome.get_text() == 'Home'
    assert links_page.linkHome.get_dom_attribute('href') == 'https://demoqa.com'

    assert len(browser.window_handles) == 1
    links_page.linkHome.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2