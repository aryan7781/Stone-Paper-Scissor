import mediapipe as mp
import cv2
import time
import pandas as pd

from HandTrackingModule import HandDetector

hand_detector = HandDetector()
hand_detector.collect_landmarks(
    'Thumbs_Up',
    'Thumbs_Up.csv'
)