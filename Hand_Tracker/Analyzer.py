import cv2
import tensorflow as tf

from HandTrackingModule import HandDetector

hand_detector = HandDetector()
cap = cv2.VideoCapture(0)
classifier = tf.keras.models.load_model('./Model/Classifier.h5')
MIN_TRACK_CON = 0.9

while True:
    success, img = cap.read()
    lms = hand_detector.get_landmarks(img)
    to_print = "None"
    if lms == "No Hand Tracked":
        print(lms)
    else:
        pred = (classifier.predict(lms))
        if pred < (1 - MIN_TRACK_CON):
            to_print = "Paper"
        elif pred > MIN_TRACK_CON:
            to_print = "Stone"

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
