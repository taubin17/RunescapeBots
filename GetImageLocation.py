import cv2
import pyautogui
from PIL import ImageGrab
import numpy as np
import random
import time
if __name__ == '__main__':
    x = 1336
    y = 700
    y_change = 30
    we_are_stuck = 0
    need_to_click = True
    global screen
    test = True
    while test == True:
        screen = ImageGrab.grab(bbox=(2310, 1100, 2500, 1365))
        #whole_screen = ImageGrab.grab()
        #cv2.namedWindow('screen')
        #cv2.moveWindow('screen', 1600, 1100)
        cv2.imshow('Screen15', np.array(screen))

        #y += y_change
        #y_change = 30
        #if is_bag_full() == True:
            #drop_fish()
        #time.sleep(1)
        #fish_avail = is_fish(img)
        #print (str(fish_avail))
        #time.sleep(3)
        time.sleep(1)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            #cv2.imwrite('Fishing.png', img)
            cv2.destroyAllWindows()
            break

