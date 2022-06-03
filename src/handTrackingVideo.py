import cv2
import mediapipe as mp

# if the input is webcam/camera, pass '0' to parameter instead of video file
# cap = cv2.VideoCapture('data/hand_tracking.mov')
# cap = cv2.VideoCapture(0)
# cap = cv2.imread('data/kovacic_celebration.jpg')
# cap = cv2.VideoCapture('data/kovacic_celebration.jpg')

mpHands = mp.solutions.hands
hand = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

#check if video/camera is captured
while(cap.isOpened()):
    ret, frame = cap.read()
    width = cap.get(3)  # float `width`
    height = cap.get(4)  # float `height`
    frame = cv2.resize(frame, (int(width/3), int(height/4)))
    print(frame.shape)


    imgRgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hand.process(imgRgb)
    #print(result.multi_hand_landmarks)

    if result.multi_hand_landmarks:
        for handLandmark in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, handLandmark, mpHands.HAND_CONNECTIONS)

    if ret == True:

        #display the captured video/camera
        cv2.imshow('Frame', frame)

        #press Q on keyboard to exit display
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    #break the loop
    else:
        break

#when the captured video is unused, release to remove
cap.release()
#close all the frames
cv2.destroyAllWindows()