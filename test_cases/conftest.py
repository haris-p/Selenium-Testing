import pytest
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os, time
import random

# ============================
# DRIVER FIXTURE UNIVERSAL
# ============================
@pytest.fixture
def driver():
    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = uc.Chrome(
        options=options,
        suppress_warnings=True,
        use_subprocess=True
    )

    driver.maximize_window()
    yield driver
    driver.quit()

# ============================
# SCREENSHOT HOOK
# ============================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    driver = item.funcargs.get("driver", None)

    # Buat folder screenshot
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    screenshot_dir = os.path.join(base_dir, "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    test_name = item.name

    # Screenshot saat FAIL
    if report.when == "call" and report.failed and driver:
        path = os.path.join(screenshot_dir, f"{test_name}_FAILED_{timestamp}.png")
        driver.save_screenshot(path)
        print(f"\n❌ Screenshot disimpan: {path}")

    # Screenshot saat PASS
    if report.when == "call" and report.passed and driver:
        path = os.path.join(screenshot_dir, f"{test_name}_PASSED_{timestamp}.png")
        driver.save_screenshot(path)
        print(f"\n✅ Screenshot disimpan: {path}")