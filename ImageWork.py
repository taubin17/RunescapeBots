import cv2
import pyautogui
import numpy as np
from PIL import ImageGrab
import time
import imutils
import pytesseract
from skimage.measure import compare_ssim
from bs4 import BeautifulSoup

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

def trash(image):
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for each in cnts:
        M = cv2.moments(each)
        cX = int(M['m10'] / M['m00'])
        cY = int(M['m01'] / M['m00'])

        cv2.drawContours(image, [each], -1, (0, 255, 0), 2)
        cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
        cv2.putText(image, 'center', (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.imshow('Conts', image)
        cv2.waitKey(0)
    #time.sleep(4)


def FindColor(image, boundaries):
    for lower, upper in boundaries:
        lower = np.array(lower, dtype = 'uint8')
        upper = np.array(upper, dtype = 'uint8')

        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)

        for x in range(len(output[40])):
            if output[40][x].any():
                print(output[40][x], x)
            #print(each)
        #trash(image)
        cv2.imshow('color', output)
        cv2.waitKey(10000)
        exit()



if __name__ == '__main__':
    done = False

    boundaries = [
        ([20, 20, 60], [40, 40, 77])
    ]
    #for x in range (3):
        #time.sleep(1)
        #print(3-(x+1))
    screen = ImageGrab.grab(bbox=(2320, 85, 2327, 100))
    second_char = ImageGrab.grab(bbox=(2327, 85, 2334, 100))
    image_two = np.array(second_char)
    #screen = ImageGrab.grab()
    image = np.array(screen)
    #image = cv2.imread('Fixed.PNG')
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    six = cv2.imread('Five.PNG')
    six = cv2.cvtColor(six, cv2.COLOR_BGR2GRAY)
    six = cv2.resize(six, (1000, 500), interpolation=cv2.INTER_CUBIC)
    big_image = cv2.cvtColor(image_two, cv2.COLOR_BGR2GRAY)
    big_image = cv2.resize(big_image, (1000, 500), interpolation=cv2.INTER_CUBIC)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(big_image, (5, 5), 0)
    ret, thresh = cv2.threshold(blurred, 103, 255, cv2.THRESH_BINARY_INV)
    cv2.imwrite('One.png', thresh)
    #image = cv2.imread('detectedGreen.png')
    #FindColor(image, boundaries)
    (score, diff) = compare_ssim(thresh, six, full=True)
    diff = (diff * 255).astype('uint8')
    print('SSIM: {}'.format(score))

    thresh2 = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(thresh, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(six, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('Original', six)
    cv2.imshow('Modded', thresh)
    cv2.imshow('Diff', diff)
    cv2.imshow('Thresh', thresh2)
    cv2.waitKey(1)

    #gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #blurred = cv2.GaussianBlur(big_image, (5, 5), 0)
    #ret, thresh = cv2.threshold(blurred, 103, 255, cv2.THRESH_BINARY_INV)
    #health = pytesseract.image_to_string(thresh, lang='eng',config='--psm 5 -c tessedit_char_whitelist=0123456789')
    #print(health)
    #while not done:
    #cv2.imshow('screen', thresh)
    #cv2.imwrite('Six.png', thresh)
    #cv2.waitKey(10000)
    #cv2.destroyAllWindows()







