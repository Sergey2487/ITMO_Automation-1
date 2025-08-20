from pages.base_page import BasePage
from selenium.common import NoSuchElementException
from components.component import WebElement


class WebTables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.Header_column1 = WebElement(driver,
                                         'div.rt-th:nth-child(1)')
        self.Header_column2 = WebElement(driver,
                                         'div.rt-th:nth-child(2) > div:nth-child(1)')
        self.Header_column3 = WebElement(driver,
                                         'div.rt-th:nth-child(1) > div:nth-child(1)')
        self.Header_column4 = WebElement(driver,
                                         'div.rt-th:nth-child(1) > div:nth-child(1)')
        self.table_page = WebElement(driver,
                                     '.-pageJump > input:nth-child(1)')
        self.add_record = WebElement(driver,
                                     '#addNewRecordButton')
        self.delete_record1 = WebElement(driver,
                                         '#delete-record-1')
        self.delete_record2 = WebElement(driver,
                                         '#delete-record-2')
        self.delete_record3 = WebElement(driver,
                                         '#delete-record-3')
        self.delete_record4 = WebElement(driver,
                                         '#delete-record-4')
        self.edit_record4 = WebElement(driver,
                                       '#edit-record-4')

        self.alert_dialog = WebElement(driver,
                                       '.modal-dialog')
        self.alert_dialog_firstname = WebElement(driver,
                                                 '#firstName')
        self.alert_dialog_lastname = WebElement(driver,
                                                '#lastName')
        self.alert_dialog_email = WebElement(driver,
                                             '#userEmail')
        self.alert_dialog_age = WebElement(driver,
                                           '#age')
        self.alert_dialog_salary = WebElement(driver,
                                              '#salary')
        self.alert_dialog_departament = WebElement(driver,
                                                   '#department')
        self.alert_dialog_submit = WebElement(driver,
                                              '#submit')

        self.no_rows_message = WebElement(driver,
                                          '.rt-noData')
        self.tableCell_1 = WebElement(driver,
                                      'div.rt-tr-group:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
        self.tableCell_4 = WebElement(driver,
                                      'div.rt-tr-group:nth-child(4) > div:nth-child(1) > div:nth-child(1)')
        self.table_head_firstname = WebElement(driver,
                                               'div.rt-th:nth-child(1)')
        self.table_head_lastname = WebElement(driver,
                                              'div.rt-th:nth-child(2)')
        self.table_head_age = WebElement(driver,
                                         'div.rt-th:nth-child(3)')
        self.table_head_email = WebElement(driver,
                                           'div.rt-th:nth-child(4)')
        self.table_head_salary = WebElement(driver,
                                            'div.rt-th:nth-child(5)')
        self.table_head_departament = WebElement(driver,
                                                 'div.rt-th:nth-child(6)')
        self.table_body = WebElement(driver,
                                     'div.rt-tr-group:nth-child(1)')
        self.rows_count = WebElement(driver,
                                     '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select',
        )

        self.next_button = WebElement(driver,
                                      '.-next > button:nth-child(1)')
        self.previous_button = WebElement(driver,
                                          '.-previous > button:nth-child(1)')

    def send_form(self) -> bool:
        try:
            if self.alert_dialog.exist():
                self.alert_dialog_firstname.send_keys('bro')
                self.alert_dialog_lastname.send_keys('Bros')
                self.alert_dialog_email.send_keys('bro@mail.ru')
                self.alert_dialog_age.send_keys('8')
                self.alert_dialog_salary.send_keys('30000')
                self.alert_dialog_departament.send_keys('zxc')
                self.alert_dialog_submit.click()
                return True
        except Exception as ex:
            print(ex)
            return False
