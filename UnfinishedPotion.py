import pyautogui
from random import *
import time
import keyboard
import pytesseract
from PIL import ImageGrab
import cv2
import numpy as np
import smtplib
import imaplib
import mailbox
import base64
import email
import re
from email.message import EmailMessage
from email.headerregistry import Address


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'


#For selecting which potion is being made
weed = cv2.imread('ToadFlaxClean.PNG')
vial = cv2.imread('NewVial.PNG')
unf_pot = cv2.imread('ToadFlaxUnf.PNG')


current_email = ''
left = 'left'
right = 'right'
potion_price = 1929
weed_price = 1695

increase = 'increase'
decrease = 'decrease'


def send_email(message):
    #content = 'Robot has finished cleaning ' + str(count)
    #content += ' Ranarr Weeds, netting ' + str((count * potion_price) - (count * ranarr_price)) + 'GP profit'

    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    #Login
    mail.login('taubinrunescape@gmail.com', 'NeverEatSoggyWaffles')
    mail.sendmail('taubinrunescape@gmail.com', '6035082773@vtext.com', message)
    mail.close()
    print('Email sent!')
    return True


def read_emails():
    global current_email

    fdin = open('last_email.txt', 'r')
    prev_com = fdin.read()
    fdin.close()
    fdout = open('last_email.txt', 'w')
    #print(fdin.read())
    #exit()

    username = 'taubinrunescape@gmail.com'
    password = 'NeverEatSoggyWaffles'

    imap = imaplib.IMAP4_SSL('imap.gmail.com')
    imap.login(username, password)

    imap.select('Inbox')

    typ, data = imap.uid('search', None, 'ALL')

    inbox_item_list = data[0].split()

    most_recent = inbox_item_list[-1]

    result, email_data = imap.uid('fetch', most_recent, '(RFC822)')

    raw_email = email_data[0][1].decode('utf-8')

    email_message = email.message_from_string(raw_email)

    latest_email = email_message.get_payload()
    latest_email = re.sub(r"[\n\t\s]*", "", latest_email)
    #print(latest_email, prev_com)
    #exit()

    if latest_email != prev_com:
        send_email(('Mode set to ' + latest_email))

    if latest_email == 'Logout':
        fdout.write(latest_email)
        fdout.close()
        #print('Not the same')
        click(2543, 14, left)
        sleep(0.2)
        click(1226, 729, left)
        sleep(0.1)
        send_email('Successfully Logged Out')
        imap.close()
        imap.logout()
        exit()
        #return True
    if latest_email == 'Create':
        fdout.write(latest_email)
        fdout.close()
        print('Back to grinding')
        imap.close()
        imap.logout()
        return False
    if latest_email == 'Stand by':
        fdout.write(latest_email)
        fdout.close()
        print('Stopping and waiting')
        imap.close()
        imap.logout()
        exit()
    imap.close()
    imap.logout()
    #print()




def setup():
    pyautogui.moveTo(2374, 39, duration=0.33)
    pyautogui.click()
    pyautogui.keyDown('up')
    time.sleep(0.4)
    pyautogui.keyUp('up')
    pyautogui.moveTo(randint(1100, 1800), randint(700, 980), duration=uniform(0.14, 0.23))
    pyautogui.scroll(-1700)


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


def read_item_count(x, y):
    bank_image = ImageGrab.grab(bbox=(x, y, x + 50, y + 12))
    image = np.array(bank_image)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray_image, 175, 255, cv2.THRESH_BINARY_INV)
    thresh = cv2.resize(thresh, (100, 30), interpolation=cv2.INTER_CUBIC)
    string = pytesseract.image_to_string(thresh, config='--psm 6 tessedit_char_whitelist 0123456789', )
    print(string)
    #cv2.namedWindow('screen')
    #cv2.moveWindow('screen', 0, 0)
    #cv2.imshow('screen', thresh)
    #cv2.waitKey(500)
    #cv2.destroyAllWindows()
    return int(string)
    #exit()

def sleep(timer):
    time.sleep(uniform(timer - (timer / 10), timer + (timer / 10)))
    return


def bank():
    global count
    weeds = []
    screen = ImageGrab.grab()
    screen = np.array(screen)

    if image_match(screen, unf_pot, 'gray', 0.88) != 0:
        count += len(image_match(screen, unf_pot, 'gray', 0.88))
    #Right click the banker
    click(1308, 660, right)
    sleep(0.1)

    #Select bank option
    click(1265, 701, left)
    sleep(0.56)

    #Empty out the bag
    click(1314, 1005, left)
    sleep(0.14)

    #Check for supplies
    #vials = read_item_count(989, 304)
    #finished_potions = image_match(screen, cv2.imread('RanarrUnf.PNG'), 'gray', 0.87)
    #weeds = image_match(screen, cv2.imread('EmptyRanarr.PNG'), 'gray', 0.80)
    print(count)
    #if weeds != 0:
        #print('Bank Empty')
        #send_email()
        #exit()

    #Done deposit at bank
    return
    #exit()



def type(string):
    pyautogui.write(string, interval=(uniform(0.04, 0.14)))



def get_item(item):
    #Click the exchange officer
    click(1366, 693, right)
    sleep(0.5)
    #Click on the exchange option
    click(1301, 734, left)
    sleep(0.4)

    #Type in string in GE search
    type(item)
    sleep(0.6)

    #Click on the item in chat box
    click(231, 1278)


def find_price(margin):
    click(251, 1275)

    if margin == increase:

        click(1324, 671, left)



def mix_potions():

    global count

    time.sleep(0.3)
    sleep(5)
    screen = ImageGrab.grab()
    screen = np.array(screen)

    vials = image_match(screen, vial, 'gray', 0.80)
    weeds = image_match(screen, weed, 'gray', 0.80)

    #print(weeds, vials)

    if weeds == 0 or vials == 0:
        print('Empty, ready to sell')
        return send_email('Shlonks created ' + str(count) + 'unfinished potions, yielding a profit of ' + str(count * (potion_price - weed_price - 4)) + 'GP')
        #exit()
    #Click on the vial
    click(vials[randint(0, len(vials) - 3)][0], vials[randint(0, len(vials) - 3)][1], left)
    sleep(0.35)

    #Click on the weed
    click(weeds[randint(2, len(weeds) - 1)][0], weeds[randint(2, len(weeds) - 1)][1], left)
    sleep(0.6)

    #Click create all
    click(233, 1305, left)
    sleep(7.4)

    #Count potions, add them to the count
    #screen = ImageGrab.grab()
    #screen = np.array(screen)
    #count += len(image_match(screen, cv2.imread('RanarrUnf.PNG'), 'gray', 0.85))


def click(x, y, button):
    pyautogui.moveTo(x - 3, y + 3, duration=uniform(0.12, 0.25))
    time.sleep(0.05)
    pyautogui.click(button=button)
    return


def click_clean(x, y, button):
    pyautogui.moveTo(x - 3, y + 3, duration=uniform(0.11, 0.16))
    pyautogui.click(button=button)
    return


def grab_weeds():

    #Right click the weeds
    click(965, 324, right)
    sleep(0.07)

    #Take 14 weeds
    click(922, 393, left)
    sleep(0.05)

    #exit the bank
    click(1362, 248, left)
    sleep(0.04)
    return

def grab_vials():
    #Right click the vials
    click(1010, 322, right)
    sleep(0.09)
    #Take 14 vials
    click(975, 392, left)
    sleep(0.07)
    return
if __name__ == '__main__':
    global count
    global center_matches
    count = 0
    center_matches = []
    #count = input('Enter herb count: ')
    #count = int(count)
    done = False
    receiving = False
    #setup()
    while not done:
        #find_price('Ranarr weed')
        while not receiving:
            #read_emails()
            #if len(center_matches) != 0:
            #center_matches.clear()
            bank()
            grab_vials()
            grab_weeds()
            receiving = mix_potions()
            #read_emails()
            #exit()
            #vials = read_item_count(989, 304)
            #weeds = read_item_count(945, 304)
        while receiving:
            receiving = read_emails()
    exit()