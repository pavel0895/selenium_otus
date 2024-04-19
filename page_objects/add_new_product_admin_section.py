from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from page_objects.base_app import BasePage


class AddNewProductAdminSection(BasePage):
    def __init__(self, browser):
        self.WebDriverWait = None
        self.browser = browser
        self.LINK_ADD_NEW = (By.XPATH, "//i[@class='fa-solid fa-plus']")
        self.USERNAME_INPUT = (By.NAME, "product_description[1][name]")
        self.TAG_INPUT = (By.NAME, "product_description[1][meta_title]")
        self.TAB_DATA = (By.LINK_TEXT, "Data")
        self.MODEL_INPUT = (By.NAME, "model")
        self.TAB_SEO = (By.LINK_TEXT, "SEO")
        self.KEYWORD_INPUT = (By.NAME, "product_seo_url[0][1]")
        self.TAB_SEO = (By.LINK_TEXT, "SEO")
        self.SAVE = (By.XPATH, "//i[@class='fa-solid fa-floppy-disk']")
        self.SUCCESS_ALERT_PRODUCT = (By.CSS_SELECTOR, '.alert-success')

    def input_product_name(self, product_name):
        self.get_element(self.USERNAME_INPUT).send_keys(product_name)

    def input_model_product(self, product_model):
        self.get_element(self.MODEL_INPUT).send_keys(product_model)

    def input_tag_title(self, tag_title):
        self.get_element(self.TAG_INPUT).send_keys(tag_title)

    def input_keyword(self, keyword):
        self.get_element(self.KEYWORD_INPUT).send_keys(keyword)

    def scroll_down_products(self):
        product = self.get_element(self.TAG_INPUT)
        actions = ActionChains(self.browser)
        actions.move_to_element(product).perform()
        product.click()
        return product

    def click_add_new_product(self):
        self.get_element(self.LINK_ADD_NEW).click()

    def click_tab_data(self):
        self.get_element(self.TAB_DATA).click()

    def click_tab_seo(self):
        self.get_element(self.TAB_SEO).click()

    def click_save_product(self):
        self.get_element(self.SAVE).click()

    def success_alert_product(self):
        self.get_element(self.SUCCESS_ALERT_PRODUCT)
