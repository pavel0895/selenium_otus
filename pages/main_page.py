from selenium.webdriver.common.by import By


class MainPage:
    CURRENCY_FORM = (By.XPATH, "//*[@id='form-currency']/div/a/span")
    BUTTON_SEARCH = (By.CSS_SELECTOR, "button[type='button']")
    SEARCH_FIELD = (By.XPATH, "//*[@id='search']")
    LINK_OPENCART = (By.LINK_TEXT, "OpenCart")
    BUTTON_CART = (By.XPATH, "//*[@id='header-cart']/div/button")
