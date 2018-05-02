i = 0
import pyautogui as pg
import webbrowser
import time
webbrowser.open("https://www.amazon.com")
time.sleep(5)
while i < 5:
    pg.hotkey('tab')
    i += 1
time.sleep(2)
pg.typewrite("Vinyl records", 0.1)
time.sleep(1)
pg.hotkey('enter')
