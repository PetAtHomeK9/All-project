from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Set up the ChromeDriver service using webdriver_manager
service = Service(ChromeDriverManager().install())

# Initialize the Chrome browser
driver = webdriver.Chrome(service=service(ChromeDriverManager().install()))

# Open a website
driver.get("https://appclick.ng/portal/site/userlogin")

# Find an element by its name attribute
search_box = driver.find_element(By.NAME, "q")

# Perform an action (e.g., enter text and submit)
search_box.send_keys("Selenium")
search_box.submit()

# Wait for a few seconds to see the result
time.sleep(5)

# Close the browser
driver.quit()
