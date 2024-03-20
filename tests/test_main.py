from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import MainPage


def test_check_main(browser):
    wait = WebDriverWait(browser, 5)
    browser.get(browser.base_url)
    wait.until(EC.visibility_of_element_located(MainPage.LINK_OPENCART))
    wait.until(EC.visibility_of_element_located(MainPage.SEARCH_FIELD))
    wait.until(EC.visibility_of_element_located(MainPage.BUTTON_SEARCH)).click()
    wait.until(EC.visibility_of_element_located(MainPage.BUTTON_CART)).click()
    wait.until(EC.visibility_of_element_located(MainPage.CURRENCY_FORM))
