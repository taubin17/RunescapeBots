import cv2
import pyautogui
import numpy as np
import time
from random import *
from PIL import ImageGrab

def run_to_bank():
    print("Run to bank here!")
    pyautogui.moveTo(878, 53, duration=0.26)
    pyautogui.click()
    time.sleep(10)
    pyautogui.moveTo(439, 280)
    print("Attempting to bank")
    time.sleep(2)
    pyautogui.click()
    print("Attempting click on bank booth")
    time.sleep(5)
    pyautogui.moveTo(584, 466, duration=0.21)
    print("Hovering over depo all now")
    time.sleep(0.4)
    print("Depoed complete")
    pyautogui.click()
    time.sleep(0.6)
    pyautogui.moveTo(314, 232)
    print("Grabbed axe from bank")
    time.sleep(0.5)
    pyautogui.click()
    print("Done grabbing the axe")
    time.sleep(0.40)
    pyautogui.moveTo(609, 49, duration=0.20)
    print("Moved cursor to close bank")
    pyautogui.click()
    time.sleep(0.15)
    run_to_tree()

    #exit()
def run_to_tree():
    pyautogui.moveTo(969, 172, duration= 0.23)
    print("Running as far as possible from bank")
    pyautogui.click()
    time.sleep(10)
    pyautogui.moveTo(559, 471, duration = 0.25)
    print("Moving right next to the tree")
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(562, 358, duration= 0.14)
    print("Moving cursor over tree")
    time.sleep(0.24)
def at_oak(screen):
    pic = cv2.imread('ChopOak.png')
    #cv2.namedWindow('Oak')
    #cv2.moveWindow('Oak', 1500, 1100)
    #cv2.imshow('Oak', screen)
    is_bag_full()
    at_oak = image_match(screen, pic, "", 0.50)
    if at_oak == True:
        print("Cutting Tree")
        pyautogui.click()
        time.sleep(randint(5, 9))
def is_bag_full():
    #print("Checking Bag")
    at_trees = False
    #whole_bag = ImageGrab.grab(bbox=(810, 375, 988, 638))
    #whole_bag = np.array(whole_bag)
    #cv2.namedWindow('WholeBag')
    #cv2.moveWindow('WholeBag',300, 1000)
    #cv2.imshow('WholeBag', whole_bag)
    last_slot = ImageGrab.grab(bbox=(937, 575, 995, 638))
    last_slot = np.array(last_slot)
    #cv2.imshow('location', last_slot)
    #time.sleep(1)
    pic = cv2.imread('Backpack.png')
    backpack_full = not (image_match(last_slot, pic, "gray", .90))
    print("Checking bag")
    if backpack_full == True:
        print('Backpack is full!')
        run_to_bank()
        at_trees = False
    if backpack_full == False and at_trees == False:
        #run_to_tree()
        at_trees = True
    #cv2.imwrite('Backpack.png', last_slot)
    #cv2.namedWindow('backpack')
    #cv2.moveWindow('backpack', 1500, 1100)
    #cv2.imshow('backpack', last_slot)
    #return
def at_bank():
    pic = cv2.imread('Bank.png')
    at_bank = image_match(np.array(screen), pic, "", 0.40)
    if at_bank == True:
        print ("At the Bank")
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(584, 480, duration=0.21)
        time.sleep(0.04)
        pyautogui.click()
        time.sleep(0.06)
        pyautogui.moveTo(621, 49, duration=0.20)
        pyautogui.click()
        run_to_tree()
    return at_bank
def image_match(r, pic, match_type, accuracy):
    screen = r
    gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    template = pic
    gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    #w, h = gray_template.shape[::-1]

    if match_type == "gray" or match_type == "grey":
        res = cv2.matchTemplate(gray_screen, gray_template, cv2.TM_CCOEFF_NORMED)
        #cv2.imshow('screen2', gray_screen)
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
        return True
    else:
        return False
    #else:
        #print("No match detected")
        #for pt in zip(*loc[::-1]):
            #cv2.rectangle(screen, pt, (pt[0] + w), (0, 255, 255), 2)
        #cv2.imshow('detected', screen)
        #return True
    #else:
        #return False

last_time = time.time()
if __name__ == '__main__':
    global screen
    test = True
    while test == True:
        #Where the AI looks at for determining tree readiness/at the bank
        screen = ImageGrab.grab(bbox=(0, 30, 114, 60))

        #Comment out screen and uncomment this screen to take/reset an image!
        #screen = ImageGrab.grab(bbox=(942, 580, 990, 624))


        img = np.array(screen)
        chop_oak = cv2.imread('ChopOak.png')
        #print("We've successfully started running on windows!")
        cv2.namedWindow('screen')
        cv2.moveWindow('screen', 1600, 1100)
        cv2.imshow('screen', np.array(screen))

        fps = (int(1 / (time.time() - last_time)))
        #print ('Fps: ', fps)
        #print (pyautogui.position())
        time.sleep(1)

        #Check if bag is full
        #is_bag_full()

        #Bank Section
        #if at_bank(img) == True:
        #    pyautogui.click()
        #    time.sleep(5)
        #    pyautogui.moveTo(584, 480, duration=0.21)
        #    time.sleep(0.04)
        #    pyautogui.click()
        #    time.sleep(0.06)
        #    pyautogui.moveTo(621, 49, duration=0.20)
        #    pyautogui.click()
        #    run_to_tree()
            #while 1:
                #print(pyautogui.position())


        #Wood Cutting Section
        #at_oak(img)




        #if image_match(img, chop_oak) == True:
            #print("It says tree is ready!")
            #cv2.imshow('screen2', screen)
            #cv2.imshow('screen3', chop_oak)
        #else:
            #print("Tree is not ready")
        #time.sleep(1)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            #cv2.imwrite('Backpack.png', img)
            cv2.destroyAllWindows()
            break
        last_time = time.time()

        #time.sleep(10)
        #print("We took a scrot")