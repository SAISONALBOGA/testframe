from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.ID, "flash")

    def login(self, username, password):

        self.wait.wait_for_element(self.USERNAME).send_keys(username)
        self.wait.wait_for_element(self.PASSWORD).send_keys(password)
        self.wait.wait_for_element(self.LOGIN_BUTTON).click()