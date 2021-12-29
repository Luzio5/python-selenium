from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
import datos
import time


def start_sesion(mail, password):
    element_mail = browser.find_element_by_xpath("//input[@name='email']")
    element_mail.send_keys(mail)
    element_passwd = browser.find_element_by_xpath("//input[@name='password']")
    element_passwd.send_keys(password)
    browser.find_element_by_class_name("btn").click()
    return


def wait(sec):
    time.sleep(sec)
    return


def activity_entry(id):
    browser.get('https://agenda.sinergialife.uy/reservaactividad?id=' + str(id))
    wait(2)
    delay = 2  # seconds
    WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.CLASS_NAME, "activity_tomorrow_date")))
    return


def time_search(horario):
    WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.CLASS_NAME, "activity_btn_back")))
    wait(2)
    elements = browser.find_elements_by_xpath("//p[contains(@class, 'activity_time')]")
    pos = -1
    for i in range(elements.__len__()):
        if elements[i].text == horario:
            pos = i
    if pos == -1:
        print("no encontro horario")
        exit(0)
    print(pos)
    return pos


def reservar(pos):
    selector = "//div[contains(@class, 'activity_card')][" + str(pos) + "]//a[contains(@class, 'btn-card-reservar')]"
    browser.find_element_by_xpath(selector).click()
    wait(2)
    browser.find_element_by_xpath("//button[contains(@class, 'btn_modal_confirmar')]").click()
    return

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options, executable_path='/home/luciano/sinergia_auto_clase/geckodriver')
browser.get('https://agenda.sinergialife.uy/signin')

delay = 2 # seconds
elem = WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='email']")))

# iniciar_sesion
start_sesion(datos.mail, datos.passwd)


# esperar unos segundos
wait(2)


# chequea si logró entrar bien. sino reintentar FALTA


# asumiendo que entramos vamos a la actividad que nos interesa
activity_entry(datos.activity)


# Nos movemos al día siguiente para agendarnos ###Falta chequear si realmente funciona para el lunes
element = browser.find_element_by_class_name("activity_tomorrow_date").click()


# buscamos el horario
pos = time_search(datos.horario)


#nos agendamos
reservar(pos)
print ("Listorta!!")
