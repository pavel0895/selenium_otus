import time


def test_check_title(browser):
    browser.get("https://google.com")
    assert "Google" in browser.title
    time.sleep(1)
