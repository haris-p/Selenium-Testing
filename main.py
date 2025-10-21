from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://youtube.com")
print(driver.title)
time.sleep(2)

Search_bar = driver.find_element(By.NAME,"search_query")
Search_bar.clear()
Search_bar.send_keys("getting started with python")
Search_bar.send_keys(Keys.RETURN)

time.sleep(3)

driver.quit()