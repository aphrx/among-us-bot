import time
from PIL import ImageGrab
import numpy as np
import cv2

class Bot:
    def __init__(self):
        self.name = "Aphrx"

    def startup(self):
        self.buffer(10)

    def getVideo(self):

    def buffer(self, timer):
        for i in range(timer):
            print(self.name + " will start in " + str(timer-i))
            time.sleep(1)
        
    
bot = Bot()
bot.startup()