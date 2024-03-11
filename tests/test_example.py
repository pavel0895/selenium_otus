import time


def test_check_title(browser):
    browser.get(browser.base_url)
    assert "opencart" in browser.title
    time.sleep(5)
