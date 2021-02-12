import cv2
import sys
import numpy
import time
from app.src.services.core.config.Config import Config


class FaceDetector:

    def isUserDetected(self):
        config = Config()
        config = config.getConfig()
        config['path']
        # Loads the cascade for face detection
        cascPath = config['path'] + "/storage/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)

        # Captures the stream from laptop camera
        video_capture = cv2.VideoCapture(0)

        # Capture frame-by-frame
        ret, frame = video_capture.read()
        # Colours the image grey, so that it can be recognized by opencv
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        #User has not been detected
        if type(faces) == tuple:
            return False
        #User has been detected
        return True
