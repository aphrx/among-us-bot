import time
from PIL import ImageGrab
import numpy as np
import cv2
import pyautogui
import pytesseract
import navigate
import tasks
from pytesseract import Output

class Bot:
    def __init__(self):
        self.name = "Aphrx"
        self.tasks = None

    def menu(self):
        print("What would you like to do?")
        print("[1] Run Bot")
        print("[2] Solve Tasks")
        print("[3] Navigate to Tasks")

        option = int(input('options:'))

        if(option == 1):
            self.startup()
        if(option == 2):
            tasks.menu()
        if(option == 3):
            navigate.map()

    def startup(self):
        self.scale_percent = 60 # percent of original size
        self.width = int(1920 * self.scale_percent / 100)
        self.height = int(1080 * self.scale_percent / 100)
        self.dim = (self.width, self.height)
        self.buffer(2)
        self.read_map()
        #self.getVideo()

    def read_map(self):
        task_locations = [
            #(807, 511), # Medbay: Sample
            (1290, 691) # Admin: Swipe Card
        ]
        task = (235, 221, 4)
        pyautogui.press("tab")
        img = ImageGrab.grab(bbox=(0,0 ,1920,1080))
        pix = img.load()
        
        for tasks in task_locations:
            if pix[tasks] == task:
               navigate.admin_swipe_card()

    def getVideo(self):
        pyautogui.press("tab")
        while(True):
            img = ImageGrab.grab(bbox=(0,0 ,1920,1080)) #bbox specifies specific region (bbox= x,y,width,height)
            img_np = np.array(img)
            frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            frame_r = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
            #if self.tasks is None: 
            #    self.tasks, output = self.determineTasks(frame_r)
            #else:
            #    print(self.tasks)
            frame_hsv = cv2.cvtColor(img_np, cv2.COLOR_BGR2HSV)
            frame_r_hsv = cv2.resize(frame_hsv, (0,0), fx=0.5, fy=0.5)
            self.playerLocation(frame_r_hsv)
            
        cv2.destroyAllWindows()

        
    def timedKeyPress(self, dur):
        end = time.time() + dur
        while(time.time() < end):
            pyautogui.keyDown("up")
        pyautogui.keyUp("tab")

    def determineTasks(self, img):
        self.timedKeyPress(5)
        print("Looking for tasks")
        tasks = []
        output = img.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                                param1=100, param2=30, minRadius=15, maxRadius=25)
        if circles is not None:
            detected_circles = np.uint16(np.around(circles))
            for (x, y ,r) in detected_circles[0, :]:
                print(x, y, r)
                if (x == 70 and y == 70 or x == 72 and y == 72 or x==72 and y == 70 or  x == 924 and y == 108 or x == 926 and y == 36):
                    continue
                tasks.append([x, y])
                cv2.circle(output, (x, y), r, (0, 0, 0), 3)
                cv2.circle(output, (x, y), 2, (0, 255, 255), 3)
        return tasks, output
        

    def buffer(self, timer):
        for i in range(timer):
            print(self.name + " will start in " + str(timer-i))
            time.sleep(1)
        
    
bot = Bot()
bot.menu()