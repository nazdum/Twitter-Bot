from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import tweepy as tw

'''
Configuraciones de selenium
'''
options = Options()
options.binary_location = r'/lib/firefox-developer-edition/firefox'
driver = webdriver.Firefox(executable_path=r'/home/camilo/Documentos/sovietK/geckodriver', options=options)
'''
Fin de las configuraciones de selenium
'''


def twLogin():
    driver.get("https://twitter.com/login")

    time.sleep(4) #tiempo para que cargue twitter

    campoUsuario = driver.find_element(By.NAME,value="text")
    campoUsuario.send_keys("@verdaderopresor")

    time.sleep(1)
    nextBtn = driver.find_element(By.XPATH,value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]')
    nextBtn.click()

    time.sleep(3)
    campoContraseña = driver.find_element(By.NAME,value="password")
    campoContraseña.send_keys("#Ragnaros321")

    time.sleep(2)

    loginBtn = driver.find_element(By.XPATH,value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]")
    loginBtn.click()

def nuevoTwit(mensaje):
    twLogin()
    time.sleep(6)

    cajaTexto = driver.find_element(By.XPATH,value="/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div")
    cajaTexto.send_keys(mensaje)

    enviarBtn = driver.find_element(By.XPATH,value="/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div")
    enviarBtn.click()

def irAlPerfil(usuario):
    twLogin()
    time.sleep(3)

    barraBusqueda = driver.find_element(By.XPATH,value="/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input")
    barraBusqueda.send_keys(usuario)
    barraBusqueda.send_keys(Keys.ENTER)

    time.sleep(3)
    personas = driver.find_element(By.XPATH,value="/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/nav/div/div[2]/div/div[3]/a")
    personas.click()

    time.sleep(1)
    perfil = driver.find_element(By.XPATH,value="/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div/div/div[2]/div/div[1]/a/div/div[1]/div[1]/span/span")
    perfil.click()

def nombrePerfil(usuario):
    irAlPerfil(usuario)
    time.sleep(4)
    nombre = driver.find_element(By.XPATH,value="/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/span[1]/span")
    print(nombre.get_attribute('innerHTML'))

