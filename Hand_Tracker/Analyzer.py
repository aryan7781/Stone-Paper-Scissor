import cv2
import tensorflow as tf
import numpy as np

from HandTrackingModule import HandDetector

hand_detector = HandDetector()
cap = cv2.VideoCapture(0)
classifier = tf.keras.models.load_model('E:\Coding\Projects\Stone Paper Scissor\Stone-Paper-Scissor\Hand_Tracker\Model\Classifier.h5')
MIN_TRACK_CON = 0.9

while True:
    success, img = cap.read()
    # lms = hand_detector.get_landmarks(img)
    # to_print = "None"
    # if lms == "No Hand Tracked":
    #     print(lms)
    # else:
    #     pred = np.argmax((classifier.predict(lms)), axis = -1)
    #     if pred == 0:
    #         to_print = "Paper"
    #     elif pred == 1:
    #         to_print = "Scissor"
    #     elif pred == 2:
    #         to_print = "Stone"
    to_print = hand_detector.get_result_as_dict(img, classifier)
    # print(to_print)
    cv2.putText(
        img,
        f'{to_print}',
        (20, 70),
        cv2.FONT_HERSHEY_PLAIN,
        3,
        (0, 0, 0),
        3
    )

    cv2.imshow("Analyze", img)
    cv2.waitKey(1)

cv2.destroyAllWindows()
