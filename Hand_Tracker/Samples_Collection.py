import mediapipe as mp
import cv2
import time
import pandas as pd

from HandTrackingModule import HandDetector

hand_detector = HandDetector()
NUM_SAMPLES = 10000

# # Collecting Landmarks For Stone
# hand_detector.collect_landmarks(
#     'Stone',
#     './Landmarks/Stone.csv',
#     num_samples= NUM_SAMPLES
# )
# time.sleep(5)

# # Collecting Landmarks For Paper
# hand_detector.collect_landmarks(
#     'Paper',
#     './Landmarks/Paper.csv',
#     num_samples=NUM_SAMPLES
# )
# time.sleep(5)


# Collecting Landmarks For Scissors
hand_detector.collect_landmarks(
    'Scissor',
    './Landmarks/Scissor.csv',
    num_samples=NUM_SAMPLES
)
time.sleep(5)

# # Collecting Landmarks For Scissors
# hand_detector.collect_landmarks(
#     'Scissor',
#     './Landmarks/Scissor.csv',
#     num_samples=NUM_SAMPLES
# )