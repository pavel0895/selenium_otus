from selenium.webdriver.common.by import By
from page_objects.base_app import BasePage


class AuthAdmin(BasePage):
    def __init__(self, browser):
        self.browser = browser
        self.AUTH_LINK = (By.XPATH, '//span[contains(text(), "John Doe")]')
        self.LOGOUT_LINK = (By.XPATH, '//span[contains(text(), "Logout")]')
        self.SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
        self.USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
        self.PASSWORD_INPUT = (By.NAME, "password")

    @property
    def find_username(self):
        return self.get_element(self.AUTH_LINK)

    def logout(self):
        self.get_element(self.LOGOUT_LINK).click()
