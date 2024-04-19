from selenium.webdriver.common.by import By
from page_objects.base_app import BasePage


class LoginAdmin(BasePage):

    def __init__(self, browser):
        self.browser = browser
        self.USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
        self.PASSWORD_INPUT = (By.NAME, "password")
        self.OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
        self.FORGOTTEN_PASSWORD = (By.XPATH, "//*[text()=' No match for Username and/or Password. ']")
        self.SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    @property
    def get_field_username_input(self):
        return self.get_element(self.USERNAME_INPUT)

    @property
    def get_field_password_input(self):
        return self.get_element(self.PASSWORD_INPUT)

    @property
    def get_opencart_link(self):
        return self.get_element(self.OPENCART_LINK)

    @property
    def get_text_forgotten_password(self):
        return self.get_element(self.USERNAME_INPUT)
