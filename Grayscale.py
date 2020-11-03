from PIL import ImageGrab
import cv2
import pyautogui
import numpy as np
import time

for x in range(5):
    time.sleep(1)
    print(5 - x)

screen = ImageGrab.grab()
screen = np.array(screen)
gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
cv2.imwrite('grayscreen.png', gray_screen)