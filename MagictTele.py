import pyautogui
from random import *
import time
from termcolor import colored, cprint

def click(x, y):
    pyautogui.moveTo(randint(x - 2, x + 2), randint(y - 2, y + 2), duration= uniform(0.15, 0.22))
    pyautogui.click()


if __name__ == '__main__':
    #training = True
    XP = 0
    for x in range(5955 * 5):
        pyautogui.moveTo(randint(2419, 2421), randint(1176, 1178), duration=0.05)
        pyautogui.click()
        if x % 5 == 0:
            XP += 55.5
            cprint('XP: ' + (str(XP)), 'cyan')
        time.sleep(uniform(0.24, 0.34))
    click(2515, 18)
    time.sleep(0.24)
    click(1771, 725)
