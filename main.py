from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

student_name = []
msg = ''

with open("msg.txt", "r") as j:
    msg = j.read()

with open("alunos.txt", "r") as f:
    student_name = f.readlines() # readlines() returns a list of items, each item is a line in your file



tam = len(student_name)
for i in range(tam):
    student_name[i] = student_name[i].rstrip()

print(msg)


class Wpp:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://web.whatsapp.com/'
        self.match_text = 'matched-text' #class
        self.ctt_field = '/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/input'
        self.input_msg = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]'
    def navigate(self):
        self.driver.get(self.url)
        print('Insira o QR Code')
        print('')
        os.system('PAUSE')
    
    def search_ctt(self, std_nome):
        self.std_nome = std_nome
        self.driver.find_element(By.XPATH, self.ctt_field).clear()
        self.driver.find_element(By.XPATH, self.ctt_field).send_keys(self.std_nome)
        time.sleep(5)     
    
    def check_ctt_name(self, std_nome):
        self.std_nome = std_nome
        self.match = self.driver.find_element_by_class_name(self.match_text)
        self.match_txt_upper = self.match.text
        time.sleep(1)

        if (self.std_nome.upper() == self.match_txt_upper.upper()):
            self.enter_key_ctt()
            print('Uma mensagem foi enviada para {}!'.format(self.std_nome))
        else:
            print('Nome procurado nao existe!')
        

    def write_message(self, msg):
        self.msg = msg
        self.driver.find_element(By.XPATH, self.input_msg).send_keys(self.msg)

        self.enter_key_message()

        
        
    def enter_key_ctt(self):
        self.driver.find_element(By.XPATH, self.ctt_field).send_keys(Keys.ENTER)
        time.sleep(1)

    def enter_key_message(self):
        self.driver.find_element(By.XPATH, self.input_msg).send_keys(Keys.ENTER)
        time.sleep(1)   
ff = webdriver.Firefox()
wpp = Wpp(ff)
wpp.navigate()



for i in range(len(student_name)):

    try:
        wpp.search_ctt(student_name[i])
        wpp.check_ctt_name(student_name[i])
        wpp.write_message('{} {}'.format(student_name[i], msg))
    except:
        print('O contato {} não consta na sua lista'.format(student_name[i]))
    
