import pytesseract
from PIL import ImageGrab
import numpy as np
import time
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

if __name__ == '__main__':
    done = False

    while not done:
        screen = ImageGrab.grab(bbox=(0, 0, 200, 200))
        img = np.array(screen)

        health = pytesseract.image_to_string(cv2.imread('Numbers.PNG'))
        print (health)
        time.sleep(10)