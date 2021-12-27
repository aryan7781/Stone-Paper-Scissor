import cv2
import tensorflow as tf

from HandTrackingModule import HandDetector

hand_detector = HandDetector()
cap = cv2.VideoCapture(0)
classifier = tf.keras.models.load_model('./Model/Classifier.h5')

while True:
    success, img = cap.read()
    lms = hand_detector.get_landmarks(img)
    if lms == "No Hand Tracked":
        print(lms)
    else:
        print(classifier.predict(lms))

    cv2.imshow("Analyze", img)
    cv2.waitKey(1)

cv2.destroyAllWindows()
