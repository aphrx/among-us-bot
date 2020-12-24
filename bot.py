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
        ["Align Engine (Upper Engine)", (273, 355), tasks.align_engine_output],#
        ["Align Engine (Lower Engine)", (275, 854), tasks.align_engine_output],#

        ["Calibrate Distributor", (817, 643), tasks.calibrate_distributor],#

        ["Chart Course", (1796, 432), tasks.chart_course],#

        ["Clean O2 Filter", (1293, 460), tasks.clean_O2_filter],#

        ["Clear Asteroids", (1430, 262), tasks.clear_asteroids],#

        ["Divert Power", (690, 635), tasks.divert_power], #
        ["Accept Power (Communications)", (1310, 914), tasks.accept_power],#
        ["Accept Power (Lower Engine)", (322, 717), tasks.accept_power],#
        ["Accept Power (Upper Engine)", (352, 209), tasks.accept_power],#
        ["Accept Power (Navigation)", (1712, 437), tasks.accept_power],#
        ["Accept Power (O2)", (1400, 441), tasks.accept_power],#
        ["Accept Power (Security)", (562, 462), tasks.accept_power],#
        ["Accept Power (Shields)", (1496, 763), tasks.accept_power],#
        ["Accept Power (Weapons)", (1525, 252), tasks.accept_power],#

        ["Empty Garbage/Chute (Cafeteria)", (1241, 176), tasks.empty_chute],#
        ["Empty Garbage/Chute (O2)", (1260, 473), tasks.empty_chute],#
        ["Empty Garbage/Chute (Storage)", (1092, 1020), tasks.empty_chute],#

        ["Fix Wires (Electrical)", (742, 651), tasks.fix_wires], #
        ["Fix Wires (Storage)", (978, 696), tasks.fix_wires],#
        ["Fix Wires (Security)", (422, 528), tasks.fix_wires],#
        ["Fix Wires (Navigation)", (1652, 492), tasks.fix_wires],
        ["Fix Wires (Admin)", (1114, 599), tasks.fix_wires],#
        ["Fix Wires (Cafeteria)", (841, 124), tasks.fix_wires],#

        ["Fuel Engine (Storage)", (941, 906), tasks.fuel_engines],#
        ["Fuel Engine (Lower Engine)", (308, 852), tasks.fuel_engines],#
        ["Fuel Engine (Upper Engine)", (308, 350), tasks.fuel_engines],#

        ["Inspect Sample", (808, 513), tasks.inspect_sample], #

        ["Prime Shields", (1367, 910), tasks.prime_shields],#

        ["Stabilize Steering", (1824, 532), tasks.stabilize_steering],#

        ["Start Reactor", (166, 565), tasks.start_reactor],#

        ["Submit Scan", (757, 552), tasks.submit_scan],#

        ["Swipe Card", (1289, 691), tasks.swipe_card], #Changed

        ["Unlock Manifolds", (135, 440), tasks.unlock_manifold],#
        
        ["Download/Upload (Cafeteria)", (1200, 137), tasks.download_upload],#
        ["Download/Upload (Admin)", (1160, 593), tasks.download_upload],#
        ["Download/Upload (Communications)", (1215, 908), tasks.download_upload], #changed
        ["Download/Upload (Electrical)", (655, 585), tasks.download_upload], #
        ["Download/Upload (Navigation)", (1752, 438), tasks.download_upload],#
        ["Download/Upload (Weapons)", (1413, 177), tasks.download_upload]] #

class Bot:
    def __init__(self):
        self.name = "Aphrx"
        self.tasks = None

    def menu(self):
        print("What would you like to do?")
        print("[1] Run Bot")
        print("[2] Solve Tasks")
        print("[3] Navigate to Tasks")
        print("[4] Find me")

        option = int(input('options:'))

        if(option == 1):
            self.startup()
        if(option == 2):
            tasks.menu()
        if(option == 3):
            navigate.pathfinding()
        if(option == 4):
            self.find_me()

    def find_me(self):
        c = pyautogui.locateOnScreen('map_character.png', grayscale=True, confidence=.65)
        pyautogui.moveTo(c)

    def startup(self):
        time.sleep(2)
        self.scale_percent = 100 # percent of original size
        self.width = int(1920 * self.scale_percent / 100)
        self.height = int(1080 * self.scale_percent / 100)
        self.dim = (self.width, self.height)
        self.select_screen()
        self.read_map()

    def read_map(self):
        while True:
            pyautogui.press("tab")
            img = ImageGrab.grab(bbox=(0,0 ,1920,1080))
            pix = img.load()
            task = None
            for t in tasks_loc:
                if pix[t[1]] > (190, 190, 0) and pix[t[1]] < (255, 255, 80) and pix[t[1]][2] < 200 and pix[t[1]][1] != 17:
                    print(t[0])
                    print(pix[t[1]])
                    task = t
            if task is not None:
                result = navigate.pathfinding(tasks_loc.index(task))
                pyautogui.press("tab")
                if result is 1:
                    self.perform_task(task)

    def select_screen(self):
        pyautogui.click(int(self.width/2), int(self.height/2))

    def perform_task(self, task):
        if task[0] != "Unlock Manifolds":
            tasks.start_task()
        task[2]()
    
bot = Bot()
bot.menu()