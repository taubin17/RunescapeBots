import pyautogui
import time
from random import *


def click(x, y):
    pyautogui.moveTo(randint(x - 2, x + 2), randint(y - 2, y + 2), duration=uniform(0.15, 0.30))
    pyautogui.click()


def sleep(delay):
    time.sleep(uniform(delay - (delay / 10), delay + (delay / 10)))
    return


def run_away():
    click(1280, 50)
    sleep(0.4)
    click(1280, 50)
    sleep(0.4)

def run_back():
    click(1280, 1060)
    sleep(0.4)
    click(1280, 1060)
    sleep(0.4)

if __name__ == '__main__':
    done = False
    while not done:
        time.sleep(600)
        run_away()
        sleep(0.7)
        run_back()
