from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import logging

class BasePage:
    def __init__(self, driver: WebDriver, base_url: str = None):
        self.driver = driver
        self.base_url = base_url if base_url else "https://www.saucedemo.com/"

    def visit(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def get_url(self):
        return self.driver.current_url

    def equal_url(self):
        if self.get_url().rstrip('/') == self.base_url:
            return True
        else:
            return False

    def alert(self):
        try:
            return self.driver.switch_to.alert
        except Exception as ex:
            logging.log(1, ex)
            return False
