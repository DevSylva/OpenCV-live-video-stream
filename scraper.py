from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# driver = webdriver.Chrome(chrome_driver_path)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://google.com")
print(driver.title)
driver.quit()