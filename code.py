# importing files 
import cv2
import numpy as np
import time
from matplotlib.pyplot import axis


fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi' , fourcc , 20.0 , (640 , 500))
cap = cv2.VideoCapture(0)

time.sleep(2)
bg = 0

for i in range(0,60):
    ret , bg = cap.read()

bg = np.flip(bg , axis = 1)

while(cap.isOpened()):
    ret , img = cap.read()
    if not ret :
        break
    img = np.flip(img , axis = 1)
    hsv = cv2.cvtColor(img , cv2.  COLOR_BGR2HSV)

    upper_black = np.array([104 , 153 , 70])
    lower_black = np.array([30 ,30 , 0])
    mask = cv2.inRange(hsv , upper_black , lower_black)
    res = cv2.bitwise_and(hsv , hsv , mask = mask)

    f = cv2.addWeighted(res , 1 , 1 , 0)
    output_file.write(f)
    cv2.imshow('magic' , f)
    cv2.waitKey(1)

    if f==0:
        np.where(img)
    
    if 'esc' or 'g':
        break 








