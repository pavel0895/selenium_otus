from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_admin_page import LoginAdminPage
from pages.auth_data import auth_user_name, auth_user_password


def test_auth_admin(browser):
    browser.get(browser.base_url + "/administration")
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(LoginAdminPage.USERNAME_INPUT)).send_keys(auth_user_name)
    wait.until(EC.visibility_of_element_located(LoginAdminPage.PASSWORD_INPUT)).send_keys(auth_user_password)
    wait.until(EC.visibility_of_element_located(LoginAdminPage.SUBMIT_BUTTON)).click()
    find_username = wait.until(EC.presence_of_element_located((LoginAdminPage.AUTH_LINK)))
    assert find_username.is_displayed()
    wait.until(EC.visibility_of_element_located(LoginAdminPage.LOGOUT_LINK)).click()
