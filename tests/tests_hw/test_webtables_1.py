from pages.click_Add import WebTables
from selenium.webdriver.common.keys import Keys
import time


def test_webtables_1(browser):
    webtable_page = WebTables(browser)
    webtable_page.visit()

    webtable_page.add_record.click()
    time.sleep(1)
    assert webtable_page.alert_dialog.exist()
    assert not webtable_page.alert_dialog_submit.click()
    assert webtable_page.send_form()
    assert webtable_page.tableCell_4.get_text() == 'bro'

    webtable_page.edit_record4.click()
    time.sleep(1)
    assert webtable_page.alert_dialog.exist()
    webtable_page.alert_dialog_firstname.clear()
    webtable_page.alert_dialog_firstname.send_keys('firstname')
    webtable_page.alert_dialog_submit.click()
    assert webtable_page.tableCell_4.get_text() == 'firstname'

    webtable_page.delete_record4.click()
    assert webtable_page.tableCell_4.get_text().strip() == ''


def test_webtables_2(browser):
    webtable_page = WebTables(browser)
    webtable_page.visit()

    webtable_page.rows_count.scroll_to_element()
    webtable_page.rows_count.click()
    webtable_page.rows_count.send_keys(Keys.PAGE_UP)
    webtable_page.rows_count.send_keys(Keys.ENTER)

    assert not webtable_page.next_button.click()
    assert not webtable_page.previous_button.click()
    assert webtable_page.next_button.get_dom_attribute('disabled') == 'true'
    assert webtable_page.previous_button.get_dom_attribute('disabled') == 'true'

    for _ in range(4):
        webtable_page.add_record.click()
        webtable_page.send_form()

    webtable_page.next_button.click()
    assert webtable_page.table_page.get_dom_attribute('value') == '2'

    webtable_page.previous_button.click()
    assert webtable_page.table_page.get_dom_attribute('value') == '1'
