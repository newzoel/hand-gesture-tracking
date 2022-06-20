import os.path

import cv2
import mediapipe as mp


def handTrackingVideo(path=None):
    # if the input is webcam/camera, pass '0' to parameter instead of video file
    if(path):
        path = os.path.normpath(path)
        cap = cv2.VideoCapture(path)
    else:
        cap = cv2.VideoCapture(0)

    mpHands = mp.solutions.hands
    hand = mpHands.Hands(min_tracking_confidence=0.8)
    mpDraw = mp.solutions.drawing_utils

    # check if video/camera is captured
    while(cap.isOpened()):
        ret, frame = cap.read()
        width = cap.get(3)  # float `width`
        height = cap.get(4)  # float `height`

        if (width > 1280 and height > 720):
            if(height > width):
                frame = cv2.resize(frame, (int(width/3), int(height/5)), interpolation=cv2.INTER_NEAREST)    #resize portrait frame
                print(frame.shape)
            else:
                frame = cv2.resize(frame, (1280, 720), interpolation=cv2.INTER_NEAREST)    #resize landscape frame
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