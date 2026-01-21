import time
from selenium import webdriver # type: ignore

from selenium import webdriver


driver = webdriver.Chrome()

driver.get("http://selenium.dev")

driver.quit()
