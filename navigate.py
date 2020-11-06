import pyautogui
import time
import tasks
from PIL import ImageGrab

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
    time.sleep(2)
    while True:
        timedKeyPress(2, "up")
        timedKeyPress(2, "down")
        timedKeyPress(2, "left")
        timedKeyPress(2, "right")
        

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