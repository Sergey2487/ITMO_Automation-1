from components.component import WebElement
from pages.base_page import BasePage


class LinksPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/links'
        super().__init__(driver, self.base_url)
        self.linkHome = WebElement(driver, '#simpleLink')
