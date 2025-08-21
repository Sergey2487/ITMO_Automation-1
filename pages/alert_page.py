from pages.base_page import BasePage
from components.component import WebElement


class AlertPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)

        self.alert_button = WebElement(driver, '#alertButton')
        self.timer_alert_button = WebElement(driver, '#timerAlertButton')
        self.confirm_button = WebElement(driver, '#confirmButton')
        self.prompt_button = WebElement(driver, '#promtButton')
        self.confirm_result = WebElement(driver, '#confirmResult')
        self.prompt_result = WebElement(driver, '#promptResult')

