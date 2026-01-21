# Automação Login Portal do Cliente 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o driver (ex: Chrome)
driver = webdriver.Chrome()
driver.get("https://bin.qa.portaldocliente.fiserv.com/")
time.sleep(5)

# Exemplo: Encontrar um campo de texto pelo ID
cpf_cnpj = driver.find_element(By.ID, "b2-b2-b4-InputMask")
cpf_cnpj.click()
time.sleep(2)
cpf_cnpj.send_keys("18711403829" + Keys.INSERT)
time.sleep(2)


# Exemplo: Encontrar um campo de texto pelo ID
senha = driver.find_element(By.ID, "b2-b2-Input_Password")
senha.click()
time.sleep(2)
senha.send_keys("Bin@12345678" + Keys.INSERT)
time.sleep(2)

entrar = driver.find_element(By.CLASS_NAME, "font-login")
entrar.click()
time.sleep(15)

# 5 Salva o screenshot no diretório atual
driver.save_screenshot("evidencia_final.png")
