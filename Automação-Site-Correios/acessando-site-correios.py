# Acessando Site Correios

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o driver (ex: Chrome)
driver = webdriver.Chrome()
driver.get("https://www.correios.com.br/")
time.sleep(5)

# clicando no botão enviar
botao_enviar = driver.find_element(By.ID,"itemMenu_enviar")
botao_enviar.click()
time.sleep(3)

# clicando no botão receber
botao_receber = driver.find_element(By.ID, "itemMenu_receber")
botao_receber.click()
time.sleep(3)

# clicando no botão comprar
botao_comprar = driver.find_element(By.ID, "itemMenu_comprar")
botao_comprar.click()
time.sleep(3)

