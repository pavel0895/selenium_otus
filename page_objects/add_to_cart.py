from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from page_objects.base_app import BasePage


class AddCart(BasePage):
    def __init__(self, browser):
        self.browser = browser
        self.ADD_CART = (By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/form/div/button[1]")
        self.SUCCESS_ALERT = (By.CSS_SELECTOR, '.alert-success')

    def set_window(self):
        self.browser.set_window_size(1920, 1080)

    def add_product(self):
        product = self.get_element(self.ADD_CART)
        actions = ActionChains(self.browser)
        actions.move_to_element(product).perform()
        product.click()
        return product

    def success_alert(self):
        self.get_element(self.SUCCESS_ALERT)
