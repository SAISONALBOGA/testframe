import pytest
from pages.login_page import LoginPage
from config.settings import BASE_URL


def test_valid_login(driver):

    login = LoginPage(driver)

    login.open(BASE_URL)

    login.login("tomsmith", "SuperSecretPassword!")

    assert "secure" in driver.current_url


@pytest.mark.parametrize("username,password", [
    ("wrong", "wrong"),
    ("tomsmith", "wrong"),
    ("", "")
])
def test_invalid_login(driver, username, password):

    login = LoginPage(driver)

    login.open(BASE_URL)

    login.login(username, password)

    assert "login" in driver.current_url