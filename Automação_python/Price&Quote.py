# baixar as bibliotecas
# py -m pip install pyautogui
# py -m pip install selenium

import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException


# Configurar o WebDriver para usar o Firefox com opções
options = Options()
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0")

download_folder = r'caminho_da_pasta' # salva o arquivo localmente
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", download_folder)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
options.set_preference("pdfjs.disabled", True)

driver = webdriver.Firefox(options=options)

# Acesse a página desejada
driver.get("_url_")

# Aguarde a página carregar
time.sleep(5)

# Preencha a autenticação do pop-up
pyautogui.write('user')
pyautogui.press('tab') 
pyautogui.write('senha')
pyautogui.press('enter')  

time.sleep(10)

# Encontrar os campos de login e senha
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[contains(@class, " x-form-text x-form-field x-abs-layout-item") and @type="text"]'))
)
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[contains(@class, " x-form-text x-form-field x-abs-layout-item") and @type="password"]'))
)

# Inserir o login e a senha
username_field.send_keys('user')
password_field.send_keys('senha')
time.sleep(5)


# Encontrar e clicar no botão de login
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@type="button" and contains(@class, "x-btn-text") and text()="Login"]')))
login_button.click()

time.sleep(5)


try:
    applications_td = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//td[@id="ext-gen128"]'))
    )
    applications_button = applications_td.find_element(By.XPATH, './/button[@type="button" and contains(@class, "x-btn-text") and text()="Applications"]')
    applications_button.click()
    time.sleep(5)

    # Espere que a lista esteja visível e então clique em um elemento dela (quotation lines)
    quotation_lines_item_in_applications = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, '//li[contains(@id, "ItemQuotationLines")]/a[contains(@class, "x-menu-item") and contains(span/text(), "Quotation lines")]'))
    )
    quotation_lines_item_in_applications.click()
    time.sleep(5)
    
    # Clique direito na tabela 
    right_click = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@id, "ext-gen168") and contains(@class, "x-window-body x-window-body-noborder")]' ))
    )
    time.sleep(5)
    # Crie uma instância de ActionChains
    actions = ActionChains(driver)

    actions.context_click(right_click).perform()
    time.sleep(5)

    # Localiza o elemento filtro na tela
    filter_table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//li[contains(@id, "ToolBar.LookupToolStrip.Filter")]'))
    )

    # Crie uma instância de ActionChains
    actions = ActionChains(driver)
    # Mova o cursor sobre o elemento
    actions.move_to_element(filter_table).perform()
    time.sleep(5)

    # Clicar para filtrar
    quotations_qlik = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, '//li[contains(@id, "ToolBar.LookupToolStrip.Filter.1237199")]'))
    )
    quotations_qlik.click()
    time.sleep(5)

    # Ache a div, clique direito para selecionar o botão de exportar
    right_click = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@id, "ext-gen168") and contains(@class, "x-window-body x-window-body-noborder")]' ))
    )
    actions = ActionChains(driver)
    actions.context_click(right_click).perform()
    time.sleep(5)


    export_list = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, '//li[contains(@id, "ToolBar.ActionsToolStrip.Export")]'))
    )
    export_list.click()
    time.sleep(5)

    # Clique no botão de Exportar! 
    export_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/button[@type="button" and contains(@class, "x-btn-text") and text()="Export"]')) 
    )
    export_button.click()
    time.sleep(5)

except TimeoutException:
    print("Um dos elementos não foi encontrado ou não estava visível.")

# Encerre o driver depois de 2 minutos
time.sleep(120)
driver.quit()