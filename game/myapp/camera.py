import cv2
import sys
import tensorflow as tf
BASE_DIR = "../"
sys.path.insert(0, (BASE_DIR + 'Hand_Tracker'))

from HandTrackingModule import HandDetector
hand_detector = HandDetector()
classifier = tf.keras.models.load_model((BASE_DIR + "Hand_Tracker/Model/Classifier.h5"))


class VideoCamera(object):
    def __init__(self):
        self.video=cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success,image=self.video.read()
        ret,jpeg=cv2.imencode('.jpg',image)
        return jpeg.tobytes()


    def get_result(self):
        success, image = self.video.read()
        predicted_data = hand_detector.get_result_as_dict(image, classifier)
        
        return predicted_data