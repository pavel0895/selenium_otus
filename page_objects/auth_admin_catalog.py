from selenium.webdriver.common.by import By
from page_objects.base_app import BasePage


class AdminCatalog(BasePage):

    def __init__(self, browser):
        self.browser = browser
        self.MENU_CATALOG = (By.XPATH, "//*[@id ='menu-catalog']")
        self.PRODUCTS_LIST = (By.XPATH, "//*[@id ='collapse-1']/li[2]")
        self.FILTER_NAME = (By.XPATH, "//*[@id = 'input-name']")

    def click_menu_catalog(self):
        self.get_element(self.MENU_CATALOG).click()

    def click_products_list(self):
        self.get_element(self.PRODUCTS_LIST).click()

    def search_field_name(self):
        self.get_element(self.FILTER_NAME)
