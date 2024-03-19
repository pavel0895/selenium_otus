from selenium.webdriver import Keys
from pages.auth_data import auth_user_name, auth_user_password
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.catalog_page import CatalogPage


def test_check_open_catalog(browser):
    browser.get(browser.base_url + "/administration")
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(CatalogPage.LOGIN_INPUT)).send_keys(auth_user_name)
    wait.until(EC.visibility_of_element_located(CatalogPage.PASSWORD_INPUT)).send_keys(auth_user_password)
    wait.until(EC.visibility_of_element_located(CatalogPage.PASSWORD_INPUT)).send_keys(Keys.ENTER)
    wait.until(EC.visibility_of_element_located(CatalogPage.MENU_CATALOG)).click()
    wait.until(EC.visibility_of_element_located(CatalogPage.PRODUCTS_LIST)).click()
    wait.until(EC.visibility_of_element_located(CatalogPage.FILTER_NAME))
    wait.until(EC.visibility_of_element_located(CatalogPage.FILTER_PRICE))
    wait.until(EC.visibility_of_element_located(CatalogPage.MODEL_NAME))
