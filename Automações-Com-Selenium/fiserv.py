# logando no site da fiserv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.fiserv.com.br/")
time.sleep(5)

diminuir_tudo = driver.find_element(By.ID,"_evidon-barrier-declinebutton")
diminuir_tudo.click()
time.sleep(5)

quem_atendemos = driver.find_element(By.CLASS_NAME,"has-submenu")
quem_atendemos.click()
time.sleep(5)