# Automação Login Portal do Cliente 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.chrome.service import Service

# Define o nome da pasta
pasta_evidencias = 'evidencias'
# Cria a pasta se ela não existir
if not os.path.exists(pasta_evidencias):
    os.makedirs(pasta_evidencias)

# Inicializa o driver (ex: Chrome)
driver = webdriver.Chrome()
driver.get("https://bin.qa.portaldocliente.fiserv.com/")
time.sleep(5)

# Exemplo: Encontrar um campo de texto pelo ID
cpf_cnpj = driver.find_element(By.ID, "b2-b2-b4-InputMask")
cpf_cnpj.click()
time.sleep(1)
cpf_cnpj.send_keys("18711403829" + Keys.INSERT)
time.sleep(1)


# Exemplo: Encontrar um campo de texto pelo ID
senha = driver.find_element(By.ID, "b2-b2-Input_Password")
senha.click()
time.sleep(1)
senha.send_keys("Bin@12345678" + Keys.INSERT)
time.sleep(1)

caminho_foto = os.path.join(pasta_evidencias, "evidencia_1.png")
driver.save_screenshot(caminho_foto)
print(f"Evidência salva em: {caminho_foto}")

entrar = driver.find_element(By.CLASS_NAME, "font-login")
entrar.click()
time.sleep(10)
caminho_foto = os.path.join(pasta_evidencias, "evidencia_2.png")
driver.save_screenshot(caminho_foto)
print(f"Evidência salva em: {caminho_foto}")

acesso_rapido_antecipacao = driver.find_element(By.ID,"b10-AntecipacaoDiv2")
acesso_rapido_antecipacao.click()
time.sleep(15)
caminho_foto = os.path.join(pasta_evidencias, "evidencia_3.png")
driver.save_screenshot(caminho_foto)
print(f"Evidência salva em: {caminho_foto}")

troca_estabelecimento = driver.find_element(By.ID,"b5-b3-$b2")
troca_estabelecimento.click()
time.sleep(15)

caminho_foto = os.path.join(pasta_evidencias, "ultima_evidencia.png")
driver.save_screenshot(caminho_foto)
print(f"Evidência salva em: {caminho_foto}")

