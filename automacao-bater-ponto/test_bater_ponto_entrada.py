 # Bater ponto de entrada no ADP  

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o driver (ex: Chrome)
driver = webdriver.Chrome()
driver.get("https://expert.cloud.brasil.adp.com/ipclogin/1/loginform.html?TYPE=33554433&REALMOID=06-000f0243-eb2e-117b-922c-11720acb0000&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-t8SOWIK%2fgJwbjEv4UX5gkf1B0Omto2OBtIjuIUUFMSwG89pqbtT%2bKprwK%2fbvYoHl&TARGET=-SM-http%3a%2f%2fexpert%2ecloud%2ebrasil%2eadp%2ecom%2fexpert%2f")
time.sleep(10)

# preenchendo usuario
cpf_cnpj = driver.find_element(By.ID,"login")
cpf_cnpj.click()
time.sleep(1)
cpf_cnpj.send_keys("demetrios.silva.1" + Keys.INSERT)
time.sleep(1)

# preenchendo senha
cpf_cnpj = driver.find_element(By.ID,"login-pw")
cpf_cnpj.click()
time.sleep(1)
cpf_cnpj.send_keys("Nubank@123" + Keys.INSERT)
time.sleep(1)