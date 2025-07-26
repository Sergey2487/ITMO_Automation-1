from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = "https://www.saucedemo.com/"

    def visit(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator)
