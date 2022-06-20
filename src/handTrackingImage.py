import glob
import os
import numpy as np

import cv2
import mediapipe as mp


def handTrackingImage(path):

    mpHands = mp.solutions.hands
    hand = mpHands.Hands(min_tracking_confidence=0.8)
    mpDraw = mp.solutions.drawing_utils

    # check whether the path is dir or file
    if(os.path.isdir(path)):
        path = os.path.normpath(path)
        png = glob.glob(path+'\*.png')
        jpg = glob.glob(path+'\*.jpg')
        jpeg = glob.glob(path+"\*.jpeg")

        image = png + jpg + jpeg
        print(image)

        saved_img = dict()

        for num, img in enumerate(image):
            cap = cv2.imread(img)

            result = hand.process(cv2.cvtColor(cap, cv2.COLOR_BGR2RGB))
            print(result.multi_handedness)
            print(result.multi_hand_landmarks)


            if result.multi_hand_landmarks:
                for handLandmark in result.multi_hand_landmarks:
                    mpDraw.draw_landmarks(cap, handLandmark, mpHands.HAND_CONNECTIONS)

            print(type(cap))
            print(saved_img)
            saved_img[str(num)] = cap

            cv2.imshow('result', cap)
            cv2.waitKey(1000)
            cv2.destroyAllWindows()


    # check whether the path is dir or file
    elif(os.path.isfile(path)):
        path = os.path.normpath(path)
        cap = cv2.imread(path)

        image = cv2.cvtColor(cap, cv2.COLOR_BGR2RGB)
        result = hand.process(image)
        print(result.multi_handedness)
        print(result.multi_hand_landmarks)


        if result.multi_hand_landmarks:
            for handLandmark in result.multi_hand_landmarks:
                mpDraw.draw_landmarks(cap, handLandmark, mpHands.HAND_CONNECTIONS)

        cv2.imshow('result', cap)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        saved_img = cap
        print(type(saved_img))
        print(saved_img)

    else:
        print("Either the path doesn't exist or you don't")

    return saved_img

def save(img, path=None):
    if not path:
        path = '../out/'
    else:
        if(os.path.isdir(path)):
            return
        else:
            os.makedirs(path)

    path = os.path.normpath(path)

    if(isinstance(img, dict)):
        for x, y in img.items():
            cv2.imwrite(path+'/out{}.png'.format(x), y)

    else:
        cv2.imwrite(path, img)
