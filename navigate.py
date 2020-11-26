import pyautogui
import time
import tasks
from PIL import ImageGrab
import cv2
import numpy as np

def map():
    print("Where would you like to go?:")
    print("[0] Troubleshoot")
    print("[1] Admin: Swipe Card")

    option = int(input('options:'))

    if(option == 0):
        troubleshoot()
    if(option == 1):
        admin_swipe_card()

def troubleshoot():
    #while True:
    img = ImageGrab.grab(bbox=(0,0,1920,1080))
    pix = img.load()
    img = np.array(img)
    
    print(pix[1068, 216])

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
    #lower_range = np.array([10,40,220])
    #upper_range = np.array([190,200,250])

    lower_range = np.array([100,10,10])
    upper_range = np.array([200,20,20])
    
    mask = cv2.inRange(img, lower_range, upper_range)
    output = cv2.bitwise_and(img, img, mask = mask)

    
    cv2.imshow('img', cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    cv2.imshow('mask', mask)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
        

def timedKeyPress(dur, key):
    end = time.time() + dur
    while(time.time() < end):
        pyautogui.keyDown(key)
    pyautogui.keyUp(key)

def admin_swipe_card():
    time.sleep(2)
    timedKeyPress(0.5, "right")
    timedKeyPress(1, "down")
    timedKeyPress(0.7, "left")
    timedKeyPress(2.8, "down")
    timedKeyPress(2.5, "right")
    timedKeyPress(0.5, "down")
    tasks.start_task()
    tasks.swipe_card()
    timedKeyPress(0.5, "up")
    timedKeyPress(2.5, "left")
    timedKeyPress(2.8, "up")
    timedKeyPress(0.7, "right")
    timedKeyPress(1, "up")
    timedKeyPress(0.5, "left")