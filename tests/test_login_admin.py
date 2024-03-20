from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_admin_page import LoginAdminPage


def test_login_admin(browser):
    browser.get(browser.base_url + "/administration")
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(LoginAdminPage.USERNAME_INPUT))
    wait.until(EC.visibility_of_element_located(LoginAdminPage.PASSWORD_INPUT))
    wait.until(EC.visibility_of_element_located(LoginAdminPage.OPENCART_LINK))
    wait.until(EC.visibility_of_element_located(LoginAdminPage.SUBMIT_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(LoginAdminPage.FORGOTTEN_PASSWORD))
