#this is a screen recoder using python
# we are gonna take a screenshot for every millisecond and then merge them all together

import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time
#captures the entire screen
width=GetSystemMetrics(0)
height=GetSystemMetrics(1)

dim=(width,height)
