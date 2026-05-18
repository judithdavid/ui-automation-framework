# import os
# import pytest
# from datetime import datetime

# from utils.driver_factory import create_driver


# @pytest.fixture
# def driver():

#     driver = create_driver()

#     yield driver

#     driver.quit()


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):

#     outcome = yield
#     report = outcome.get_result()

#     if report.when == "call" and report.failed:

#         driver = item.funcargs.get("driver")

#         if driver:

#             os.makedirs("screenshots", exist_ok=True)

#             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

#             screenshot_name = (
#                 f"screenshots/{item.name}_{timestamp}.png"
#             )

#             driver.save_screenshot(screenshot_name)

import os
import pytest
from datetime import datetime

from utils.driver_factory import create_driver
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.fixture
def driver():

    driver = create_driver()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            screenshot_name = (
                f"screenshots/{item.name}_{timestamp}.png"
            )

            driver.save_screenshot(screenshot_name)

            logger.error(
                f"Screenshot captured: {screenshot_name}"
            )