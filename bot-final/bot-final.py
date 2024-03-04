import re
import random
import time
import pyautogui as pg

b = 0

def extraer_nombres(ruta_archivo):
  nombres = []
  with open(ruta_archivo, 'r') as archivo:
    for linea in archivo:
      coincidencia = re.search(r'\"(.*?)\"', linea)
      if coincidencia:
        nombre = coincidencia.group(1)
        nombres.append(nombre)
  return nombres

ruta_archivo = "C:\\Users\\Admin\\Desktop\\listavictimas.txt"
nombres_extraidos = extraer_nombres(ruta_archivo)

time.sleep(9)

for i in range(130):
    a = nombres_extraidos[b]
    pg.click()
    pg.hotkey('ctrl', 'a')
    pg.press('backspace')
    pg.hotkey('altright', "q")
    pg.write(a)
    time.sleep(2)
    pg.press("enter")
    pg.press("enter")
    pg.press("enter")
    pg.press("enter")
    pg.press("enter")
    b += 1
    time.sleep(65)
    


