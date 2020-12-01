import pyautogui
import time
import tasks
from PIL import ImageGrab, Image
import cv2
import numpy as np

marker = (198, 17, 17)

def map():
    print("Where would you like to go?:")
    print("[1] Custom Map")
    print("[2] Pathfinding")

    option = int(input('options:'))

    if(option == 1):
        custom_map()
    if(option == 2):
        pathfinding()

def custom_map():
    tasks = [
        ["Admin", (1288, 688)], 
        ["Inspect Sample", (807, 511)],
        ["Divert Power", (692, 587)],
        ["Download [Electrical]", (658, 585)]
        ]
    trail = []
    while True:
        imgGrab = ImageGrab.grab(bbox=(0,0,1920,1080))
        img = np.array(imgGrab)
        img[467:655, 836:984] = [0, 0, 0]
        img[504:553, 1055:1216] = [0, 0, 0]
        img[560:600, 628:837] = [0, 0, 0]
        pix = imgGrab.load()

        result = np.zeros((540, 960, 3), dtype = "uint8")
        marker_arrived = (228, 132, 10)
        Y,X = np.where(np.all(img==marker_arrived, axis=2))

        for t in trail:
            y = int(t[1])
            x = int(t[0])
            result[y-1:y+1, x-1:x+1] = [255, 255, 255]

        if len(X) == 0:
            Y,X = np.where(np.all(img==marker, axis=2))
        if len(X) != 0:
            img[Y[0]-1:Y[0]+1, X[0]-1:X[0]+1] = [198, 17, 17]
            y = int(Y[0]/2)
            x = int(X[0]/2)
            trail.append([x, y])
            result[y-1:y+1, x-1:x+1] = [198, 17, 17]
        

        for task in tasks:
            if pix[task[1]][0] > 200:
                y = int(task[1][1]/2)
                x = int(task[1][0]/2)
                result[y-3:y+3, x-3:x+3] = [245, 226, 4]
  
        cv2.imwrite("result.png", cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
        cv2.imshow('Result', cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
        cv2.waitKey(1)
    cv2.destroyAllWindows()

def pathfinding():
    img_map_pix = Image.open('result_test.jpg')
    img_map_og = np.array(img_map_pix)

    nodes = (0, 254, 0)
    #while True:
    img_map_pix = Image.open('result_test.jpg')
    img_map = np.array(img_map_pix)
    imgGrab = ImageGrab.grab(bbox=(0,0,1920,1080))
    img = np.array(imgGrab)
    img[467:655, 836:984] = [0, 0, 0]
    img[504:553, 1055:1216] = [0, 0, 0]
    img[560:600, 628:837] = [0, 0, 0]
    
    pix_map = img_map_pix.load()
    Y,X = np.where(np.all(img==marker, axis=2))
    x = 0
    y = 0
    for i in range(len(X)):
        x = int(X[i]/2)
        y = int(Y[i]/2)
        if pix_map[x, y] == (255, 255, 255):
            img_map[y, x] = [198, 17, 17]
            img_map[y-1:y+1, x-1:x+1] = [198, 17, 17]
            break
    find_path(x, y, pix_map)

    cv2.imshow("result", img_map)
    cv2.waitKey(0)

def find_path(current_pos_x, current_pos_y, pix):
    dir = None
    path = []
    nodes = []
    current_pos = (current_pos_x, current_pos_y)
    destination = (643, 310)
    while True:
        current_pos_x = current_pos[0]
        current_pos_y = current_pos[1]
        possible = [(current_pos_x-1, current_pos_y), (current_pos_x+1, current_pos_y), (current_pos_x, current_pos_y-1), (current_pos_x, current_pos_y+1)]
        if current_pos == destination:
            print("ARRIVED!")
            break
        elif (dir == None) or (pix[possible[dir]] < (240, 240, 240)):
            end_counter = 0
            for moves in possible:
                if pix[moves] != (255, 0, 0) and pix[moves] >= (240, 240, 240):
                    pix[current_pos] = (255, 0, 0)
                    dir = possible.index(moves)
                    path.append(current_pos)
                    current_pos = moves
                else:
                    end_counter += 1
            
            if end_counter == 4:
                if len(nodes) != 0:
                    node_index = path.index(nodes[-1])
                    path = path[:node_index+1]
                    current_pos = path[-1]
                else:
                    print("END")
                    break
            
            elif end_counter != 3:
                nodes.append(current_pos)
                print("EC Node: " + str(current_pos))
        else:
            white_counter = 0
            path.append(current_pos)
            for moves in possible:
                if pix[moves] != (255, 0, 0) and pix[moves] >= (240, 240, 240):
                    white_counter += 1
            
            if white_counter != 1:
                nodes.append(current_pos)
                print("WC Node: " + str(current_pos))

            pix[current_pos] = (255, 0, 0)
            current_pos = possible[dir]

        print(current_pos)
        print(pix[452, 369])
    print(nodes)
    print(path)
'''
        if dir == 0:
            print("Left")
        if dir == 1:
            print("Right")
        if dir == 2:
            print("Up")
        if dir == 3:
            print("Down")
'''

        
