import pytest
import os, time
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# =========================================
# FIXTURE DRIVER (BERSIH)
# =========================================
@pytest.fixture(scope="class")
def driver(request):
    options = uc.ChromeOptions()

    # Matikan autofill & password manager
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-autofill")
    options.add_argument("--disable-save-password-bubble")

    driver = uc.Chrome(options=options)
    driver.maximize_window()

    # Global wait
    driver.wait = WebDriverWait(driver, 15)

    request.cls.driver = driver
    yield driver
    driver.quit()


# =========================================
# PYTEST HOOK → SCREENSHOT PASS & FAIL
# =========================================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    driver = item.funcargs.get("driver", None)
    if driver is None:
        return

    # Folder screenshot
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    screenshot_dir = os.path.join(base_dir, "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    test_name = item.name
    status = "FAILED" if report.failed else "PASSED"
    path = os.path.join(screenshot_dir, f"{test_name}_{status}_{timestamp}.png")

    # Tangkap screenshot hanya saat tahap "call"
    if report.when == "call":
        try:
            driver.wait.until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
        except:
            pass
        time.sleep(1)

        # Debug URL
        print("\n🌐 URL saat screenshot:", driver.current_url)
        driver.save_screenshot(path)
        if report.failed:
            print(f"❌ Screenshot disimpan: {path}")
        else:
            print(f"✅ Screenshot disimpan: {path}")