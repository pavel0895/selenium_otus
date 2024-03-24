from pages.main_page import MainPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_cart(browser):
    wait = WebDriverWait(browser, 10)
    browser.get(browser.base_url)
    browser.set_window_size(1920, 1080)
    product = wait.until(EC.visibility_of_element_located(MainPage.ADD_CART))
    actions = ActionChains(browser)
    actions.move_to_element(product).perform()
    product.click()
    wait.until(EC.visibility_of_element_located(MainPage.SUCCESS_ALERT))
