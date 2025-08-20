from pages.click_Add import WebTables
import time

def test_webtables(browser):
    webtable_page = WebTables(browser)
    webtable_page.visit()

    assert not webtable_page.tableCell_1.get_text() == ''
    webtable_page.delete_record1.click()
    webtable_page.delete_record2.click()
    webtable_page.delete_record3.click()
    time.sleep(1)
    assert webtable_page.tableCell_1.get_text() == ' '