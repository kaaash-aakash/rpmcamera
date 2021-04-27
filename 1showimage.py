import numpy as np
import cv2 as cv

file_path = r"res/averaged_frame.jpg"

img = cv.imread(file_path, 1)
cv.imshow('image', img)
cv.waitKey(0)

cv.destroyAllWindows()
