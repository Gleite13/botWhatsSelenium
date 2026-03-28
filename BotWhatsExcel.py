import time

import openpyxl
from urllib.parse import quote  # para enviar corretamente a mensagem  dentro do link
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys # Utlizar teclado com Selenium


# Configurar serviço do chrome
servico = Service(ChromeDriverManager().install())

# Navegar até o whatsapp
driver = webdriver.Chrome(service=servico)
driver.get('https://web.whatsapp.com/') #get para pegar a URL do whatsapp
time.sleep(40)


# Carregar o Excel

workbook = openpyxl.load_workbook('clientes.xlsx')
paginaClientes = workbook['Planilha1']

# clicar em enviar Mensagem



for linha in paginaClientes.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value

    mensagem = f'Olá {nome} estou testando um programa no python {vencimento}'

    try:
        linkMensagemFormatada = f'https://web.whatsapp.com/send?phone={telefone}&text="{quote(mensagem)}"'
        driver.get(linkMensagemFormatada)
        sleep(15)
        campoMensagem = driver.find_element('xpath',
                                            '//*[@id="main"]/footer/div[1]/div/span/div/div/div/div[3]/div[1]/p')
        time.sleep(0.5)
        campoMensagem.click()
        campoMensagem.send_keys(Keys.ENTER)
        sleep(3)





        

    except:
        print(f'Não foi possivel mandar a mensagem para {nome}')
        with open('erros.csv', 'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome},{telefone}')