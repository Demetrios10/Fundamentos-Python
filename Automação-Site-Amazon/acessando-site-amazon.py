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
botao_livros = driver.find_element(By.ID,"nav-hamburger-menu")
botao_livros.click()
time.sleep(3)


