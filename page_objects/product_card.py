from selenium.webdriver.common.by import By
from page_objects.base_app import BasePage


class ProductCard(BasePage):

    def __init__(self, browser):
        self.browser = browser
        self.TABLETS_LINK = (By.LINK_TEXT, "Tablets")
        self.TABLETS_CHECK = (By.LINK_TEXT, "Samsung Galaxy Tab 10.1")
        self.PRICE_CHECK = (By.CLASS_NAME, "price-new")
        self.QUANTITY_FIELD = (By.XPATH, "//*[@id ='input-quantity']")
        self.BUTTON_CART = (By.XPATH, "//*[@id ='button-cart']")

    def get_tablets_link(self):
        self.browser.find_element(self.TABLETS_LINK).click()

    def get_tablets_check(self):
        self.browser.find_element(self.TABLETS_CHECK).click()

    @property
    def get_price_check(self):
        return self.browser.find_element(self.PRICE_CHECK)

    @property
    def get_quantity_field(self):
        return self.browser.find_element(self.QUANTITY_FIELD)

    def click_button_cart(self):
        self.browser.find_element(self.BUTTON_CART).click()
