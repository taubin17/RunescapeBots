import cv2
import pyautogui
import numpy as np
from PIL import ImageGrab
import imutils


def image_match(r, pic, match_type, accuracy):
    #screen = r
    #gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    template = pic
    gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    #w, h = gray_template.shape[::-1]

    if match_type == "gray" or match_type == "grey":
        res = cv2.matchTemplate(r, gray_template, cv2.TM_CCOEFF_NORMED)
        w, h = gray_template.shape[::-1]
        #cv2.imshow('screen2', gray_screen)
        #cv2.imshow('screen3', gray_template)
    else:
        #w, h = template.shape[::-1]
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
            cv2.rectangle(r, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
        #cv2.namedWindow('detected')
        #cv2.moveWindow('detected', 0, 0)
        #cv2.imshow('detected', screen)
        #print("Iron detected")
        #cv2.imwrite('detectedGreen.png', gray_screen)
        #exit()
        #if step != 1 and fell is False:
           # pyautogui.moveTo((pt[0] + (w / 2)), (pt[1] + (h / 2)), duration=0.20)
       # else:
            #pyautogui.moveTo((pt[0] + (w / 2)), (pt[1] + 15), duration=0.20)
        #pyautogui.click()
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


def check_fall():
    global fell
    fell = False

def step_one():

    global step
    step = 1
    screen = ImageGrab.grab()
    screen = np.array(screen)

    step_images = []
    step_images.append(cv2.imread('Tree.PNG'))

    gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray_screen, (5, 5), 0)
    ret, thresh = cv2.threshold(blurred, 120, 140, cv2.THRESH_BINARY_INV)

    #cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #cnts = imutils.grab_contours(cnts)
    if image_match(thresh, step_images[0], 'gray', 0.80):
        print("Found Tree")
    cv2.imshow('thresh', thresh)
    cv2.waitKey(50000)
    cv2.destroyAllWindows()
    #print('Done')
    return


if __name__ == '__main__':
    step_one()