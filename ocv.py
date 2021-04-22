#OpenCV basics
#image has 3 colors(RGB) and alpha - which is the degree of opacity of the image, images are generally converted to greyscale to decreases processing power used as it eliminates alpha.

import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread('pen.jpg',cv2.IMREAD_GRAYSCALE)
#or ('pen.jpg',0) where 0 corresponds to grayscale
#IMREAD_COLOR - (1)
#IMREAD_UNCHANGED - (-1)

#Block 1
'''
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#showing with cv

'''
#Block 2
'''
plt.imshow(img, cmap = 'gray' , interpolation = 'bicubic') #Interpolation is a method of constructing new data points within range of discrete set of known data points.
plt.show()
'''
#cv2.imwrite('greyed.png',img) #saves image in grayscale 
# impo - cv2 does BGR while matplotlib does RGB

#Block 3
'''
cap = cv2.VideoCapture(0) #0 indicates 1st
fourcc = cv2.VideoWriter_fourcc(*'XVID') #fourcc is short for "four character code" -  an identifier for video codec
out = cv2.VideoWriter('output.avi', fourcc , 30.0 , (640,480)) #output name; FourCC code;FPS and framewidth and height
while True:
    ret , frame = cap.read() #if there's a feed you get True in ret & frame captured in frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #initialising new window while converting it to greyscale
    cv2.imshow('frame',frame)
    out.write(frame)# writing frame by frame
    cv2.imshow('grayed',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'): #0xff is hexadecimal representation
        break
cap.release() #releases camera so it's not in use nomo
out.release()
cv2.destroyAllWindows()
'''