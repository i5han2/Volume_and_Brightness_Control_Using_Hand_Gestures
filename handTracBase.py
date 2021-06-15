import cv2
import mediapipe

vidObj = cv2.VideoCapture(0)

mpHands = mediapipe.solutions.hands
hands = mpHands.Hands()
mpDraw = mediapipe.solutions.drawing_utils

while True:
    _,cap = vidObj.read()
    rgb = cv2.cvtColor(cap,cv2.COLOR_BGR2RGB)
    res = hands.process(rgb)
    if res.multi_hand_landmarks:
        for handLndMarks in res.multi_hand_landmarks:
            mpDraw.draw_landmarks(cap,handLndMarks,mpHands.HAND_CONNECTIONS)

    cv2.imshow("video",cap)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()