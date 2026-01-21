from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1 Inicializa o driver (ex: Chrome)
driver = webdriver.Chrome()

try:
    # 2. Navegar até a página
    driver.get("https://bin.qa.portaldocliente.fiserv.com/")
    time.sleep(5)

    # 3 Seleciona o elemento
    botao_login = driver.find_element(By.ID,"b2-b2-b4-InputMask")
    
    
    # 4. Clicar no elemento
    botao_login.click()
    time.sleep(5)

    # 5 Salva o screenshot no diretório atual
    driver.save_screenshot("evidencia_final.png")
finally:
    driver.quit()