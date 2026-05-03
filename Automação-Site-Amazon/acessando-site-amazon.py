# Acessando Site Amazon

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o driver (ex: Chrome)
driver = webdriver.Chrome()
driver.get("https://www.amazon.com.br")
time.sleep(5)

# clicando no botão todos
botao_todos = driver.find_element(By.ID,"nav-hamburger-menu")
botao_todos.click()
time.sleep(5)

# clicando no botão X para fechar
botao_x = driver.find_element(By.ID,"hmenu-close-icon")
botao_x.click()
time.sleep(3)


