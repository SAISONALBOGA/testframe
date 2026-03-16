from pages.test_scenarios_page import TestScenariosPage


def test_alert_handling(driver):

    page = TestScenariosPage(driver)

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    page.trigger_alert()

    alert = driver.switch_to.alert
    alert.accept()

    assert True