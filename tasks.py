import pyautogui
import time
import numpy as np
import cv2
from PIL import ImageGrab, Image
import pytesseract

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
    print("[15] Calibrate Distributor")
    print("[16] Start Reactor")
    print("[17] Chart Course")
    print("[18] Unlock Manifold")
    
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
    elif(option == 15):
        start_task()
        calibrate_distributor()
        menu()
    elif(option == 16):
        start_task()
        start_reactor()
        menu()
    elif(option == 17):
        start_task()
        chart_course()
        menu()
    elif(option == 18):
        #start_task()
        unlock_manifold()
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
    img = ImageGrab.grab(bbox=(0,0 ,1920,1080))
    pix = img.load()
    for i in sliders:
        if pix[i][0] > 50:
            pyautogui.moveTo(i)
            pyautogui.drag(0, -100, 0.5, button='left')
            break

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
    red = (202, 102, 120)
    img = ImageGrab.grab(bbox=(0,0 ,1920,1080))
    pix = img.load()
    for tile in tiles:
        print(pix[tile])
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
        img = ImageGrab.grab(bbox=(553,135,1361,941))
        array = np.array(img)
        asteroid = (24, 56, 41)
        Y,X = np.where(np.all(array==asteroid, axis=2))
        if len(X) != 0:
            pyautogui.moveTo(X[0]+553, Y[0]+135)
            pyautogui.click()

def clean_O2_filter():
    while True:
        img = ImageGrab.grab(bbox=(0,0 ,1920,1080))
        array = np.array(img)
        leaf = (198, 150, 66)
        Y,X = np.where(np.all(array==leaf, axis=2))
        if len(X) != 0:
            pyautogui.moveTo(X[0], Y[0])
            pyautogui.dragTo(668, 555, 0.5, button='left')

def calibrate_distributor():
    distributor = [(800, 300), (800, 550), (800, 830)]
    buttons = [(1230, 310), (1230, 580), (1230, 840)]
    on = (71, 73, 71)
    for i in range(3):
        pyautogui.moveTo(buttons[i])
        while True:
            img = ImageGrab.grab(bbox=(0,0 ,1920,1080))
            pix = img.load()
            print(pix[distributor[i]])
            if pix[distributor[i]] == on:
                pyautogui.click()
                break

def start_reactor(): 
    lights = [(500, 450), (650, 450), (790, 450), (500, 600), (650, 600), (790, 600), (500, 750), (650, 750), (790, 750)]
    buttons = [(1140, 450), (1260, 450), (1400, 450), (1140, 600), (1260, 600), (1400, 600), (1140, 750), (1260, 750), (1400, 750), ]
    
    on = (68, 168, 255)
    for i in range(0, 5):
        flashed = []
        while True:
            img = ImageGrab.grab(bbox=(0,0 ,1920,1080))
            pix = img.load()
            for j in range(9):
                if(pix[lights[j]] == on):
                    flashed.append(j)
                    time.sleep(0.3)

            if len(flashed) == (i + 1):
                break
            
        time.sleep(1)
        print(flashed)
        for k in flashed:
            pyautogui.moveTo(buttons[k])
            pyautogui.click()
            time.sleep(0.2)        

def stabilize_steering():
    pyautogui.moveTo(960, 537)
    pyautogui.click()

def chart_course():
    while True:
        img = ImageGrab.grab(bbox=(0,0 ,1920,1080))
        array = np.array(img)
        rocket = (37, 111, 159)
        nodes = (36, 111, 159)
        Y,X = np.where(np.all(array==rocket, axis=2))
        Yn,Xn = np.where(np.all(array==nodes, axis=2))
        if len(X) != 0 and len(Xn) != 0:
            pyautogui.moveTo(X[0], Y[0])
            pyautogui.dragTo(Xn[0], Yn[0], 0.1, button='left')

def unlock_manifold_get_numbers():
    start_task()
    merged = Image.new("RGB", (1150, 115))
    number_box_start = [(585,395), (737, 395), (890, 395), (1040, 395), (1195, 395), (585,548), (737, 548), (890, 548), (1040, 548), (1195, 548)]
    
    for i in range(10):
        img = ImageGrab.grab(bbox=(number_box_start[i][0]+10,number_box_start[i][1]+10,number_box_start[i][0]+125,number_box_start[i][1]+125))
        merged.paste(img, (int(i * 115),0))
        
    img = np.array(merged)
    img = img[:, :, ::-1].copy()
    img[:,:,0] = np.zeros([img.shape[0], img.shape[1]])
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Connect text with a horizontal shaped kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10,3))
    dilate = cv2.dilate(thresh, kernel, iterations=3)

    # Remove non-text contours using aspect ratio filtering
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        aspect = w/h
        if aspect < 3:
            cv2.drawContours(thresh, [c], -1, (0,0,0), -1)

    # Invert image and OCR
    result = 255 - thresh
    cv2.imwrite("manifold_debug.png", result)
    data = pytesseract.image_to_string(result, lang='eng',config='--psm 6 -c tessedit_char_whitelist=123456789N')
    return data.strip()

def unlock_manifold():
    data = unlock_manifold_get_numbers()
    whitelist = "123456789N"
    print(data)
    print(len(data))
    if(len(data) == 10):
        print("Correct len")
    else:
        start_task()
        unlock_manifold()
    for i in data:
        for j in whitelist:
            print (i + " and " + j + " are " + str(i==j))
            if i == j:
                whitelist = whitelist.replace(j, "")
    print("whitelist: " + whitelist + "len: " + str(len(whitelist)))
    if (whitelist == ""):
        print("success")
    else:
        start_task()
        unlock_manifold() 