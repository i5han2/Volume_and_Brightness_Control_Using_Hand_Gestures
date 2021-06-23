import cv2
from handLmModel import handDetector



def main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    detector = handDetector()

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    siz = (frame_width, frame_height)

    # Below VideoWriter object will create
    # a frame of above defined The output
    # is stored in 'filename.avi' file.
    res = cv2.VideoWriter('demo.avi',
                             cv2.VideoWriter_fourcc(*'MJPG'),
                             10, siz)

    while True:
        success, img = cap.read()
        img = cv2.flip(img,1)
        img = detector.findHands(img)
        lmList = detector.findPosition(img,draw=False)
        if len(lmList) != 0:
            print(lmList)

            if lmList[0] == 'both':
                cv2.putText(img,'Right',(lmList[1][0][1],lmList[1][0][2]), cv2.FONT_HERSHEY_PLAIN, 3,(255, 25, 0), 3)
                cv2.putText(img, 'Left', (lmList[2][0][1], lmList[2][0][2]), cv2.FONT_HERSHEY_PLAIN, 3,(0, 25, 255), 3)
            elif lmList[0] == 'Left':
                cv2.putText(img, 'Left', (lmList[1][0][1], lmList[1][0][2]), cv2.FONT_HERSHEY_PLAIN, 3,
                            (0, 25, 255), 3)
            elif lmList[0] == 'Right':
                cv2.putText(img, 'Right', (lmList[1][0][1], lmList[1][0][2]), cv2.FONT_HERSHEY_PLAIN, 3,
                            (255, 25, 0), 3)

        cv2.imshow("Image", img)
        res.write(img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()