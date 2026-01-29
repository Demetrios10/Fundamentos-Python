 # Bater ponto de entrada no ADP  

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o driver (ex: Chrome)
driver = webdriver.Chrome()
driver.get("")
time.sleep(10)

# preenchendo usuario
cpf_cnpj = driver.find_element(By.ID,"login")
cpf_cnpj.click()
time.sleep(1)
cpf_cnpj.send_keys("" + Keys.INSERT)

# preenchendo senha
cpf_cnpj = driver.find_element(By.ID,"login-pw")
cpf_cnpj.click()
time.sleep(1)
cpf_cnpj.send_keys("" + Keys.INSERT)

# clicando no Botão entrar 
botao_entrar = driver.find_element(By.CLASS_NAME,"button_primary")
botao_entrar.click()
time.sleep(20)

# clicando no Botão bater ponto 
botao_bater_ponto = driver.find_element(By.CLASS_NAME,"")
botao_bater_ponto.click()
time.sleep(10)
