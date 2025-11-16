import time
import pytest
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_01_Admin_Login:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()

    def test_title_verification(self, driver):
        driver.get(self.admin_page_url)
        act_title = driver.title
        exp_title = "nopCommerce demo store. Login"

        assert act_title == exp_title

    def test_valid_admin_login(self, driver):
        driver.get(self.admin_page_url)
        admin_lp = Login_Admin_Page(driver)
        admin_lp.enter_username(self.username)
        admin_lp.enter_password(self.password)
        admin_lp.click_login()
    
        dashboard = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='content-header']/h1"))
        )
        assert dashboard.text == "Dashboard"

    def test_invalid_admin_login(self, driver):
        driver.get(self.admin_page_url)
        admin_lp = Login_Admin_Page(driver)
        admin_lp.enter_username(self.invalid_username)
        admin_lp.enter_password(self.password)
        admin_lp.click_login()
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//li"))
        )
    
        assert error_message.text == "No customer account found"