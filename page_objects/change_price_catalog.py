from selenium.webdriver.common.by import By
from page_objects.base_app import BasePage


class PriceCatalog(BasePage):
    path = "/en-gb/catalog/desktops"

    def __init__(self, browser):
        self.browser = browser
        self.PRODUCT_LIST = (By.ID, "product-list")
        self.CHANGE_CURRENCY = (By.XPATH, "//span[contains(text(), 'Currency')]")
        self.EURO_CURRENCY = (By.LINK_TEXT, "€ Euro")

    def open_catalog(self, browser):
        self.browser.get(browser.base_url + self.path)

    def get_product_price_dollar(self):
        return self.get_all_elements(self.PRODUCT_LIST)

    def get_price_change_dollar(self, product_price_dollar):
        self.price_before_change = [price.text for price in product_price_dollar]

    def get_change_currency(self):
        self.get_element(self.CHANGE_CURRENCY).click()

    def get_euro_currency(self):
        self.get_element(self.EURO_CURRENCY).click()

    def get_product_price_euro(self):
        return self.get_all_elements(self.PRODUCT_LIST)

    def get_price_change_euro(self, product_price_euro):
        self.price_after_change = [price.text for price in product_price_euro]

    @property
    def check_price(self):
        return self.price_after_change != self.price_before_change
