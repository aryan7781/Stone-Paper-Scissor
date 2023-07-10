import time

from HandTrackingModule import HandDetector

hand_detector = HandDetector()
NUM_SAMPLES = 10000


hand_detector.collect_landmarks(
    'Scissor',
    './Landmarks/Scissor.csv',
    num_samples=NUM_SAMPLES
)
time.sleep(5)
