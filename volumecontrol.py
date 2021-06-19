import cv2
import time
import numpy as np
import math
from handLmModel import handDetector

vidObj = cv2.VideoCapture(0)
vidObj.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
vidObj.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

handlmsObj = handDetector(detectionCon=0.7)

while True:
    _,frame = vidObj.read()
    frame = handlmsObj.findHands(frame)
    lndmrks = handlmsObj.findPosition(frame,draw=False)
    if lndmrks:
        # print(lndmrks[4],lndmrks[8])

        xr1,yr1 = lndmrks[4][1],lndmrks[4][2]
        xr2,yr2 = lndmrks[8][1],lndmrks[8][2]
        cxr,cyr = (xr1+xr2)//2, (yr1+yr2)//2
        dist = math.hypot(xr2-xr1,yr2-yr1)
        print(dist)

        cv2.circle(frame,(xr1,yr1),5,(255,125,100),cv2.FILLED)
        cv2.circle(frame, (xr2, yr2), 5, (255, 125, 100), cv2.FILLED)

    cv2.imshow("stream",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()