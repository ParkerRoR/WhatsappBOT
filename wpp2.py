'''import re

nome = input('Qual o seu nome completo? ')

if re.search('\\benzo\\b', nome, re.IGNORECASE):
    print("A string tem o nome Enzo")
else:
    print("A string não tem o nome Enzo")'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
nome_contato = []
blacklist = []
msg = ''

with open("wpp_msg.txt", "r") as j:
    msg = j.read()

with open("wpp_alunos.txt", "r") as f:
    nome_contato = f.readlines() # readlines() returns a list of items, each item is a line in your file

with open("wpp_blacklist.txt", "r") as b:
    blacklist = b.readlines()



tam = len(nome_contato)
for i in range(tam):
    nome_contato[i] = nome_contato[i].rstrip()
os.system('cls')
print('A mensagem a ser enviada será:')
print('')
print(msg)
time.sleep(3)
os.system('cls')

mensagem = msg
class Wpp:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://web.whatsapp.com/'
        self.field_search_ctt = '/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/input'
        self.field_msg = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]'
        self.matched_down = 'matched-text' # class
        self.btn_send_msg = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button'
        self.label_ctt_right_window = '/html/body/div[1]/div/div/div[4]/div/header/div[2]/div/div/span'
    def navigate(self):
        self.driver.get(self.url)

    def set_msg(self, mensagem):
        self.mensagem = mensagem
        self.driver.find_element(By.XPATH, self.field_msg).send_keys(self.mensagem)
    
    def click_send_msg(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_send_msg).click()
    
    def set_search_ctt(self, nome_contato):
        time.sleep(1)
        self.nome_contato = nome_contato
        self.driver.find_element(By.XPATH, self.field_search_ctt).clear()
        self.driver.find_element(By.XPATH, self.field_search_ctt).send_keys(self.nome_contato)
    
    def click_ctt(self):
        time.sleep(1)
        self.contato = self.driver.find_element_by_xpath('//span[@title="{}"]'.format(self.nome_contato))
        self.check_ctt_isTrue()

    def check_ctt_isTrue(self):
        if (self.nome_contato == []):
            print('{} não foi encontrado'.format(self.nome_contato))
        else:
            self.contato.click()
def start():
    ff = webdriver.Firefox()
    wpp = Wpp(ff)
    wpp.navigate()
    os.system('pause')
    for i in range(len(nome_contato)):
        try:            

                
                for z in range(len(blacklist)):
                    if (nome_contato[i].lower() == blacklist[z].lower()):
                        blacklist_true = True
                        print('O contato: {} está na blacklist'.format(blacklist[z].capitalize()))
                    else:
                        blacklist_true = False

                if (blacklist_true == True):
                    blacklist_true = False
                else:
                    wpp.set_search_ctt(nome_contato[i])
                    wpp.click_ctt()
                    wpp.set_msg('Boa tarde {}, {}'.format(nome_contato[i].lower().capitalize(), mensagem))
                    wpp.click_send_msg()
        except:
            print('O contato {} NÃO foi encontrado, por favor cadastre-o!'.format(nome_contato[i]))
start()
