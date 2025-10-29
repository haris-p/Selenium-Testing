import pytest
import os
import time
from selenium import webdriver

# === Fixture setup/teardown driver ===
@pytest.fixture
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()


# === Hook pytest untuk ambil screenshot otomatis ===
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Jalankan proses test dulu
    outcome = yield
    report = outcome.get_result()
    driver = getattr(item.instance, "driver", None)

    # Pastikan folder screenshot ada
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    screenshot_dir = os.path.join(base_dir, "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)

    # Nama file screenshot
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    test_name = item.name

    # 🔹 Screenshot saat test FAIL
    if report.when == "call" and report.failed and driver:
        screenshot_path = os.path.join(screenshot_dir, f"{test_name}_FAILED_{timestamp}.png")
        driver.save_screenshot(screenshot_path)
        print(f"\n❌ Screenshot disimpan di: {screenshot_path}")

    # 🔹 Screenshot saat test PASS
    elif report.when == "call" and report.passed and driver:
        screenshot_path = os.path.join(screenshot_dir, f"{test_name}_PASSED_{timestamp}.png")
        driver.save_screenshot(screenshot_path)
        print(f"\n✅ Screenshot disimpan di: {screenshot_path}")