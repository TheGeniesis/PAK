
import cv2
import sys
import numpy
import time
from app.src.services.core.config.Config import Config

class FaceDetector():

    def detect(self):
        config = Config()
        config = config.getConfig()
        config['path']
        #Loads the cascade for face detection
        cascPath = config['path'] + "/storage/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)

        #Captures the stream from laptop camera
        video_capture = cv2.VideoCapture(0)

        check_length = 10 
        start_time = time.time()

        while True:
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

            if type(faces) == tuple:
                print("User not detected")
            elif type(faces) == numpy.ndarray:
                print("User detected")
            
            current_time = time.time()
            if int(current_time - start_time) > check_length:
                break

            time.sleep(1)
