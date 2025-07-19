from pages.base_page import BasePage
from components.component import WebElement


class ElementsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://demoqa.com/elements"
        self.text_please = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6')


    def get_center_text(self):
        return self.find_element("#app > div > div > div > div.col-12.mt-4.col-md-6").text
