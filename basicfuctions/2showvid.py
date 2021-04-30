import numpy as np
import cv2 as cv

file_path = r"res/fidget.mp4"
# file_path = r"res/fan30fpsAniketMobile.mp4"

cap = cv.VideoCapture(file_path)


while True:
    isTrue, frame = cap.read()

    cv.imshow("video", frame)

    if cv.waitKey(40) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
