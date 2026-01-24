# logando no site saucedemo

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o driver (ex: Chrome)
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(5)

# preenchendo usuario
usuario = driver.find_element(By.ID,"user-name")
usuario.click()
time.sleep(1)
usuario.send_keys("standard_user" + Keys.INSERT)
time.sleep(1)

# preenchendo senha
senha = driver.find_element(By.ID,"password")
senha.click()
time.sleep(1)
senha.send_keys("secret_sauce" + Keys.INSERT)
time.sleep(1)

# clicando no botão login 
botao_login = driver.find_element(By.ID,"login-button")
botao_login.click()
time.sleep(10)






