"""wpp.py -> envia mensagem pelo whatsapp."""


# -.- conding: utf-8 -.-

import time
from selenium import webdriver


class zap:
    """Envia mensagem para pessoas ou grupos."""

    def __init__(self):
        """Envia mensagem."""
        self.mensagem = "linux é vida!!"
        self.grupos_ou_pessoas = ['nome_1', 'nome_2']
        options = webdriver.ChromeOptions()  # drive do google chrome
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver', chrome_options=options
        )

    def enviar(self):
        """Função para enviar a mensagem."""
        self.driver.get('https://web.whatsapp.com')
        time.sleep(40)  # tempo de 40 para você logar com o qrcode
        # criando o laço para enviar a mensagem para sua lista de contato
        for grupo in self.grupos_ou_pessoas:
            usuario = self.driver.find_element_by_xpath(
                '//span[@title = "{}"]'.format(grupo)
            )
            usuario.click()
            msg_box = self.driver.find_element_by_class_name('_13mgZ')
            msg_box.send_keys(self.mensagem)
            botao = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']"
            )
            time.sleep(3)
            botao.click()


auto = zap()
auto.enviar()
