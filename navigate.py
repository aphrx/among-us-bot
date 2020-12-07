import pyautogui
import time
import tasks
from PIL import ImageGrab, Image
import cv2
import numpy as np
import random

marker = (198, 17, 17)
marker_arrived = (228, 132, 10)
tasks = [["Admin Swipe", (641, 337)], 
        ["Fuel Engine (Storage)", (466, 449)],
        ["Fix Wires (Electrical)", (372, 323)],
        ["Calibrate Distributor", (410, 323)],
        ["Divert Power", (329, 323)],
        ]

def map():
    print("Where would you like to go?:")
    print("[1] Custom Map")
    print("[2] Pathfinding")

    option = int(input('options:'))

    if(option == 1):
        custom_map()
    if(option == 2):
        pathfinding()

def get_screen():
    imgGrab = ImageGrab.grab(bbox=(0,0,1920,1080))
    img = np.array(imgGrab)
    img[467:655, 836:984] = [0, 0, 0]
    img[504:553, 1055:1216] = [0, 0, 0]
    img[560:600, 628:837] = [0, 0, 0]
    pix = imgGrab.load()
    return img, pix



def custom_map():
    
    trail = []
    while True:
        imgGrab = ImageGrab.grab(bbox=(0,0,1920,1080))
        img = np.array(imgGrab)
        img[467:655, 836:984] = [0, 0, 0]
        img[504:553, 1055:1216] = [0, 0, 0]
        img[560:600, 628:837] = [0, 0, 0]
        pix = imgGrab.load()

        result = np.zeros((540, 960, 3), dtype = "uint8")
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
            print(str(x) + ", " + str(y))
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
    img_map_pix = Image.open('result_test_2.jpg')
    for task in tasks:
        destination = task[1]
        
        img_map = np.array(img_map_pix)
        img=Image.fromarray(img_map)
        img.save('before_run.png')
        pix_map = img_map_pix.load()

        imgGrab = ImageGrab.grab(bbox=(0,0,1920,1080))
        img = np.array(imgGrab)
        img[467:655, 836:984] = [0, 0, 0]
        img[504:553, 1055:1216] = [0, 0, 0]
        img[560:600, 628:837] = [0, 0, 0]
        
        colors = [(198, 17, 17), (228, 132, 10), (101, 7, 46), (149, 202, 220)]
        
        x = 0
        y = 0

        for color in colors:
            Y,X = np.where(np.all(img==color, axis=2))
            for i in range(len(X)):
                xt = int(X[i]/2)
                yt = int(Y[i]/2)
                print(str(xt) + ", " + str(yt))
                if pix_map[xt, yt] > (210, 210, 210):
                    x = xt
                    y = yt
                    img_map[y, x] = [198, 17, 17]
                    break
        
        if x == 0:
            print("Can't find")
            
            return

        print(pix_map[x, y])
        print(str(x) + ", " + str(y))

        path, directions = search((x, y), destination, img_map, pix_map)

        for i in path:
            img_map[i[1], i[0]] = (0, 255, 0)

        navigate(path, directions, img_map, destination)

    

def navigate(path, directions, img_map, destination):
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

    print(turns)

    dir = None
    while len(turns) > 0:
        img_map = img_map_org
        img, pix = get_screen()

        Y,X = np.where(np.all(img==marker, axis=2))
        if len(X) == 0:
            Y,X = np.where(np.all(img==marker_arrived, axis=2))
        x = 0
        y = 0

        for i in range(len(X)):
            x += int(X[i]/2)
            y += int(Y[i]/2)
        x = int(x/len(X))-10
        y = int(y/len(Y))+10
        p = 15
            
        img_map[y-p:y+p, x-p:x+p] = [198, 17, 17]

        pixel = Image.fromarray(img_map, 'RGB').load()
        #print(pixel[(turns[0][0][0]), (turns[0][0][1])])

        if pixel[destination] == (198,17,17):
            print("Arrived")
            if dir is not None:
                pyautogui.keyUp(pyautogui_directions[dir])
            break

        elif pixel[(turns[0][0][0]), (turns[0][0][1])] == (198, 17, 17) or dir is None:
            print("at node")
            if dir != None:
                pyautogui.keyUp(pyautogui_directions[dir])
            dir = turns[0][1]
            turns.pop(0) 
                    
        pyautogui.keyDown(pyautogui_directions[dir])

        cv2.imshow("result", img_map)
        cv2.waitKey(1)
    cv2.destroyAllWindows()    

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
        
        print(current)
        path.append(current)
        if current in surroundings:
            directions.append(surroundings.index(current))
        array[current[1], current[0]] = (255, 255, 0)
        img=Image.fromarray(array)
        pix = img.load()
    for p in path:
        array[p[1], p[0]] = (0, 255, 0)
    img=Image.fromarray(array)
    img.save('image.png')
    return path, directions
   

def find_path(current_pos, pix, destination):
    print(current_pos)
    dir = None
    path = []
    nodes = []
    directions = []
    while True:
        prior = current_pos
        possible = [(current_pos[0]-1, current_pos[1]), 
                    (current_pos[0]+1, current_pos[1]), 
                    (current_pos[0], current_pos[1]-1), 
                    (current_pos[0], current_pos[1]+1)]

        if len(path) > 3 and path[-1] == path[-3]:
            print(current_pos)
            print(pix[437, 450])
            print(pix[437, 448])
            print(pix[438, 449])
            print(pix[436, 449])

            break
        
        if dir != None:
            pix[current_pos] = (0, 0, 0)

        # If current position is destination
        if current_pos == destination:
            print("ARRIVED!")
            break

        # If just started or can't keep going straight
        elif (dir == None) or ((dir != None) and (pix[possible[dir]] < (10, 10, 10))):
            white_counter = 0
            
            for moves in possible:
                #print(pix[moves])
                if pix[moves] >= (210, 210, 210):
                    dir = possible.index(moves)
                    current_pos = moves
                    white_counter +=1
            
            print(white_counter)
            
            # All sides are black
            if white_counter == 0:
                if len(nodes) != 0:
                    node_index = path.index(nodes[-1])
                    path = path[:node_index+1]
                    directions = directions[:node_index+1]
                    current_pos = path[-1]
                else:
                    print("END")
                    break
            
            # 2 or 1 black square
            elif white_counter == 3:
                nodes.append(prior)
                print("EC Node: " + str(prior) + " " + str(white_counter))
            path.append(current_pos)
            directions.append(dir)
                   
        #keep going straight
        else:
            white_counter = 0
            directions.append(dir)
            for moves in possible:
                if pix[moves] >= (210, 210, 210):
                    white_counter += 1
            
            if white_counter >= 2:
                nodes.append(current_pos)
                print("WC Node: " + str(current_pos))

            #pix[current_pos] = (0, 0, 0)
            current_pos = possible[dir]
            path.append(current_pos)
        print(current_pos)

    return path, directions
