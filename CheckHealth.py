import cv2
from PIL import ImageGrab
import numpy as np
import pytesseract
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

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
        #for pt in zip(*loc[::-1]):
            #cv2.rectangle(gray_screen, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
        # cv2.namedWindow('detected')
        # cv2.moveWindow('detected', 0, 0)
        # cv2.imshow('detected', screen)
        # print("Iron detected")
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


def check_writing():
    done = False
    while not done:
        time.sleep(1)
        tes_screen = ImageGrab.grab(bbox=(0, 20, 200, 43))
        tes_image = np.array(tes_screen)
        tes_image = cv2.cvtColor(tes_image, cv2.COLOR_BGR2GRAY)
        #blurred = cv2.GaussianBlur(tes_image, (5, 5), 0)
        ret, thresh = cv2.threshold(tes_image, 100, 255, cv2.THRESH_BINARY_INV)
        #expand = cv2.resize(thresh, (200, 50), interpolation=cv2.INTER_CUBIC)
        cv2.namedWindow('screen')
        cv2.moveWindow('screen', 1500, 500)
        cv2.imshow('screen', thresh)
        cv2.waitKey(500)
        res = pytesseract.image_to_string(thresh, lang='eng')
        print(res)

if __name__ == '__main__':
    check_writing()