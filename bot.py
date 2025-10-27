import pyautogui
import time

mensajes = [
    "potato.start uwunt",
    "uwu",
    "potato",
    "https://tenor.com/view/mwa-gif-20960109",
    "uwu",
    "https://tenor.com/view/mwa-gif-20960109",
    "potato",
    "https://tenor.com/view/mwa-gif-20960109",
    "uwu",
    "https://tenor.com/view/mwa-gif-20960109",
    "AGAIN!"
]

time.sleep(1)  # Time to select the bar

i = 0
while True:
    pyautogui.write(mensajes[i])
    pyautogui.press('enter')
    i = (i + 1) % len(mensajes)  # Reset the messange :D
    time.sleep(30)
