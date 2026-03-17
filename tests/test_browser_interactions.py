from pages.scenarios_page import ScenariosPage


def test_alert_handling(driver):

    page = ScenariosPage(driver)

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    page.trigger_alert()

    alert = driver.switch_to.alert
    alert.accept()

    assert True