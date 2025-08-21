from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from components.component import WebElement
from selenium.webdriver.support import expected_conditions as EC


class ModalDialogPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://demoqa.com/modal-dialogs'
        self.btns_menu_selector = '#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(3) > div > ul > li'
        self.home_icon_selector = 'header a'
        self.small_modalButton = WebElement(driver,
                                            '#showSmallModal')
        self.large_modalButton = WebElement(driver,
                                            '#showLargeModal')
        self.close_small_modalButton = WebElement(driver,
                                                  '#closeSmallModal')
        self.close_large_modalButton = WebElement(driver,
                                                  '#closeLargeModal')
        self.modalDialog = WebElement(driver,
                                      '.modal-dialog')


    def visit(self):
        self.driver.get(self.base_url)

    def check_menu_buttons_count(self, expected_count):
        try:
            elements = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, self.btns_menu_selector))
            )
            return len(elements) == expected_count
        except Exception as e:
            print(e)
            return False

    def go_to_home(self):

        home_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.home_icon_selector)))
        home_icon.click()

    def equal_url(self):
        return self.driver.current_url == self.base_url
