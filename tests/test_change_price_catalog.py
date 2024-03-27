from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_change_price_catalog_desktops(browser):
    wait = WebDriverWait(browser, 10)
    browser.get(browser.base_url + "/en-gb/catalog/desktops")
    product_price_dollar = wait.until(EC.presence_of_all_elements_located(MainPage.PRODUCT_LIST))
    price_before_change = [price.text for price in product_price_dollar]
    wait.until(EC.visibility_of_element_located(MainPage.CHANGE_CURRENCY)).click()
    wait.until(EC.visibility_of_element_located(MainPage.EURO_CURRENCY)).click()
    product_price_euro = wait.until(EC.presence_of_all_elements_located(MainPage.PRODUCT_LIST))
    price_after_change = [price.text for price in product_price_euro]
    assert price_after_change != price_before_change, "Цены изменились при переключении валюты"
