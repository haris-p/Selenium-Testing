import time
import pytest
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page


@pytest.mark.usefixtures("setup")
class Test_01_Admin_Login:
    admin_page_url = "https://admin-demo.nopcommerce.com/login"
    username = "admin@yourstore.com"
    password = "admin"
    invalid_username = "adminreabndom@yourstor.com"

    def test_title_verification(self):
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "nopCommerce demo store. Login"
        time.sleep(2)
        assert act_title == exp_title, f"Expected '{exp_title}', got '{act_title}'"

    def test_valid_admin_login(self):
        self.driver.get(self.admin_page_url)
        admin_lp = Login_Admin_Page(self.driver)

        admin_lp.enter_username(self.username)
        admin_lp.enter_password(self.password)
        admin_lp.click_login()
        time.sleep(2)

        act_dashboard_text = self.driver.find_element(By.XPATH, "//div[@class='content-header']/h1").text
        assert act_dashboard_text == "Dashboard", f"Expected Dashboard, got {act_dashboard_text}"

    def test_invalid_admin_login(self):
        self.driver.get(self.admin_page_url)
        admin_lp = Login_Admin_Page(self.driver)

        admin_lp.enter_username(self.invalid_username)
        admin_lp.enter_password(self.password)
        time.sleep(2)
        admin_lp.click_login()      
        time.sleep(3)
        error_message = self.driver.find_element(By.XPATH, "//li").text
        print("Error message:", error_message)
        
        assert error_message == "No customer account found", f"Unexpected message: {error_message}"