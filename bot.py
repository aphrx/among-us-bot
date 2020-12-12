import time
from PIL import ImageGrab
import numpy as np
import cv2
import pyautogui
import pytesseract
import navigate
import tasks
from pytesseract import Output

tasks_loc = [
        ["Align Engine (Upper Engine)", (273, 355)],#
        ["Align Engine (Lower Engine)", (275, 854)],#

        ["Calibrate Distributor", (817, 643)],#

        ["Chart Course", (1796, 432)],#

        ["Clean O2 Filter", (1293, 460)],#

        ["Clear Asteroids", (1430, 262)],#

        ["Divert Power", (690, 635)], #
        ["Accept Power (Communications)", (1310, 914)],#
        ["Accept Power (Lower Engine)", (322, 717)],#
        ["Accept Power (Upper Engine)", (352, 209)],#
        ["Accept Power (Navigation)", (1712, 437)],#
        ["Accept Power (O2)", (1400, 441)],#
        ["Accept Power (Security)", (562, 462)],#
        ["Accept Power (Shields)", (1496, 763)],#
        ["Accept Power (Weapons)", (1525, 252)],#

        ["Empty Garbage/Chute (Cafeteria)", (1241, 176)],#
        ["Empty Garbage/Chute (O2)", (1260, 473)],#
        ["Empty Garbage/Chute (Storage)", (1092, 1020)],#

        ["Fix Wires (Electrical)", (742, 651)], #
        ["Fix Wires (Storage)", (978, 696)],#
        ["Fix Wires (Security)", (422, 528)],#
        ["Fix Wires (Navigation)", (832, 241)],
        ["Fix Wires (Admin)", (1114, 599)],#
        ["Fix Wires (Cafeteria)", (841, 124)],#

        ["Fuel Engine (Storage)", (941, 906)],#
        ["Fuel Engine (Lower Engine)", (308, 852)],#
        ["Fuel Engine (Upper Engine)", (308, 350)],#

        ["Inspect Sample", (808, 513)], #

        ["Prime Shields", (1367, 910)],#

        ["Stabilize Steering", (1824, 532)],#

        ["Start Reactor", (166, 565)],#

        ["Submit Scan", (757, 552)],#

        ["Swipe Card", (1289, 691)], #Changed

        ["Unlock Manifolds", (135, 440)],#
        
        ["Download/Upload (Cafeteria)", (1200, 137)],#
        ["Download/Upload (Admin)", (1160, 593)],#
        ["Download/Upload (Communications)", (1215, 908)], #changed
        ["Download/Upload (Electrical)", (655, 585)], #
        ["Download/Upload (Navigation)", (1752, 438)],#
        ["Download/Upload (Weapons)", (1413, 177)]] #

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
            navigate.pathfinding()

    def startup(self):
        self.scale_percent = 100 # percent of original size
        self.width = int(1920 * self.scale_percent / 100)
        self.height = int(1080 * self.scale_percent / 100)
        self.dim = (self.width, self.height)
        self.select_screen()
        self.read_map()

    def read_map(self):
        pyautogui.press("tab")
        img = ImageGrab.grab(bbox=(0,0 ,1920,1080))
        pix = img.load()
        task = None
        for t in tasks_loc:
            if pix[t[1]] > (190, 190, 0) and pix[t[1]] < (255, 255, 80) and pix[t[1]][2] < 200:
                print(t[0])
                print(pix[t[1]])
                task = t
        
        navigate.pathfinding(tasks_loc.index(task))

    def select_screen(self):
        pyautogui.click(int(self.width/2), int(self.height/2))
    
bot = Bot()
bot.menu()