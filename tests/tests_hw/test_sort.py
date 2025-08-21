from pages.click_Add import WebTables
import time


def test_web_tables(browser):
    webtable_page = WebTables(browser)
    webtable_page.visit()
    time.sleep(2)
    webtable_page.table_head_firstname.click()
    table_list = webtable_page.table_body.find_elements()

    webtable_page.table_head_lastname.click()
    table_list = webtable_page.table_body.find_elements()

    webtable_page.table_head_age.click()
    table_list = webtable_page.table_body.find_elements()

    webtable_page.table_head_salary.click()
    table_list = webtable_page.table_body.find_elements()

    webtable_page.table_head_email.click()
    table_list = webtable_page.table_body.find_elements()

    webtable_page.table_head_departament.click()
    table_list = webtable_page.table_body.find_elements()
