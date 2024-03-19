from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.product_page import ProductPage


def test_product_card(browser):
    browser.get(browser.base_url)
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(ProductPage.TABLETS_LINK)).click()
    wait.until(EC.visibility_of_element_located(ProductPage.TABLETS_CHECK)).click()
    wait.until(EC.visibility_of_element_located(ProductPage.PRICE_CHECK))
    wait.until(EC.visibility_of_element_located(ProductPage.QUANTITY_FIELD))
    wait.until(EC.visibility_of_element_located(ProductPage.BUTTON_CART)).click()
