import pyautogui
from random import *
import time
import keyboard

left = 'left'
right = 'right'


def sleep(timer):
    time.sleep(uniform(timer - (timer / 10), timer + (timer / 10)))
    return


def bank():
    click(1336, 664, right)
    sleep(0.8)
    click(1336, 706, left)
    sleep(0.8)
    click(1316, 1011, left)
    #exit()


def grab_herb():
    #grab herb
    click(964, 316, right)
    time.sleep(0.8)
    click(927, 424, left)
    time.sleep(0.8)

    #close bank
    click(1361, 250, left)
    return


def click(x, y, button):
    pyautogui.moveTo(x - 3, y + 3, duration=uniform(0.25, 0.35))
    pyautogui.click(button=button)
    return


def click_clean(x, y, button):
    pyautogui.moveTo(x - 3, y + 3, duration=uniform(0.11, 0.16))
    pyautogui.click(button=button)
    return


def clean():
    global count
    x = 2342
    y = 1118
    for columns in range(7):
        for rows in range(4):
            click_clean(x, y, left)
            sleep(1.05)
            count -= 1
            if count == 0:
                print('All Done')
                exit()
            x += 40
        x -= 40 * 4
        y += 36
    return



if __name__ == '__main__':
    global count
    count = input('Enter herb count: ')
    count = int(count)
    done = False
    while not keyboard.is_pressed('q'):
        #if keyboard.is_pressed('q'):
            #print('All Finished')
            #done = True
        #else:
        bank()
        grab_herb()
        clean()
    exit()