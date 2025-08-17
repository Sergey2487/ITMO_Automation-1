import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.text_box import TextBox


def test_text_box(browser):
    page = TextBox(browser)
    page.visit()

    test_name = "Николай Скобичевский"
    test_address = "СПб, ул. Турку, д. 66"

    page.name.send_keys(test_name)
    page.address.send_keys(test_address)

    browser.execute_script("arguments[0].scrollIntoView(true);", page.btn_submit.find_element())
    page.btn_submit.click()

    WebDriverWait(browser, 5).until(
        EC.visibility_of(page.displayed_info.find_element())
    )
    time.sleep(5)
    result_text = page.displayed_info.get_text()

    assert test_name in result_text, f"Имя '{test_name}' не найдено в результатах"
    assert test_address in result_text, f"Адрес '{test_address}' не найден в результатах"
