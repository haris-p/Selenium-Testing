from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login_Admin_Page:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    btn_login_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,5)

    def enter_username(self, username):
        field = self.wait.until(
            EC.visibility_of_element_located((By.ID, self.textbox_username_id))
        )
        field.click()
        field.send_keys(Keys.CONTROL, 'a')
        field.send_keys(Keys.DELETE)
        field.send_keys(username)

    def enter_password(self, password):
        field = self.wait.until(
            EC.visibility_of_element_located((By.ID, self.textbox_password_id))
        )
        field.click()
        field.send_keys(Keys.CONTROL, 'a')
        field.send_keys(Keys.DELETE)
        field.clear()
        field.send_keys(password)
       
    def click_login(self):
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.btn_login_xpath))
        )
        button.click()