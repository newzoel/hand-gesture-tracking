import glob
import os

import cv2
import mediapipe as mp


def handTrackingImage(path):

    mpHands = mp.solutions.hands
    hand = mpHands.Hands(min_tracking_confidence=0.8)
    mpDraw = mp.solutions.drawing_utils

    # check if the path is dir or image file
    if(os.path.isdir(path)):
        path = os.path.normpath(path)
        png = glob.glob(path+'\*.png')
        jpg = glob.glob(path+'\*.jpg')
        jpeg = glob.glob(path+"\*.jpeg")

        image = png + jpg + jpeg
        print(image)

        for x in image:
            cap = cv2.imread(x)
            print(x)

            result = hand.process(cv2.cvtColor(cap, cv2.COLOR_BGR2RGB))
            print(result.multi_handedness)
            print(result.multi_hand_landmarks)


            if result.multi_hand_landmarks:
                for handLandmark in result.multi_hand_landmarks:
                    mpDraw.draw_landmarks(cap, handLandmark, mpHands.HAND_CONNECTIONS)

            cv2.imshow('result', cap)
            cv2.waitKey(1000)
            cv2.destroyAllWindows()

    # check if the path is dir or image file
    elif(os.path.isfile(path)):
        path = os.path.normpath(path)
        cap = cv2.imread(path)

        result = hand.process(cv2.cvtColor(cap, cv2.COLOR_BGR2RGB))
        print(result.multi_handedness)
        print(result.multi_hand_landmarks)


        if result.multi_hand_landmarks:
            for handLandmark in result.multi_hand_landmarks:
                mpDraw.draw_landmarks(cap, handLandmark, mpHands.HAND_CONNECTIONS)

        cv2.imshow('result', cap)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Either the path doesn't exist or you don't")
