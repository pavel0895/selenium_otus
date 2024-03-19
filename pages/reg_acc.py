from selenium.webdriver.common.by import By


class RegAcc:
    FIRST_NAME = (By.XPATH, "//*[@id='input-firstname']")
    LAST_NAME = (By.XPATH, "//*[@id='input-lastname']")
    EMAIL = (By.XPATH, "//*[@id='input-email']")
    PASSWORD_INPUT = (By.XPATH, "//*[@id='input-password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    CHECKBOX = (By.NAME, "agree")
