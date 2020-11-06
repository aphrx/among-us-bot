import pyautogui
import time
from PIL import ImageGrab

def menu():
    print("What task would you like to perform:")
    print("[0] Troubleshoot")
    print("[1] Swipe Card")
    print("[2] Download/Upload")
    print("[3] Fuel Engines")
    print("[4] Divert Power")
    print("[5] Empty Chutes")
    print("[6] Accept Power")
    print("[7] Fix Wires")
    option = int(input('options:'))

    if(option == 0):
        troubleshoot()
    elif(option == 1):
        start_task()
        swipe_card()
    elif(option == 2):
        start_task()
        download_upload()
    elif(option == 3):
        start_task()
        fuel_engines()
    elif(option == 4):
        start_task()
        divert_power()
    elif(option == 5):
        start_task()
        empty_chute()
    elif(option == 6):
        start_task()
        accept_power()
    elif(option == 7):
        start_task()
        fix_wires()
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
    menu()

def download_upload():
    pyautogui.moveTo(970, 650)
    pyautogui.click()
    menu()

def accept_power():
    pyautogui.moveTo(956, 539)
    pyautogui.click()
    menu()

def fuel_engines():
    pyautogui.moveTo(1470, 880)
    pyautogui.mouseDown()
    time.sleep(5)
    pyautogui.mouseUp()
    menu()

def divert_power():
    sliders = [(620, 780), (715, 780), (813, 780), (912, 780), (1007, 780), (1101, 780), (1201, 780), (1297, 780)]
    for i in sliders:
        pyautogui.moveTo(i)
        pyautogui.drag(0, -100, 0.5, button='left')
    menu()

def empty_chute():
    pyautogui.moveTo(1270,420)
    pyautogui.mouseDown()
    pyautogui.moveTo(1270,720)
    time.sleep(5)
    pyautogui.mouseUp()
    menu()

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

#start_task()
#empty_chute()
#troubleshoot()
#divert_power()
#download()
#fuel_engines()
menu()