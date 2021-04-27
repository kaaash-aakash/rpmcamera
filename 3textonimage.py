import numpy as np
import cv2 as cv

file_path = r"res/fidget.mp4"
file_path = r"res/fan30fpsAniketMobile.mp4"

cap = cv.VideoCapture(file_path)

i = 1
while True:
    isTrue, frame = cap.read()

    cv.putText(frame, str(i), (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)

    cv.imshow("video", frame)
    i +=1
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    print(i)

print(i)
cap.release()
cv.destroyAllWindows()

# fidget.mp4 showing 14249 frames