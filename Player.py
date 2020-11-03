import cv2
from PIL import ImageGrab
import random
import time
import pyautogui
import numpy as np

screen_x = 2560
screen_y = 1440

player_x = screen_x / 2
player_y = screen_y / 2

def image_match(r, pic, match_type, accuracy):
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
    # print (loc)
    if len(loc[0]) > 0:
        # print("Registered something")
        for pt in zip(*loc[::-1]):
            cv2.rectangle(gray_screen, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
        cv2.namedWindow('detected')
        cv2.moveWindow('detected', 0, 0)
        cv2.imshow('detected', gray_screen)
        cv2.waitKey(5000)
        #print("Iron detected")
        #cv2.imwrite('detectedGreen.png', gray_screen)
        # exit()
        # pyautogui.moveTo(((pt[0] + w) / 2), ((pt[1] + h) / 2), duration=0.20)
        # pyautogui.click()
        # check_done(template)
        # exit()
        return True
    else:
        return False
    # else:
    # print("No match detected")

    # return True
    # else:
    # return False

def find_bankers():
    low = 60
    high = 75
    lower_color_bounds = (low, low, low)
    upper_color_bounds = (high, high, high)
    screen = ImageGrab.grab()
    image = np.array(screen)
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mask = cv2.inRange(image, lower_color_bounds, upper_color_bounds)
    mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    image = image & mask_rgb
    cv2.imshow('screen', image)
    cv2.waitKey(5000)

if __name__ == '__main__':
    #pyautogui.moveTo(player_x, player_y, duration=0.22)
    for x in range (3):
        print(2 - x)
        time.sleep(1)
    #find_bankers()
    if image_match((np.array(ImageGrab.grab())), cv2.imread('LeftBanker1.PNG'), 'gray', 0.50) is True:
        print('Found Banker')