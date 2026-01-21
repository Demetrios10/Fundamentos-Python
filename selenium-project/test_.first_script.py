import time
from selenium import webdriver # type: ignore

driver = webdriver.Chrome()
driver.get("http://selenium.dev")
time.sleep(3)

driver.quit()