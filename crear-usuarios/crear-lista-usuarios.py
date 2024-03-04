import pyautogui as pg
import time

time.sleep(10)

for i in range(150):
    pg.write(f'lista.push(obj[{i}].innerText);')
    pg.press('enter')
    
    
