from pages.reg_data import reg_first_name, reg_last_name, reg_email, reg_password
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.reg_acc import RegAcc


def test_reg_acc(browser):
    browser.get(browser.base_url + "/index.php?route=account/register")
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(RegAcc.FIRST_NAME)).send_keys(reg_first_name)
    wait.until(EC.visibility_of_element_located(RegAcc.LAST_NAME)).send_keys(reg_last_name)
    wait.until(EC.visibility_of_element_located(RegAcc.EMAIL)).send_keys(reg_email)
    wait.until(EC.visibility_of_element_located(RegAcc.PASSWORD_INPUT)).send_keys(reg_password)
    wait.until(EC.visibility_of_element_located(RegAcc.CHECKBOX)).click()
    wait.until(EC.visibility_of_element_located(RegAcc.SUBMIT_BUTTON)).click()
