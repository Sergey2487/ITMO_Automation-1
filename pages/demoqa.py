from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from components.component import WebElement


class DemoQaPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://demoqa.com/"

        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1) > div')
        self.text_footer = WebElement(driver, '#app > footer')

    def get_footer_text(self):
        return self.find_element("footer span").text

    def click_elements_button(self):
        self.find_element("#app > div > div > div.home-body > div > div:nth-child(1) > div").click()
