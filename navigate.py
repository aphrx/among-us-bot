import pyautogui
import time
import tasks
from PIL import ImageGrab, Image
import cv2
import numpy as np

marker = (198, 17, 17)
marker_arrived = (228, 132, 10)
tasks = [["Admin Swipe", (641, 337)], 
        ["Fuel Engine (Storage)", (466, 449)]]
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
    destination = tasks[1][1]
    img_map_pix = Image.open('result_test_2.jpg')

    img_map_pix = Image.open('result_test_2.jpg')
    img_map = np.array(img_map_pix)
    imgGrab = ImageGrab.grab(bbox=(0,0,1920,1080))
    img = np.array(imgGrab)
    img[467:655, 836:984] = [0, 0, 0]
    img[504:553, 1055:1216] = [0, 0, 0]
    img[560:600, 628:837] = [0, 0, 0]
    
    pix_map = img_map_pix.load()
    #Y,X = np.where(np.all(img==marker_arrived, axis=2))
    #if len(X) == 0:
    Y,X = np.where(np.all(img==marker, axis=2))
    x = 0
    y = 0

    for i in range(len(X)):
        x = int(X[i]/2)
        y = int(Y[i]/2)
        if pix_map[x, y] > (210, 210, 210):
            img_map[y, x] = [198, 17, 17]
            img_map[y-3:y+3, x-3:x+3] = [198, 17, 17]
            break

    path, directions = find_path((x, y), pix_map, destination)

    for i in path:
        img_map[i[1], i[0]] = (0, 255, 0)

    navigate(path, directions, img_map, destination)

    

def navigate(path, directions, img_map, destination):
    img_map_org = img_map
    direction = None
    turns = []
    pyautogui_directions = ["left", "right", "up", "down"]
    time.sleep(2)

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
        p = 10
            
        img_map[y-p:y+p, x-p:x+p] = [198, 17, 17]

        pixel = Image.fromarray(img_map, 'RGB').load()
        #print(pixel[(turns[0][0][0]), (turns[0][0][1])])

        if pixel[destination] == (198,17,17):
            print("Arrived")
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
        

def find_path(current_pos, pix, destination):
    print(current_pos)
    dir = None
    path = []
    nodes = []
    directions = []
    while True:
        possible = [(current_pos[0]-1, current_pos[1]), 
                    (current_pos[0]+1, current_pos[1]), 
                    (current_pos[0], current_pos[1]-1), 
                    (current_pos[0], current_pos[1]+1)]

        #for i in possible:
            #print(pix[i])
        
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
                if pix[moves] >= (210, 210, 210):
                    #print("Available move")
                    #pix[current_pos] = (0, 0, 0)
                    dir = possible.index(moves)
                    current_pos = moves
                    white_counter +=1
                #print(pix[moves])
            
            # All sides are black
            if white_counter == 0:
                if len(nodes) != 0:
                    print(nodes)
                    node_index = path.index(nodes[-1])
                    path = path[:node_index+1]
                    directions = directions[:node_index+1]
                    current_pos = path[-1]
                else:
                    print("END")
                    break
            
            # 2 or 1 black square
            elif white_counter == 3 or white_counter == 2:
                nodes.append(current_pos)
                for i in possible:
                    print(pix[i])
                print("EC Node: " + str(current_pos) + " " + str(white_counter))
            
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
                for i in possible:
                    print(pix[i])
                nodes.append(current_pos)
                print("WC Node: " + str(current_pos))

            #pix[current_pos] = (0, 0, 0)
            current_pos = possible[dir]
            path.append(current_pos)

        print(current_pos)
    return path, directions
