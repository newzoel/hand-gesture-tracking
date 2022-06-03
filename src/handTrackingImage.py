import os

import cv2
import mediapipe as mp


def handTrackingImage(path):

    mpHands = mp.solutions.hands
    hand = mpHands.Hands(min_tracking_confidence=0.8)
    mpDraw = mp.solutions.drawing_utils
    # testDraw = mp.solutions.drawing_utils_test

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
