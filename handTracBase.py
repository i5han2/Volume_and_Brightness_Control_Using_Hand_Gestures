import cv2
import mediapipe

vidObj = cv2.VideoCapture(0)

while True:
    _,cap = vidObj.read()
    # rgb = cv2.cvtColor(cap,cv2.COLOR_BGR2RGB)
    # res = hands.process(rgb)
    cv2.imshow("video",cap)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()