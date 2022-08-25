#this is a screen recoder using python
# we are gonna take a screenshot for every millisecond and then merge them all together
#importing the modules 
import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time
#captures the entire screen  and we can even give the custom dimensions 
width=GetSystemMetrics(0)
height=GetSystemMetrics(1)

dim=(width,height)
#format of the mp4 file
f=cv2.VideoWriter_fourcc(*"XVID")
#location of the file  and name  and dimensions
output=cv2.VideoWriter("test.mp4",f,30.0,dim)
#Timings ie the start time and end time 
now_start_time=time.time()
#duration , we add plus 4 seconds so that the code gets compiled
dur=10+4
end_time=now_start_time+dur
#capturing the viedo 
while True:
    img=pyautogui.screenshot()
    frame_1=np.array(img)
    frame_2=cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)



