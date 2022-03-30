import mediapipe as mp
import cv2
import time

import numpy as np
import pandas as pd


class HandDetector():
    def __init__(self,
                 maxHands = 2,
                 detectionCon = 0.5,
                 trackCon = 0.5):

        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            min_tracking_confidence=self.trackCon,
            min_detection_confidence=self.detectionCon,
            max_num_hands=self.maxHands
        )

        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    print(id, cx, cy)

                self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
            # return results

    def collect_landmarks(self, category_of_sample = None, save_file_name:str = "Landmarks.csv", num_samples:int = 1000):
        cap = cv2.VideoCapture(0)
        lm_cols = []
        for lm_id in range(21):
            for coord in ['x', 'y']:
                lm_cols.append(f"{lm_id}_{coord}")

        if category_of_sample:
            lm_cols.append("Category")

        lms = pd.DataFrame(columns=lm_cols)
        Stime = time.time()
        pTime = 0
        while len(lms) < num_samples:
            success, img = cap.read()
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = self.hands.process(imgRGB)

            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    lm_dict = {}
                    for id, Lm in enumerate(handLms.landmark):
                        lm_dict[f"{id}_x"] = Lm.x
                        lm_dict[f"{id}_y"] = Lm.y
                    lm_dict['Category'] = category_of_sample
                    # print(lm_dict)

                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
                    lms = lms.append(lm_dict, ignore_index=True)
                    print(len(lms))

            cv2.imshow("HandTrack", img)
            pTime = time.time() - Stime
            cv2.waitKey(1)

        cv2.destroyAllWindows()
        lms.to_csv(save_file_name)

    def get_landmarks(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                lm_dict = {}
                for id, Lm in enumerate(handLms.landmark):
                    lm_dict[f"{id}_x"] = Lm.x
                    lm_dict[f"{id}_y"] = Lm.y
                    # print(lm_dict)

                #self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
                lms = pd.Series(lm_dict)
                lms = lms.to_numpy()
                lms = np.expand_dims(lms, axis = 0)
            return lms
        else:
            return "No Hand Tracked"

    def get_results(self, img, classifier):
        lms = self.get_landmarks(img)
        result = "None"
        if not (lms == "No Hand Tracked"):

            pred = np.argmax((classifier.predict(lms)), axis=-1)
            if pred == 0:
                result = "Paper"
            elif pred == 1:
                result = "Scissor"
            elif pred == 2:
                result = "Stone"

        return result

    def get_result_as_dict(self, img, classifier):
        lms = self.get_landmarks(img)
        predicted_as_dict = {"Paper": 0,"Scissor": 0, "Stone": 0}
        prediction_arr = None
        if not (lms == "No Hand Tracked"):
            prediction_arr = classifier.predict(lms)
            pred = np.argmax((prediction_arr), axis=-1)
            if(prediction_arr[0][pred] > 0.9):
                if(pred == 2):
                    predicted_as_dict['Stone'] = 1
                elif(pred == 1):
                    predicted_as_dict['Scissor'] = 1
                elif(pred == 0):
                    predicted_as_dict['Paper'] = 1

        # print(predicted_as_dict)
        # print(prediction_arr)

        return predicted_as_dict





