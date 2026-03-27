# Importar as bibliotecas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys # Utlizar teclado com Selenium
import time
from webdriver_manager.chrome import ChromeDriverManager

# Configurar serviço do chrome
servico = Service(ChromeDriverManager().install())

# Navegar até o whatsapp
driver = webdriver.Chrome(service=servico)
driver.get('https://web.whatsapp.com/') #get para pegar a URL do whatsapp
time.sleep(40)

# Selecionar o Contatos e grupos
contatos = ['Saquarema - Agenda', 'Erika Louise']
mensagem = 'Ola, foi um prazer'

def buscarContato(contato):
    campoPesquisa = driver.find_element('xpath','//*[@id="_r_9_"]')
    time.sleep(3)
    campoPesquisa.click()
    campoPesquisa.send_keys(contato)
    campoPesquisa.send_keys(Keys.ENTER)
    time.sleep(2)

def enviarMensagem(mensagem):
    campoMensagem = driver.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span/div/div/div/div[3]/div[1]/p')
    time.sleep(3)
    campoMensagem.click()
    campoMensagem.send_keys(mensagem)
    campoMensagem.send_keys(Keys.ENTER)
    time.sleep(3)

# Enviar mensagem para contato ou grupo
for contato in contatos:
    buscarContato(contato)
    enviarMensagem(mensagem)
