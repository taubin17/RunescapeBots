import cv2
import pyautogui
import numpy as np
import time
from random import *
from PIL import ImageGrab


fishing_cords = [(1316, 765), (1316, 723), (1310, 612),(2030, 516)]
backpack_slots = [(2462, 1127), (2503, 1121), (2374, 1164), (2420, 1162), (2458, 1162), (2501, 1163)]
def on_start():
    pyautogui.moveTo(2374, 39, duration=0.33)
    pyautogui.click()
    pyautogui.keyDown('up')
    time.sleep(0.4)
    pyautogui.keyUp('up')
    pyautogui.scroll(-100)
def drop_fish():
    x = randint(2371, 2377)
    y = randint(1161, 1167)
    pyautogui.keyDown('shift')
    pyautogui.moveTo(2462, 1127, duration=0.32)
    pyautogui.click()
    pyautogui.moveTo(2503, 1124, duration=0.34)
    pyautogui.click()

    for columns in range(6):
        for rows in range(4):
            pyautogui.moveTo(x, y, duration=0.34)
            pyautogui.click()
            x += 40
        x -= 40 * 4
        y += 36
    pyautogui.keyUp('shift')

def fish_cast(x, y):
    pyautogui.moveTo(x, y, duration= 0.47)
    pyautogui.click()
def check_fish_spots():
    for each in fishing_cords:
        pyautogui.moveTo(each, duration = 0.36)
        time.sleep(0.55)
        fish_avail = image_match(np.array(screen), cv2.imread('Fishing.png'), "", .60)
        time.sleep(5)
        if fish_avail == True:
            print("Fish Found")
            fish_cast(each[0], each[1])
            time.sleep(5)
            return
        else:
            print("No fish found")


def is_bag_full():
    #print("Checking Bag")
    at_trees = False
    #whole_bag = ImageGrab.grab(bbox=(810, 375, 988, 638))
    #whole_bag = np.array(whole_bag)
    #cv2.namedWindow('WholeBag')
    #cv2.moveWindow('WholeBag',300, 1000)
    #cv2.imshow('WholeBag', whole_bag)
    last_slot = ImageGrab.grab(bbox=(2480, 1312, 2530, 1365))
    last_slot = np.array(last_slot)
    #cv2.imshow('location', last_slot)
    #time.sleep(1)
    pic = cv2.imread('Backpack.png')
    backpack_full = not (image_match(last_slot, pic, "gray", .50))
    #print("Checking bag")
    if backpack_full == True:
        print('Backpack is full!')
        #run_to_bank()
        return True
    else:
        return False
    #cv2.imwrite('Backpack.png', last_slot)
    #cv2.namedWindow('backpack')
    #cv2.moveWindow('backpack', 1500, 1100)
    #cv2.imshow('backpack', last_slot)
    #return
def image_match(r, pic, match_type, accuracy):
    screen = r
    gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    template = pic
    gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = gray_template.shape[::-1]

    if match_type == "gray" or match_type == "grey":
        res = cv2.matchTemplate(gray_screen, gray_template, cv2.TM_CCOEFF_NORMED)
        cv2.imshow('screen2', gray_screen)
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
        for pt in zip(*loc[::-1]):
            cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
        #cv2.namedWindow('detected')
        #cv2.moveWindow('detected', 0, 0)
        #cv2.imshow('detected', screen)
        #cv2.imwrite('detected.png', screen)
        #exit()
        return True
    else:
        return False
    #else:
        #print("No match detected")

        #return True
    #else:
        #return False
def is_fish(img):
    temp = cv2.imread('Fishing.png')
    is_fish = image_match(img, temp, "", .40)
    return is_fish
    #if is_fish == True:
        #print("Fish found")
    #else:
        #print("No fish")
last_time = time.time()
if __name__ == '__main__':
    x = 1336
    y = 700
    y_change = 30
    we_are_stuck = 0
    need_to_click = True
    global screen
    test = True
    on_start()
    while test == True:
        #Where the AI looks at for determining tree readiness/at the bank
        screen = ImageGrab.grab(bbox=(1195, 25, 1284, 41))
        whole_screen = ImageGrab.grab()
        if image_match(np.array(whole_screen), cv2.imread('FishLogo.png'), "gray", 0.60):
            print ("We found a Fish!")
            #time.sleep(100)
        else:
            print("We didnt find fish")

        #screen = ImageGrab.grab(bbox=(1355, 710, 1405, 750))
        #last_slot = ImageGrab.grab(bbox=(2448, 1334, 2480, 1355))
        #Comment out screen and uncomment this screen to take/reset an image!
        #screen = ImageGrab.grab(bbox=(942, 580, 990, 624))

        x = randint(1310, 1348)
        img = np.array(screen)
        #chop_oak = cv2.imread('ChopOak.png')
        #print("We've successfully started running on windows!")
        #cv2.namedWindow('screen')
        #cv2.moveWindow('screen', 1600, 1100)
        cv2.imshow('Screen15', np.array(whole_screen))

        if (y + y_change) < 400 or (y + y_change) > 900:
            y_change *= -1
            if y_change > 0:
                y_change = (randint(8, 30))
        #y += y_change
        #y_change = 30
        #if is_bag_full() == True:
            #drop_fish()
        #time.sleep(1)
        #fish_avail = is_fish(img)
        #print (str(fish_avail))
        #time.sleep(3)
        fish_avail = False
        time.sleep(1)
        while fish_avail == True:
            screen = ImageGrab.grab(bbox=(0, 20, 155, 45))
            img = np.array(screen)
            #we_are_stuck += 1
            fish_avail = is_fish(img)
            #if fish_avail == False:
                #print("Attempting Breakout")
                #break
            if need_to_click == True:
                pyautogui.click()
                need_to_click = False
            if is_bag_full() == True:
                drop_fish()
            print((str(fish_avail)), we_are_stuck)
            y_change = 0
        #print("We broke out")
        #pyautogui.moveTo(x, y, duration=0.15)
        #check_fish_spots()
        need_to_click = True


        fps = (int(1 / (time.time() - last_time)))
        #time.sleep(1)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            #cv2.imwrite('Fishing.png', img)
            cv2.destroyAllWindows()
            break
        last_time = time.time()

