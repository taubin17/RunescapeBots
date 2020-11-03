import pyautogui
import numpy
import cv2
import time
import random

pyautogui.moveTo(584, 466, duration=0.21)
print("Hovering over depo all now")
time.sleep(10)
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