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
        w, h = gray_template.shape[::-1]
        #cv2.imshow('screen2', gray_screen)
        #cv2.imshow('screen3', gray_template)
    else:
        w, h = template.shape[::-1]
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
            cv2.rectangle(gray_screen, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
        #cv2.namedWindow('detected')
        #cv2.moveWindow('detected', 0, 0)
        #cv2.imshow('detected', screen)
        #print("Iron detected")
        cv2.imwrite('detectedGreen.png', gray_screen)
        #exit()
        pyautogui.moveTo(((pt[0] + w) / 2), ((pt[1] + h) / 2), duration=0.20)
        pyautogui.click()
        #check_done(template)
        #exit()
        return True
    else:
        return False
    #else:
        #print("No match detected")

        #return True
    #else:
        #return False
def check_done(image):
    done = False
    while not done:
        whole_screen = ImageGrab.grab()
        print('Not Done')
        #print(picture)
        if image_match(np.array(whole_screen), image, "gray", 0.80) is False:
            done = True
    print('Done')
    return

if __name__ == '__main__':
    step = 6
    global screen
    test = True
    while test == True:
        whole_screen = ImageGrab.grab()
        np_screen = np.array(whole_screen)
        #is_bag_full()
        #new_level(np.array(whole_screen))
        #time.sleep(1)
        if step == 1:
            print('Searching')
            if image_match(np_screen, cv2.imread('StepOne.PNG'), "gray", 0.80):
                print("Found it!")
                step = 2
        if step == 2:
            if image_match(np_screen, cv2.imread('StepTwo.PNG'), "gray", 0.80):
                print("Step 2 done")
                step = 3
        if step == 3:
            if image_match(np_screen, cv2.imread('StepThree.PNG'), "gray", 0.80):
                print("Step 3 done")
                step = 4
        if step == 4:
            print('Searching')
            if image_match(np_screen, cv2.imread('StepFour.PNG'), "gray", 0.80):
                print("Found it!")
                step = 5
        if step == 5:
            if image_match(np_screen, cv2.imread('StepFive.PNG'), "gray", 0.80):
                print("Step 5 done")
                step = 6
        if step == 6:
            if image_match(np_screen, cv2.imread('StepSix.PNG'), "gray", 0.80):
                print("Step 6 done")
                step = 7
        if step == 7:
            if image_match(np_screen, cv2.imread('StepSeven.PNG'), "gray", 0.80):
                print("Step 7 done")
                step = 8
        if step == 8:
            if image_match(np_screen, cv2.imread('StepEight.PNG'), "gray", 0.80):
                print("Step 8 done")
                step = 1
