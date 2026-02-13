# Meu Perfil

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o driver (ex: Chrome)
driver = webdriver.Chrome()
driver.get("")
time.sleep(5)

# preenchendo usuario
cpf_cnpj = driver.find_element(By.ID,"b2-b2-b4-InputMask")
cpf_cnpj.click()
time.sleep(3)
cpf_cnpj.send_keys("" + Keys.INSERT)

# preenchendo senha
cpf_cnpj = driver.find_element(By.ID,"b2-b2-Input_Password")
cpf_cnpj.click()
time.sleep(3)
cpf_cnpj.send_keys("" + Keys.INSERT)

# clicando no Botão entrar 
botao_entrar = driver.find_element(By.ID,"b2-b2-b9-SVG")
botao_entrar.click()
time.sleep(10)

# clicando no Botão meu perfil
botao_meu_perfil = driver.find_element(By.ID,"b2-$b4")
botao_meu_perfil.click()
time.sleep(10)