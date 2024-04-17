from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from page_objects.base_app import BasePage


class AccRegistration(BasePage):
    path = "/index.php?route=account/register"

    def __init__(self, browser):
        self.browser = browser
        self.FIRST_NAME = (By.XPATH, "//*[@id='input-firstname']")
        self.LAST_NAME = (By.XPATH, "//*[@id='input-lastname']")
        self.EMAIL = (By.XPATH, "//*[@id='input-email']")
        self.PASSWORD_INPUT = (By.XPATH, "//*[@id='input-password']")
        self.CHECKBOX = (By.NAME, "agree")
        self.SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def open_registration_acc(self, browser):
        self.browser.get(browser.base_url + self.path)

    def input_first_name(self, firstname):
        self.get_element(self.FIRST_NAME).send_keys(firstname)

    def input_last_name(self, lastname):
        self.get_element(self.LAST_NAME).send_keys(lastname)

    def input_email(self, email):
        self.get_element(self.EMAIL).send_keys(email)

    def input_password(self, password):
        self.get_element(self.PASSWORD_INPUT).send_keys(password)

    def click_checkbox(self):
        self.get_element(self.CHECKBOX).click()

    def scroll_down_acc_registration(self):
        product = self.get_element(self.CHECKBOX)
        actions = ActionChains(self.browser)
        actions.move_to_element(product).perform()
        product.click()
        return product
