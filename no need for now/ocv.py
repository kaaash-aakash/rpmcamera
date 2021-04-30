#OpenCV basics
#image has 3 colors(RGB) and alpha - which is the degree of opacity of the image, images are generally converted to greyscale to decreases processing power used as it eliminates alpha.

import cv2
import matplotlib.pyplot as plt
import numpy as np
#img = cv2.imread('pen.jpg',cv2.IMREAD_GRAYSCALE)
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

#Writing on images and videos

#block 4
'''
img = cv2.imread('pen.jpg', cv2.IMREAD_COLOR)
cv2.line(img, (0,0), (150,150), (255,255,255), 15) #image, pt1,pt2,color, thickness in pixels, line type ,shift
cv2.rectangle(img, (15,25), (200,150), (0,255,0), 5 )
cv2.circle(img, (100,63), 55 , (0,0,255) , -1)
pts = np.array([[10,5],[20,30],[70,20], [50,10]], np.int32)#points and datatype
#pts = pts.reshape(-1,1,2)#google
cv2.polylines(img, [pts], True, (0,255,255) , 3)#img, points ,isclosed,color,thickness,linetype,shift
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'OpenCV Tuts', (0,130),font,1,(200,255,255),2,cv2.LINE_AA)#img, text, org,fontFace,fontScale,color,thickness,linetype,bottomLeftOrigin
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#block 5
'''
img = cv2.imread('pen.jpg', cv2.IMREAD_COLOR)
px = img[55,55] #color values at 55,55
img[10,10] = [255,0,0]#change color
#region of image
roi = img[100:150, 100:150] = [255,255,0]
roi2 = img[500:600,500:600]
img[0:100,0:100] = roi2 #copy pasting rois
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#block 6
'''
img1 = cv2.imread('pen.jpg')
img2 = cv2.imread('trimax.jpg')
img = img1 + img2
add = cv2.add(img1,img2) #adds all pixels color value(may increase 255;it doesn't care)
weighted = cv2.addWeighted(img1,0.6,img,0.4,0) #image then percent opaquenes and then gamma value
cv2.imshow('image',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#to check 
#resized = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
#block 8 imposing and basic threshold
'''
img1 = cv2.imread('impose1.png')
img2 = cv2.imread('impose2.png')
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# add a threshold
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('res',img1)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img2_fg',img2_fg)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#block 9 adaptive and normal thresholds



