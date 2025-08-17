from components.component import WebElement
from pages.base_page import BasePage


class TextBox(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.name = WebElement(driver, '#userName')
        self.email = WebElement(driver, '#userEmail')
        self.address = WebElement(driver, '#currentAddress')
        self.permanent_address = WebElement(driver, '#permanentAddress')
        self.btn_submit = WebElement(driver, '#submit')
        self.displayed_info = WebElement(driver, '#output')
