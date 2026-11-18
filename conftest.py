

import os
from datetime import datetime

import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config.config import (
    BROWSER,
    IMPLICIT_WAIT,
    SCREENSHOT_DIR
)


@pytest.fixture
def driver(request):

    # Browser configuration
    if BROWSER.lower() == "chrome":

        options = Options()
        options.add_argument("--disable-notifications")

        browser = webdriver.Chrome(options=options)

        # Set a consistent browser window size
        browser.set_window_size(1366, 1000)

    else:
        raise ValueError(f"Unsupported browser: {BROWSER}")

    # Browser settings
    browser.implicitly_wait(IMPLICIT_WAIT)

    # Provide browser instance to test
    yield browser

    # Check test execution result
    test_report = getattr(request.node, "rep_call", None)

    if test_report and test_report.failed:

        os.makedirs(SCREENSHOT_DIR, exist_ok=True)

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        screenshot_name = (
            f"{request.node.name}_{timestamp}.png"
        )

        screenshot_path = os.path.join(
            SCREENSHOT_DIR,
            screenshot_name
        )

        # Capture screenshot
        browser.save_screenshot(screenshot_path)

        # Attach screenshot to Allure
        allure.attach(
            browser.get_screenshot_as_png(),
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )

        # Attach HTML source
        allure.attach(
            browser.page_source,
            name="Failure Page Source",
            attachment_type=allure.attachment_type.HTML
        )

    # Close browser
    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    setattr(
        item,
        "rep_" + report.when,
        report
    )
