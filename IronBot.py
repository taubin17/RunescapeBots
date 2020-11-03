import cv2
import pyautogui
import numpy as np
import time
from random import *
from PIL import ImageGrab

def on_start():
    pyautogui.moveTo(2374, 39, duration=0.33)
    pyautogui.click()
    pyautogui.keyDown('up')
    time.sleep(0.4)
    pyautogui.keyUp('up')
    pyautogui.scroll(-100)
def drop_iron():
    x = 2332
    y = 1118
    pyautogui.keyDown('shift')

    for columns in range(7):
        for rows in range(4):
            pyautogui.moveTo(randint(x - 1, x + 4), randint(y - 3, y + 3), duration=uniform(0.16, 0.22))
            pyautogui.click()
            x += 40
        x -= 40 * 4
        y += 36
    pyautogui.keyUp('shift')
    return
def new_level(img):
    if image_match(img, cv2.imread('NewLevel.PNG'), "gray", 0.90):
        pyautogui.click()
        return
def is_bag_full():
    last_slot = screen = ImageGrab.grab(bbox=(2310, 1100, 2500, 1365))
    last_slot = np.array(last_slot)
    #cv2.imshow('location', last_slot)
    #time.sleep(1)
    pic = cv2.imread('RLITEbag.PNG')
    backpack_full = not (image_match(last_slot, pic, "gray", .80))
    if backpack_full == True:
        print('Backpack is full!')
        drop_iron()
        return
    else:
        return
def image_match(r, pic, match_type, accuracy):
    screen = r
    gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    template = pic
    gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = gray_template.shape[::-1]

    if match_type == "gray" or match_type == "grey":
        res = cv2.matchTemplate(gray_screen, gray_template, cv2.TM_CCOEFF_NORMED)
        #cv2.imshow('screen2', gray_screen)
        #cv2.imshow('screen3', gray_template)
    else:
        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        #cv2.imshow('screen2', screen)
        #cv2.imshow('screen3', template)

    threshold = accuracy
    loc = np.where(res >= threshold)
    #cv2.imshow('screen2', screen)
    #cv2.imshow('screen3', template)
    #print (loc)
    if len(loc[0]) > 0:
        #print("Registered something")
        #for pt in zip(*loc[::-1]):
            #cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
        #cv2.namedWindow('detected')
        #cv2.moveWindow('detected', 0, 0)
        #cv2.imshow('detected', screen)
        #print("Iron detected")
        #cv2.imwrite('detectedIron.png', screen)
        #exit()
        return True
    else:
        return False
    #else:
        #print("No match detected")

        #return True
    #else:
        #return False
def check_rocks(direction):
    done = False
    while not done:
        whole_screen = ImageGrab.grab()
        print('Not Done')
        picture = 'IronRock' + direction + '.png'
        #print(picture)
        if image_match(np.array(whole_screen), cv2.imread(picture), "gray", 0.80) is False:
            done = True
    print('Done')
    return
def mine_rocks(x, y):
    wait = uniform(0.08, 0.19)
    pyautogui.moveTo(randint(x-3, x+3), randint(y-3, y+10), duration=wait)
    pyautogui.click()
    #time.sleep(.22)

if __name__ == '__main__':
    x = 1336
    y = 700
    y_change = 30
    we_are_stuck = 0
    need_to_click = True
    global screen
    test = True
    down_breakout = False
    left_breakout = False
    right_breakout = False
    #on_start()
    #time.sleep(100)
    while test == True:
        whole_screen = ImageGrab.grab()
        is_bag_full()
        new_level(np.array(whole_screen))
        #time.sleep(1)
        if image_match(np.array(whole_screen), cv2.imread('IronRockDown.png'), "gray", 0.80):
            is_bag_full()
            mine_rocks(1260, 818)
            #is_bag_full()
            print("We found Iron!")
            check_rocks("Down")
        if image_match(np.array(whole_screen), cv2.imread('IronRockDown.png'), "gray", 0.80):
            is_bag_full()
            mine_rocks(1140, 717)
            #is_bag_full()
            print("We found Iron!")
            check_rocks("Left")
        if image_match(np.array(whole_screen), cv2.imread('IronRockDown.png'), "gray", 0.80):
            is_bag_full()
            mine_rocks(1350, 727)
            #is_bag_full()
            print("We found Iron!")
            check_rocks("Right")
    #if image_match(np.array(whole_screen), cv2.imread('IronRockDown.png'), "gray", 0.80):
        #    mine_rocks(1260, 818)
        #    print("We found Iron!")
        #    while down_breakout is False:
        #        if image_match(np.array(whole_screen), cv2.imread('IronRockDown.png'), "", 0.99) is False:
        #            down_breakout = True
        #        print("In wait loop")
        #        if is_bag_full() == True:
        #            drop_iron()
        #            break
        #        whole_screen = ImageGrab.grab()
                #pass
        #if image_match(np.array(whole_screen), cv2.imread('IronRockLeft.png'), "gray", 0.80):
        #    mine_rocks(1140, 717)
        #    print("We found Iron!")
        #    while left_breakout is False:
        #        if image_match(np.array(whole_screen), cv2.imread('IronRockLeft.png'), "", 0.99) is False:
        #            left_breakout = True
        #        print("In wait loop")
        #        if is_bag_full() == True:
        #            drop_iron()
        #            break
        #        whole_screen = ImageGrab.grab()
                #pass

        #if image_match(np.array(whole_screen), cv2.imread('IronRockRight.png'), "gray", 0.80):
        #    mine_rocks(1350, 727)
        #    print("We found Iron!")
        #    while right_breakout is False:
        #        if image_match(np.array(whole_screen), cv2.imread('IronRockRight.png'), "", 0.99) is False:
        #            right_breakout = True
        #        print("In wait loop")
        #        if is_bag_full() is True:
        #            drop_iron()
        #            break
        #        whole_screen = ImageGrab.grab()
                #pass
        #down_breakout = False
        #left_breakout = False
        #right_breakout = False
