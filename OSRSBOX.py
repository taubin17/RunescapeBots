from osrsbox import items_api
import pyautogui
import cv2
import time
import numpy as np
from PIL import ImageGrab
from random import *
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

right = 'right'
left = 'left'

GE_attendant = cv2.imread('GEleft.PNG')


def image_match(r, pic, match_type, accuracy):
    center_matches = []
    screen = r
    gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    template = pic
    gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = gray_template.shape[::-1]

    if match_type == "gray" or match_type == "grey":
        res = cv2.matchTemplate(gray_screen, gray_template, cv2.TM_CCOEFF_NORMED)
        w, h = gray_template.shape[::-1]
        # cv2.imshow('screen2', gray_screen)
        # cv2.imshow('screen3', gray_template)
    else:
        # w, h = template.shape[::-1]
        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        # cv2.imshow('screen2', screen)
        # cv2.imshow('screen3', template)

    threshold = accuracy
    loc = np.where(res >= threshold)
    # cv2.imshow('screen2', screen)
    # cv2.imshow('screen3', template)
    #print(loc)
    if len(loc[0]) > 0:
        # print("Registered something")
        for pt in zip(*loc[::-1]):
            #cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
            center_point = ((pt[0] + (w / 2)), (pt[1] + (h / 2)))
            center_matches.append(center_point)
        center_matches = list(set([i for i in center_matches]))
        x = 0
        for each in center_matches:
            x += 1
            #print(each, x)
        #print('\n\n')
        #cv2.namedWindow('detected')
        #cv2.moveWindow('detected', 0, 0)
        #cv2.imshow('detected', screen)
        #cv2.waitKey(5000)
        #cv2.destroyAllWindows()
        return center_matches
    else:
        return 0
    # else:
    # print("No match detected")

    # return True
    # else:
    # return False



def click(x, y, button):
    pyautogui.moveTo(x, y, duration=uniform(0.2, 0.25))
    pyautogui.click(button=button)

def find_price(screen):

    #Look for GE officer
    GE_officer = image_match(screen, GE_attendant, '', 0.70)
    if GE_officer != 0:
        print('Found officer')
        click(GE_officer[0][0], GE_officer[0][1], right)
        time.sleep(0.5)
    #Talk to GE officer
    #click(1394, 737, right)
    #time.sleep(0.5)

    #Click exchange
    #click(1329, 779, left)
    #time.sleep(0.5)




if __name__ == '__main__':
    #all_db_items = items_api.load()
    #for item in all_db_items:
        #print(item.id, item.name, item.cost)
    screen = ImageGrab.grab()
    screen = np.array(screen)
    find_price(screen)
    #if find_price != 0:
       # click()