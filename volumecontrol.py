import cv2
import time
import numpy as np

vidObj = cv2.VideoCapture(0)
vidObj.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
vidObj.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

while True:
    _,frame = vidObj.read()
    cv2.imshow("stream",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
