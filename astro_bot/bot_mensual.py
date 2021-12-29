from selenium import webdriver
from seleniumrequests import Firefox
import time


browser = webdriver.Firefox()


def remove_prefix(s, prefix):
    if s.startswith(prefix):
        s = s[len(prefix):]
    return s

    # Aries
    browser.get('https://www.hola.com/horoscopo/aries/mensual/mayo')
    borra = browser.find_element_by_class_name('title').text
    elem = browser.find_element_by_id('resultados').text
    texto_borrado = remove_prefix(elem, borra)

    #test para local
    posteo = Firefox()
    response = posteo.request('POST', '', data={"Signo": "Aries"})


    obj = Signos.objects.get(nombre="Aries")
    pred = Prediccion_mensual(signo=obj, prediccion_mes=texto_borrado)
    # # Tauro
    # browser.get('https://www.hola.com/horoscopo/tauro/mensual/mayo')
    # borra = browser.find_element_by_class_name('title').text
    # elem = browser.find_element_by_id('resultados').text
    # texto_borrado = remove_prefix(elem, borra)
    # obj = Signos.objects.get(nombre="Tauro")
    # pred = Prediccion_mensual(signo=obj, prediccion_mes=texto_borrado)
    # pred.save()
    # # geminis
    # browser.get('https://www.hola.com/horoscopo/geminis/mensual/mayo')
    # borra = browser.find_element_by_class_name('title').text
    # elem = browser.find_element_by_id('resultados').text
    # texto_borrado = remove_prefix(elem, borra)
    # obj = Signos.objects.get(nombre="Géminis")
    # pred = Prediccion_mensual(signo=obj, prediccion_mes=texto_borrado)
    # pred.save()
    # # cancer
    # browser.get('https://www.hola.com/horoscopo/cancer/mensual/mayo')
    # borra = browser.find_element_by_class_name('title').text
    # elem = browser.find_element_by_id('resultados').text
    # texto_borrado = remove_prefix(elem, borra)
    # obj = Signos.objects.get(nombre="Cáncer")
    # pred = Prediccion_mensual(signo=obj, prediccion_mes=texto_borrado)
    # pred.save()
    # # leo
    # browser.get('https://www.hola.com/horoscopo/leo/mensual/mayo')
    # borra = browser.find_element_by_class_name('title').text
    # elem = browser.find_element_by_id('resultados').text
    # texto_borrado = remove_prefix(elem, borra)
    # obj = Signos.objects.get(nombre="Leo")
    # pred = Prediccion_mensual(signo=obj, prediccion_mes=texto_borrado)
    # pred.save()
    # # virgo
    # browser.get('https://www.hola.com/horoscopo/virgo/mensual/mayo')
    # borra = browser.find_element_by_class_name('title').text
    # elem = browser.find_element_by_id('resultados').text
    # texto_borrado = remove_prefix(elem, borra)
    # obj = Signos.objects.get(nombre="Virgo")
    # pred = Prediccion_mensual(signo=obj, prediccion_mes=texto_borrado)
    # pred.save()
    # # libra
    # browser.get('https://www.hola.com/horoscopo/libra/mensual/mayo')
    # borra = browser.find_element_by_class_name('title').text
    # elem = browser.find_element_by_id('resultados').text
    # texto_borrado = remove_prefix(elem, borra)
    # obj = Signos.objects.get(nombre="Libra")
    # pred = Prediccion_mensual(signo=obj, prediccion_mes=texto_borrado)
    # pred.save()
    # # escorpio
    # browser.get('https://www.hola.com/horoscopo/escorpio/mensual/mayo')
    # borra = browser.find_element_by_class_name('title').text
    # elem = browser.find_element_by_id('resultados').text
    # texto_borrado = remove_prefix(elem, borra)
    # obj = Signos.objects.get(nombre="Escorpio")
    # pred = Prediccion_mensual(signo=obj, prediccion_mes=texto_borrado)
    # pred.save()
    # # sagitario
    # browser.get('https://www.hola.com/horoscopo/sagitario/mensual/mayo')
    # borra = browser.find_element_by_class_name('title').text
    # elem = browser.find_element_by_id('resultados').text
    # texto_borrado = remove_prefix(elem, borra)
    # obj = Signos.objects.get(nombre="Sagitario")
    # pred = Prediccion_mensual(signo=obj, prediccion_mes=texto_borrado)
    # pred.save()
    # # capricornio
    # browser.get('https://www.hola.com/horoscopo/capricornio/mensual/mayo')
    # borra = browser.find_element_by_class_name('title').text
    # elem = browser.find_element_by_id('resultados').text
    # texto_borrado = remove_prefix(elem, borra)
    # obj = Signos.objects.get(nombre="Capricornio")
    # pred = Prediccion_mensual(signo=obj, prediccion_mes=texto_borrado)
    # pred.save()
    # # acuario
    # browser.get('https://www.hola.com/horoscopo/acuario/mensual/mayo')
    # borra = browser.find_element_by_class_name('title').text
    # elem = browser.find_element_by_id('resultados').text
    # texto_borrado = remove_prefix(elem, borra)
    # obj = Signos.objects.get(nombre="Acuario")
    # pred = Prediccion_mensual(signo=obj, prediccion_mes=texto_borrado)
    # pred.save()
    # # piscis
    # browser.get('https://www.hola.com/horoscopo/piscis/mensual/mayo')
    # borra = browser.find_element_by_class_name('title').text
    # elem = browser.find_element_by_id('resultados').text
    # texto_borrado = remove_prefix(elem, borra)
    # obj = Signos.objects.get(nombre="Piscis")
    # pred = Prediccion_mensual(signo=obj, prediccion_mes=texto_borrado)
    # pred.save()
    # time.sleep(5)
    # browser.quit()

    # FIN BOT
    print('pronto')
