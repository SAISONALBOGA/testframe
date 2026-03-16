import pytest
from utils.driver_factory import create_driver
from utils.screenshot_utils import take_screenshot


@pytest.fixture
def driver():

    driver = create_driver()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs["driver"]

        take_screenshot(driver, item.name)