from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class WebElement:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def click(self):
        self.find_element().click()

    def click_force(self):
        self.driver.execute_script('arguments[0].click();', self.find_element())

    def send_keys(self, text):
        self.find_element().send_keys(text)

    def find_elements(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        return str(self.find_element().text)

    def get_dom_attribute(self, name: str):
        value = self.find_element().get_dom_attribute(name)
        if value is None:
            return False

        if len(value) > 0:
            return value

        return True

    def get_by_type(self):
        if self.locator_type == 'id':
            return By.ID
        elif self.locator_type == 'name':
            return By.NAME
        elif self.locator_type == 'xpath':
            return By.XPATH
        elif self.locator_type == 'css':
            return By.CSS_SELECTOR
        elif self.locator_type == 'class':
            return By.CLASS_NAME
        elif self.locator_type == 'link':
            return By.LINK_TEXT
        else:
            print("Locator type" + self.locator_type + "not correct")
            return False

    def visible(self):
        try:
            return self.find_element().is_displayed()
        except NoSuchElementException:
            return False

    def not_visible(self):
        return not self.find_element().is_displayed()
