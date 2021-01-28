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
        # Loads the cascade for face detection
        cascPath = config['path'] + "/storage/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)

        # Captures the stream from laptop camera
        video_capture = cv2.VideoCapture(0)
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
                return False
            elif type(faces) == numpy.ndarray:
                print("User detected")
                return True


            time.sleep(1)

    
    def time_difference(check_length):
        start_time = time.time()
        sound = "dzwonek.mp3"
        while True:
            if FaceDetect.isUserDetected():
                start_time = time.time()
            else:
                current_time = time.time()
                time_difference = int(current_time - start_time)
                print(time_difference)
                if time_difference >= check_length:
                    print("Brawo! Udało Ci się wykonać ćwiczenie!")
                    playsound(sound)
                    break
    def check_user(check_length):
        lista = []
        for i in range(5):
            lista.append(FaceDetect.isUserDetected())
        if sum(lista) == 0:
            print("rozpoczynam sprawdzanie")
            start_time = time.time()
            sound = "dzwonek.mp3"
            while True:
                if FaceDetect.isUserDetected():
                    break
                else:
                    current_time = time.time()
                    time_difference = int(current_time - start_time)
                    print(time_difference)
                    if time_difference >= check_length:
                        print("czas do kolejnego ćwiczenia został zresetowany")
                        playsound(sound)
                        #tu resetujemy glowny timer
                        break
FaceDetect.check_user(5)
