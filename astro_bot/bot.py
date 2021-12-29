from selenium import webdriver
import time

#Falta el texto.save() para guardar en bd
#    obj = Signos.objects.get(nombre="Aries")
#    pred = Prediccion_mensual(signo=obj, prediccion_mes="sos puto")
#    pred.save()
# Esto es para llamar y guardar en bd
browser = webdriver.Firefox()


def remove_prefix(s, prefix):
    if s.startswith(prefix):
        s = s[len(prefix):]
    return s


# Aries
browser.get('https://www.hola.com/horoscopo/aries/')
borra = browser.find_element_by_class_name('title').text
elem = browser.find_element_by_id('resultados').text
texto_borrado = remove_prefix(elem, borra)
print(texto_borrado)

# Tauro
# browser.get('https://www.hola.com/horoscopo/tauro/')
borra = browser.find_element_by_class_name('title').text
elem = browser.find_element_by_id('resultados').text
texto_borrado = remove_prefix(elem, borra)
print(texto_borrado)

# geminis
browser.get('https://www.hola.com/horoscopo/geminis/')
borra = browser.find_element_by_class_name('title').text
elem = browser.find_element_by_id('resultados').text
texto_borrado = remove_prefix(elem, borra)
print(texto_borrado)

# cancer
browser.get('https://www.hola.com/horoscopo/cancer/')
borra = browser.find_element_by_class_name('title').text
elem = browser.find_element_by_id('resultados').text
texto_borrado = remove_prefix(elem, borra)
print(texto_borrado)

# leo
browser.get('https://www.hola.com/horoscopo/leo/')
borra = browser.find_element_by_class_name('title').text
elem = browser.find_element_by_id('resultados').text
texto_borrado = remove_prefix(elem, borra)
print(texto_borrado)

# virgo
browser.get('https://www.hola.com/horoscopo/virgo/')
borra = browser.find_element_by_class_name('title').text
elem = browser.find_element_by_id('resultados').text
texto_borrado = remove_prefix(elem, borra)
print(texto_borrado)

# libra
browser.get('https://www.hola.com/horoscopo/libra/')
borra = browser.find_element_by_class_name('title').text
elem = browser.find_element_by_id('resultados').text
texto_borrado = remove_prefix(elem, borra)
print(texto_borrado)

# escorpio
browser.get('https://www.hola.com/horoscopo/escorpio/')
borra = browser.find_element_by_class_name('title').text
elem = browser.find_element_by_id('resultados').text
texto_borrado = remove_prefix(elem, borra)
print(texto_borrado)

# sagitario
browser.get('https://www.hola.com/horoscopo/sagitario/')
borra = browser.find_element_by_class_name('title').text
elem = browser.find_element_by_id('resultados').text
texto_borrado = remove_prefix(elem, borra)
print(texto_borrado)

# capricornio
browser.get('https://www.hola.com/horoscopo/capricornio/')
borra = browser.find_element_by_class_name('title').text
elem = browser.find_element_by_id('resultados').text
texto_borrado = remove_prefix(elem, borra)
print(texto_borrado)

# acuario
browser.get('https://www.hola.com/horoscopo/acuario/')
borra = browser.find_element_by_class_name('title').text
elem = browser.find_element_by_id('resultados').text
texto_borrado = remove_prefix(elem, borra)
print(texto_borrado)

# piscis
browser.get('https://www.hola.com/horoscopo/piscis/')
borra = browser.find_element_by_class_name('title').text
elem = browser.find_element_by_id('resultados').text
texto_borrado = remove_prefix(elem, borra)
print(texto_borrado)


time.sleep(5)
browser.quit()
