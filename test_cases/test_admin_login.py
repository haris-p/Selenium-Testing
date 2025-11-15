import time
import pytest
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page

class Test_01_Admin_Login:

    admin_page_url = "https://admin-demo.nopcommerce.com/login"
    username = "admin@yourstore.com"
    password = "admin"
    invalid_username = "adminreabndom@yourstor.com"

    def test_title_verification(self, driver):
        driver.get(self.admin_page_url)
        time.sleep(2)

        act_title = driver.title
        exp_title = "nopCommerce demo store. Login"

        assert act_title == exp_title

    def test_valid_admin_login(self, driver):
        driver.get(self.admin_page_url)
        admin_lp = Login_Admin_Page(driver)

        admin_lp.enter_username(self.username)
        admin_lp.enter_password(self.password)
        admin_lp.click_login()
        time.sleep(3)

        act_dashboard_text = driver.find_element(By.XPATH, "//div[@class='content-header']/h1").text
        assert act_dashboard_text == "Dashboard"

    def test_invalid_admin_login(self, driver):
        driver.get(self.admin_page_url)
        admin_lp = Login_Admin_Page(driver)

        admin_lp.enter_username(self.invalid_username)
        admin_lp.enter_password(self.password)
        admin_lp.click_login()
        time.sleep(3)

        error_message = driver.find_element(By.XPATH, "//li").text
        assert error_message == "No customer account found"