import pyautogui
import time
import tasks
from PIL import ImageGrab, Image
import cv2
import numpy as np
import random

marker = (198, 17, 17)
marker_arrived = (228, 132, 10)
tasks = [
        ["Align Engine (Upper Engine)", (130, 179)],
        ["Align Engine (Lower Engine)", (133, 425)],

        ["Calibrate Distributor", (410, 323)],

        ["Chart Course", (903, 236)],

        ["Clean O2 Filter", (635, 228)],

        ["Clear Asteroids", (707, 123)],

        ["Divert Power", (328, 315)],
        ["Accept Power (Communications)", (656, 461)],
        ["Accept Power (Lower Engine)", (157, 356)],
        ["Accept Power (Upper Engine)", (172, 105)],
        ["Accept Power (Navigation)", (860, 211)],
        ["Accept Power (O2)", (705, 216)],
        ["Accept Power (Security)", (274, 224)],
        ["Accept Power (Shields)", (745, 375)],
        ["Accept Power (Weapons)", (760, 123)],

        ["Empty Garbage/Chute (Cafeteria)", (623, 81)],
        ["Empty Garbage/Chute (O2)", (635, 239)],
        ["Empty Garbage/Chute (Storage)", (534, 519)],

        ["Fix Wires (Electrical)", (368, 328)],
        ["Fix Wires (Storage)", (475, 343)],
        ["Fix Wires (Security)", (201, 255)],
        ["Fix Wires (Navigation)", (801, 241)],
        ["Fix Wires (Admin)", (534, 284)],
        ["Fix Wires (Cafeteria)", (421, 62)],

        ["Fuel Engine (Storage)", (465, 450)],
        ["Fuel Engine (Lower Engine)", (150, 425)],
        ["Fuel Engine (Upper Engine)", (146, 175)],

        ["Inspect Sample", (394, 253)],

        ["Prime Shields", (684, 459)],

        ["Stabilize Steering", (903, 261)],

        ["Start Reactor", (78, 271)],

        ["Submit Scan", (360, 268)],

        ["Swipe Card", (635, 337)], 

        ["Unlock Manifolds", (60, 213)],
        
        ["Download/Upload (Cafeteria)", (601, 55)],
        ["Download/Upload (Admin)", (552, 284)],
        ["Download/Upload (Communications)", (589, 453)],
        ["Download/Upload (Electrical)", (317, 323)],
        ["Download/Upload (Navigation)", (860, 211)],
        ["Download/Upload (Weapons)", (694, 86)]]

def get_screen():
    imgGrab = ImageGrab.grab(bbox=(0,0,1920,1080))
    img = np.array(imgGrab)
    img[467:655, 836:984] = [0, 0, 0]
    img[504:553, 1055:1216] = [0, 0, 0]
    img[560:600, 628:837] = [0, 0, 0]
    pix = imgGrab.load()
    return img, pix

def pathfinding(i):
    img_map_pix = Image.open('result_test_2.jpg')
    destination = tasks[i][1]
    print(tasks[i][0])
    
    img_map = np.array(img_map_pix)
    img=Image.fromarray(img_map)
    pix_map = img_map_pix.load()

    imgGrab = ImageGrab.grab(bbox=(0,0,1920,1080))
    img = np.array(imgGrab)
    img[467:655, 836:984] = [0, 0, 0]
    img[504:553, 1055:1216] = [0, 0, 0]
    img[560:600, 628:837] = [0, 0, 0]
    
    colors = [(198, 17, 17), (228, 132, 10), (101, 7, 46), (149, 202, 220), (174, 116, 27), (224, 116, 9)]
    
    x = 0
    y = 0

    for color in colors:
        Y,X = np.where(np.all(img==color, axis=2))
        for i in range(len(X)):
            xt = int(X[i]/2)
            yt = int(Y[i]/2)
            print(str(xt) + ", " + str(yt))
            if pix_map[xt, yt] > (200, 200, 200):
                x = xt
                y = yt
                break
    
    if x == 0:
        print("Can't find") 
        return 0

    path, directions = search((x, y), destination, img_map, pix_map)

    for i in path:
        img_map[i[1], i[0]] = (0, 255, 0)

    return navigate(path, directions, img_map, destination)

    

def navigate(path, directions, img_map, destination):
    log = []
    img_map_org = img_map
    direction = None
    turns = []
    pyautogui_directions = ["left", "right", "up", "down"]
    time.sleep(2)
    path = path[2:]
    directions = directions[2:]

    for i in range(len(directions)):

        if direction != directions[i]:
            direction = directions[i]
            turns.append([path[i], directions[i]])
    turns.append([path[-1], -1])

    dir = None
    while len(turns) > 0:
        img_map = img_map_org
        img, pix = get_screen()

        Y,X = np.where(np.all(img==marker, axis=2))
        
        colors = [(198, 17, 17), (228, 132, 10), (101, 7, 46), (149, 202, 220), (174, 116, 27), (220, 102, 10)]
        print(dir)
        if len(X) != 0:
            for color in colors:
                Y,X = np.where(np.all(img==color, axis=2))
                if len(X) > 0:
                    break

        x = 0
        y = 0

        for i in range(len(X)):
            x += int(X[i]/2)
            y += int(Y[i]/2)
        if len(X) != 0:
            x = int(x/len(X))-10
            y = int(y/len(Y))+10
        log.append([x, y])
        p = 14

        
        if((len(log) > 5 and log[-1] == log[-5]) or (x == 0)):
            if len(turns) == 1:
                break
            wiggle(log[-1], turns[0][0], dir)
            
        img_map[y-p:y+p, x-p:x+p] = [198, 17, 17]

        pixel = Image.fromarray(img_map, 'RGB').load()

        if pixel[destination][1] == 17:
            if dir is not None:
                pyautogui.keyUp(pyautogui_directions[dir])
            return 1

        elif pixel[(turns[0][0][0]), (turns[0][0][1])] == (198, 17, 17) or dir is None:
            if dir is not None:
                pyautogui.keyUp(pyautogui_directions[dir])
            dir = turns[0][1]
            turns.pop(0)
                    
        pyautogui.keyDown(pyautogui_directions[dir])

        cv2.imshow("result", img_map)
        cv2.waitKey(1)
    cv2.destroyAllWindows()
    pyautogui.keyUp(pyautogui_directions[dir])
    return 1

def wiggle(current, turn, dir):
    key = None

    if dir == 0 or dir == 1:
        if current[1] > turn[1]:
            key = "up"
        else:
            key = "down"
    elif dir == 2 or dir == 3:
        if current[0] > turn[0]:
            key = "left"
        else:
            key = "right"
    pyautogui.click(5, 5)
    pyautogui.keyDown(key)
    time.sleep(0.1)
    pyautogui.keyUp(key)
    

def search(start, end, img, pix):
    print(start)
    isFound = False
    current = start
    array = np.array(img)
    path = []
    intersects = []
    directions = []
    path.append(current)
    while isFound is False:
        possible = []
        surroundings = [(current[0]-1, current[1]),
                        (current[0]+1, current[1]),
                        (current[0], current[1]-1),
                        (current[0], current[1]+1)]


        for move in surroundings:
            if end == move:
                isFound = True
            if (pix[move] >= (200, 200, 200) and pix[move] != (255, 255, 0)):
                possible.append(move)
        
        if len(possible) >= 2:
            if current not in intersects:
                intersects.append(current)
        if len(possible) == 0:
            intersects_reversed = intersects[::-1]
            for i in intersects_reversed:
                if i != current:
                    current = i
                    intersects.pop(intersects.index(i))
                    break
            ind = path.index(current)
            path = path[:ind]
            directions = directions[:ind]
        
        else:
            current = random.choice(possible)
        
        #print(current)

        path.append(current)
        if current in surroundings:
            directions.append(surroundings.index(current))
        array[current[1], current[0]] = (255, 255, 0)
        img=Image.fromarray(array)
        pix = img.load()

        cv2.imshow("result", array)
        cv2.waitKey(1)
    for p in path:
        array[p[1], p[0]] = (0, 255, 0)
    img=Image.fromarray(array)
    cv2.destroyAllWindows() 

    return path, directions
   
