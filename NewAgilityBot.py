import cv2
import pyautogui
import numpy as np
import time
from random import *
from PIL import ImageGrab
import pytesseract
from termcolor import colored, cprint


#def printCyan(skk): print("\033[96m {} \033[00m") .format(skk)


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'


#def regex_match():
    


def troubleshoot_cv2(img):
    cv2.namedWindow('screen')
    cv2.moveWindow('screen', 1500, 500)
    cv2.imshow('screen', img)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()


def check_writing(string):
    time.sleep(0.06)
    new_string = ''
    tes_screen = ImageGrab.grab(bbox=(0, 20, 260, 43))
    tes_image = np.array(tes_screen)
    tes_image = cv2.cvtColor(tes_image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(tes_image, 100, 255, cv2.THRESH_BINARY_INV)
    #bigger = cv2.resize(thresh, (250, 50), interpolation=cv2.INTER_CUBIC)
    res = pytesseract.image_to_string(thresh, lang='eng', config='--psm 6')
    #troubleshoot_cv2(bigger)
    for each in res:
        new_string += each

    #exit()
    print(res)
    quick_fix = new_string[0] + new_string[1] + new_string[2]
    #print('\n', new_string)
    if (new_string == string):
        return True
    if (step == 7 or step == 8 or step == 5) and (quick_fix == 'Jum'):
        return True
    else:
        return False


def crashed():
    global step
    if step == 5:
        #print('We crashed at step 4')
        time.sleep(0.6)
        click(2046, 1056, '')
        time.sleep(6.5)
        click(1911, 850, '')
        time.sleep(10.4)
        return
    if step == 8:
        #print('Crashed at step 7')
        click(1323, 331, '')
        time.sleep(10)
        return
    #exit()


def check_mouse(screen):
    temp = cv2.imread('JumpGap.PNG')
    temp_1 = cv2.imread('TallTree.PNG')
    if step != 4 and step != 7 and step != 1:
        if image_match(screen, temp, '', 0.60) is True:
            print('On Course')
        else:
            print('Off Track')
    if step == 1:
        if image_match(screen, temp_1, '', 0.50) is False:
            print('In wrong spot')
            #exit()
        else:
            print("Climbing Tree")
    if step == 4:
        if image_match(screen, temp, '', 0.60) is False:
            print("We fell off step 4")
            #Write run back to tree
    if step == 7:
        if image_match(screen, temp, '', 0.60) is False:
            print('We fell of step 7')
            #Write run back to tree
    return


def on_start():
    pyautogui.moveTo(2374, 39, duration=0.33)
    pyautogui.click()
    pyautogui.keyDown('up')
    time.sleep(0.4)
    pyautogui.keyUp('up')
    pyautogui.moveTo(randint(1100, 1800), randint(700, 980), duration=uniform(0.14, 0.23))
    pyautogui.scroll(-1700)


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


def check_health():
    global step
    screen = ImageGrab.grab(bbox=(2320, 85, 2340, 100))
    image = np.array(screen)
    if step == 4:
        if image_match(image, cv2.imread('HealthBar.PNG'), 'gray', 0.92) is False:
            print('We fell')
            time.sleep(4)
            click(2102, 1157)
            time.sleep(5.5)
            click(1815, 717)
            step = 2
            return
    if step == 7:
        if image_match(image, cv2.imread('HealthBar.PNG'), 'gray', 0.94) is False:
            print('We fell at step 7')
            time.sleep(4)
            click(1354, 318)
            time.sleep(7.6)
            step = 2
            return
    #print("We didn't fall")

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
            cv2.rectangle(gray_screen, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
        #cv2.namedWindow('detected')
        #cv2.moveWindow('detected', 0, 0)
        #cv2.imshow('detected', screen)
        #print("Iron detected")
        cv2.imwrite('detectedGreen.png', gray_screen)
        #exit()
        #pyautogui.moveTo(((pt[0] + w) / 2), ((pt[1] + h) / 2), duration=0.20)
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


def check_marks():
    global step
    global laps
    whole_screen = ImageGrab.grab()
    screen = np.array(whole_screen)
    #print('Searching ' + str(step))
    if step == 2:
        if click(1256, 609, 'Take Mark of grace / 2 more options') is False:
            click(1252, 454, '')
            time.sleep(6)
        else:
            time.sleep(1.6)
            click(1244, 598, '')
            time.sleep(4.5)
        step = 3
        return
    if step == 3:
        if click(1217, 683, 'Take Mark of grace / 2 more options') is False:
            click(1007, 704, '')
            time.sleep(6.7)
        else:
            time.sleep(2)
            click(1045, 743, '')
            time.sleep(4.8)
        step = 4
        return
    if step == 4:
        #print('Mark Found ' + str(step))
        if click(1168, 848, 'Take Mark of grace / 2 more options') is False:
            click(910, 944, '')
            time.sleep(4.8)
        else:
            time.sleep(1.8)
            click(1030, 799, '')
            time.sleep(3.8)
        step = 5
    if step == 5:
        #print("Mark Found " + str(step))
        if click(1211, 838, 'Take Mark of grace / 2 more options') is False:
            time.sleep(0.8)
            if click(1183, 1106, 'Jump Gap / 2 more options') is False:
                time.sleep(0.4)
                crashed()
                step = 2
                return
            else:
                time.sleep(4.1)
        else:
            time.sleep(2.8)
            click(1245, 950, '')
            time.sleep(3.5)
        step = 6
        return
    if step == 6:
        if click(1265, 805, 'Take Mark of grace / 2 more options') is False:
            click(1364, 860, '')
            time.sleep(7.5)
        else:
            #print("Mark Found " + str(step))
            #click(1265, 805, '')
            time.sleep(2)
            click(1341, 752, '')
            time.sleep(7.5)
        step = 7
        return
    if step == 8:
        if click(1257, 491, 'Jump Gap / 2 more options') is False and click(1257, 491, 'Jump Gap / 6 more options') is False:
            time.sleep(0.4)
            crashed()
            step = 2
            return
        time.sleep(4.6)
        laps += 1
        #printCyan(laps
        step = 1
    cprint('Laps: ' + str(laps) + ' XP: ' + str(laps * 240), 'cyan')
    return


def step_seven():
    on_box = False
    x = 2000
    global step
    while not on_box:
        if click(x, 720, 'Jump Gap / 2 more options') is True:
            on_box = True
        #if click(x, 720, 'Jum\np G\nap 12\noption:'):
         #   on_box = True
        else:
            x -= 50
    step = 8
    time.sleep(7.9)
    return

def click(x, y, string):
    if step == 7:
        delay = uniform(0.0004, 0.0008)
    else:
        delay = uniform(0.17, 0.38)
    pyautogui.moveTo(randint(x - 4, x + 4), randint(y - 4, y + 4), duration=delay)
    time.sleep(0.4)
    if string != '':
        if check_writing(string) is True:
            pyautogui.click()
            return True
        else:
            #print("False")
            return False
    else:
        pyautogui.click()
        #exit()


def did_I_fall():
    whole_screen = ImageGrab.grab()
    screen = np.array(whole_screen)

    if image_match(screen, 'Health.png', "", 0.99):
        step = 1


if __name__ == '__main__':
    global step
    global laps
    laps = 0
    step = 1
    done = False
    on_start()
    x = 0

    #while crashed is not True:
        #check_marks()
    while not done:
        screen = ImageGrab.grab()
        screen = np.array(screen)
        if step != 1 and step != 7:
            check_marks()
            print(step)
        if step == 1:
            print(step)
            click(1177, 537, 'Climb Tall tree / 2 more options')
            #x += 1
            time.sleep(6.5)
            step = 2
        if step == 7:
            print(step)
            step_seven()
        if x == 100:
            exit()
        #check_health()
