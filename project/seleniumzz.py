from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.python.org/")

print(driver.title)
download_list = driver.find_element(by=By.CSS_SELECTOR, value="li[class='tier-1 element-2   with-supernav']")
print(download_list)

download_list.click()


time.sleep(10)


