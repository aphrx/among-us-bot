import pyautogui
import time
from PIL import ImageGrab
import numpy as np

def menu():
    print("What task would you like to perform?:")
    print("[0] Troubleshoot")
    print("[1] Swipe Card")
    print("[2] Download/Upload")
    print("[3] Fuel Engines")
    print("[4] Divert Power")
    print("[5] Empty Chutes")
    print("[6] Accept Power")
    print("[7] Fix Wires")
    print("[8] Prime Shields")
    print("[9] Inspect Sample")
    print("[10] Stabilize Steering")
    print("[11] Submit Scan")
    print("[12] Align Engine Output")
    print("[13] Clear Asteroids")
    print("[14] Clean O2 Filter")
    
    option = int(input('options:'))

    if(option == 0):
        troubleshoot()
    elif(option == 1):
        start_task()
        swipe_card()
        menu()
    elif(option == 2):
        start_task()
        download_upload()
        menu()
    elif(option == 3):
        start_task()
        fuel_engines()
        menu()
    elif(option == 4):
        start_task()
        divert_power()
        menu()
    elif(option == 5):
        start_task()
        empty_chute()
        menu()
    elif(option == 6):
        start_task()
        accept_power()
    elif(option == 7):
        start_task()
        fix_wires()
        menu()
    elif(option == 8):
        start_task()
        prime_shields()
        menu()
    elif(option == 9):
        start_task()
        inspect_sample()
        menu()
    elif(option == 10):
        start_task()
        stabilize_steering()
        menu()
    elif(option == 11):
        start_task()
        menu()
    elif(option == 12):
        start_task()
        align_engine_output()
        menu()
    elif(option == 13):
        start_task()
        clear_asteroids()
        menu()
    elif(option == 14):
        start_task()
        clean_O2_filter()
        menu()
    else:
        print("Invalid option, please try again!")
        menu()
    
def troubleshoot():
    while True:
        print(pyautogui.position())

def start_task():
    pyautogui.moveTo(1800, 930)
    pyautogui.click()
    time.sleep(1)

def swipe_card():
    pyautogui.moveTo(777, 814)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(540, 400)
    pyautogui.drag(900, 0, 0.8, button='left')

def download_upload():
    pyautogui.moveTo(970, 650)
    pyautogui.click()

def accept_power():
    pyautogui.moveTo(956, 539)
    pyautogui.click()

def fuel_engines():
    pyautogui.moveTo(1470, 880)
    pyautogui.mouseDown()
    time.sleep(5)
    pyautogui.mouseUp()

def divert_power():
    sliders = [(620, 780), (715, 780), (813, 780), (912, 780), (1007, 780), (1101, 780), (1201, 780), (1297, 780)]
    for i in sliders:
        pyautogui.moveTo(i)
        pyautogui.drag(0, -100, 0.5, button='left')

def empty_chute():
    pyautogui.moveTo(1270,420)
    pyautogui.mouseDown()
    pyautogui.moveTo(1270,720)
    time.sleep(3)
    pyautogui.mouseUp()

def fix_wires():
    wires = [(560, 270), (560, 460), (560, 650), (560, 830), (1330, 270), (1330, 460), (1330, 650), (1330, 830)]
    img = ImageGrab.grab(bbox=(0,0 ,1920,1080))
    pix = img.load()

    for i in range(0, 4):
        for j in range(4, 8):
            if pix[wires[i]] == pix[wires[j]]:
                pyautogui.moveTo(wires[i])
                pyautogui.mouseDown()
                pyautogui.moveTo(wires[j])
                pyautogui.mouseUp()

def prime_shields():
    tiles = [(970, 370), (1080, 450), (1090, 640), (967, 547), (999, 699), (815, 617), (820, 458)]
    red = (202, 94, 112)
    img = ImageGrab.grab(bbox=(0,0 ,1920,1080))
    pix = img.load()
    for tile in tiles:
        if pix[tile] == red:
            pyautogui.moveTo(tile)
            pyautogui.click()
            

def inspect_sample():
    tubes = [(732, 590), (850, 590), (960, 590), (1075, 590), (1190, 590)]
    red = (246, 134, 134)
    pyautogui.moveTo(1260, 930)
    pyautogui.click()
    time.sleep(70)
    img = ImageGrab.grab(bbox=(0,0 ,1920,1080))
    pix = img.load()
    for tube in tubes:
        if pix[tube] == red:
            pyautogui.moveTo(tube[0], 850)
            pyautogui.click()

def align_engine_output():
    img = ImageGrab.grab(bbox=(0,0 ,1920,1080))
    im = np.array(img)
    marker = (202, 202, 216)
    Y,X = np.where(np.all(im==marker, axis=2))
    pyautogui.moveTo(X[0], Y[0])
    pyautogui.mouseDown()
    pyautogui.moveTo(1250, 540)
    pyautogui.mouseUp()

def clear_asteroids(): # Horrible Accuracy
    while True:
        img = ImageGrab.grab(bbox=(0,0 ,1920,1080))
        array = np.array(img)
        asteroid = (24, 56, 41)
        Y,X = np.where(np.all(array==asteroid, axis=2))
        if len(X) != 0:
            pyautogui.moveTo(X[0], Y[0])
            pyautogui.click()
            time.sleep(0.5)

def clean_O2_filter():
    while True:
        img = ImageGrab.grab(bbox=(0,0 ,1920,1080))
        array = np.array(img)
        leaf = (198, 150, 66)
        Y,X = np.where(np.all(array==leaf, axis=2))
        if len(X) != 0:
            pyautogui.moveTo(X[0], Y[0])
            pyautogui.dragTo(668, 555, 0.5, button='left')

def stabilize_steering():
    pyautogui.moveTo(960, 537)
    pyautogui.click()
    