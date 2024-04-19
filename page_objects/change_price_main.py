from selenium.webdriver.common.by import By
from page_objects.base_app import BasePage


class PriceMain(BasePage):

    def __init__(self, browser):
        self.browser = browser
        self.MAIN_PRODUCTS = (By.ID, "content")
        self.POUND_CURRENCY = (By.LINK_TEXT, "£ Pound Sterling")

    def get_price_dollar(self):
        return self.get_all_elements(self.MAIN_PRODUCTS)

    def get_pound_currency(self):
        self.get_element(self.POUND_CURRENCY).click()

    def get_price_pound(self):
        return self.get_all_elements(self.MAIN_PRODUCTS)

    def get_price_change_pound(self, product_price_pound_sterling):
        self.price_after_change = [price.text for price in product_price_pound_sterling]
