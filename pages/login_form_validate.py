from components.component import WebElement
from pages.base_page import BasePage


class LoginFormValidate(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver,self.base_url)

        self.first_name = WebElement(driver,'#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.gender_radio_1 = WebElement(driver, '#gender-radio-1')
        self.user_number = WebElement(driver, '#userNumber')
        self.btn_submit = WebElement(driver, '#submit')
        self.model_dialog = WebElement(driver, 'body > div.fade.modal.show > div')
        self.btn_close_model = WebElement(driver, '#closeLargeModal')
        self.hobbies = WebElement(driver, '#subjects-label')
        self.current_address = WebElement(driver, '#currentAddress')
        self.user_form = WebElement(self.driver, '#userForm')

        self.state_dropdown_btn = WebElement(self.driver,
                                             '#state')
        self.city_dropdown_btn = WebElement(self.driver,
                                             '#city')

        self.state_first_item = WebElement(self.driver, '#react-select-3-option-0')
        self.city_first_item = WebElement(self.driver, '#react-select-4-option-0')
        self.btn_NCR = WebElement(driver, ("xpath", "//*[contains(text(), 'NCR')]"))

