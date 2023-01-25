from selenium import webdriver
import time

class CookieClicar:
    def __init__(self):
        self.SITE_LINK = 'https://orteil.dashnet.org/cookieclicker/'     #--> Atributo do site
        self.SITE_MAP = {     #--> XPATH DOS BOTOES
            'buttons':{      #--> Botao do Cookie
                'cookie': {
                    'xpath': '/html/body/div[2]/div[2]/div[15]/div[8]/button'
                },
                'upgrade': {   #--> Botao Upgrades
                    'xpath': '/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div[$$NUMBER$$]'
                }
            }
        }     #--> COORDENADAS DOS OBJETOS
        
        self.driver = webdriver.Chrome(executable_path='C\\WebDrivers\\chromedriver.exe') # --> Conexão com o chromedriver
        self.driver.maximize_window()

    def abrir_site(self):
        time.sleep(4)
        self.driver.get(self.SITE_LINK) #--> PARA ABRIR O SITE
        time.sleep(3)
        self.element = self.driver.find_element('xpath', '//*[@id="langSelect-PT-BR"]').click()
        time.sleep(20)

    def clicar_cookie(self):
        self.driver.find_element('xpath' , self.SITE_MAP['buttons']['cookie']['xpath']).click() #--> CHAMANDO A LOCALIZAÇÂO DO BOTAO COLOCADO NO INICIO PARA CLICAR

    def pega_melhor_upgrade(self):
        encontrei = False
        elemento_atual = 2    #--> Primeiro upgrade inicia com 2

        while not encontrei:
            objeto = self.SITE_MAP['buttons']['upgrade']['xpath'].replace('$$NUMBER$$', str(elemento_atual))
            classes_objeto = self.driver.find_element('xpath' , objeto).get_attribute('class')

            if not 'enable' in classes_objeto:
                encontrei = True
            else:
                elemento_atual += 1
        return elemento_atual - 1

    def compra_upgrade(self):
        objeto = self.SITE_MAP['buttons']['upgrade']['xpath'].replace('$$NUMBER$$', str(self.pega_melhor_upgrade()))
        self.driver.find_element('xpath' , objeto).click()

cookie = CookieClicar()
cookie.abrir_site()

i = 0

while True:
    if i % 500 == 0 and i != 0:
        time.sleep(1)
        cookie.compra_upgrade()
        time.sleep(1)
    cookie.clicar_cookie()
    i += 1