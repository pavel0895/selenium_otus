from selenium.webdriver.common.by import By

from page_objects.base_app import BasePage


class DeleteProductAdminSection(BasePage):
    def __init__(self, browser):
        self.browser = browser
        self.CHECKBOX = (By.XPATH, "//*[@id = 'form-product']/div[1]/table/tbody/tr[1]/td[1]/input")
        self.DELETE_BUTTON = (By.XPATH, "//i[@class='fa-regular fa-trash-can']")

    def click_checkbox(self):
        self.browser.find_element(self.CHECKBOX).click()

    def click_delete_button(self):
        self.browser.find_element(self.DELETE_BUTTON).click()
