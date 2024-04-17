from selenium.webdriver.common.by import By
from page_objects.base_app import BasePage


class MainPage(BasePage):

    def __init__(self, browser):
        self.browser = browser
        self.LINK_OPENCART = (By.LINK_TEXT, "Specials")
        self.SEARCH_FIELD = (By.XPATH, "//*[@id='search']")
        self.BUTTON_SEARCH = (By.CSS_SELECTOR, "button[type='button']")
        self.BUTTON_CART = (By.XPATH, "//*[@id='header-cart']/div/button")
        self.CURRENCY_FORM = (By.XPATH, "//*[@id='form-currency']/div/a/span")

    @property
    def get_link_opencart(self):
        return self.get_element(self.LINK_OPENCART)

    @property
    def get_search_field(self):
        return self.get_element(self.SEARCH_FIELD)

    @property
    def get_currency_form(self):
        return self.get_element(self.CURRENCY_FORM)

    def click_button_search(self):
        self.get_element(self.BUTTON_SEARCH).click()

    def click_button_cart(self):
        self.get_element(self.BUTTON_CART).click()
