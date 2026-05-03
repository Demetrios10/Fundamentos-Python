# Acessando Site Linkedin

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o driver (ex: Chrome)
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/")
time.sleep(5)

# clicando botão vagas 
botao_vagas = driver.find_element(By.XPATH,"//a[contains(@href,'linkedin.com/jobs/search')]")
botao_vagas.click()
time.sleep(5)
