from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TestScenariosPage(BasePage):

    ALERT_BUTTON = (By.XPATH, "//button[text()='Click for JS Alert']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Click for JS Confirm']")
    PROMPT_BUTTON = (By.XPATH, "//button[text()='Click for JS Prompt']")

    def trigger_alert(self):
        self.wait.wait_for_element(self.ALERT_BUTTON).click()

    def trigger_confirm(self):
        self.wait.wait_for_element(self.CONFIRM_BUTTON).click()

    def trigger_prompt(self):
        self.wait.wait_for_element(self.PROMPT_BUTTON).click()