import time
import playsound
from app.src.services.detection.FaceDetector import FaceDetector
from app.src.services.core.config.Config import Config


class MainTimer():

    def main_timer(Min, Sec=0):
        sound = "dzwonek.mp3"

        # Begin Process
        timeLoop = True
        while timeLoop:
            Sec -= 1
            if Sec == -1:
                Sec = 59
                Min -= 1
            print(str(Min) + " Mins " + str(Sec) + " Sec ")
            if Min ==0 and Sec ==0:
                #Tu trzeba wrzucić rozpoczęcie ćwiczeń oraz uruchomić funkcje "time_difference"
                print ("czas na ćwiczenia")
                playsound.playsound(sound)
                FaceDetector.time_difference(30)
                Min=0
                Sec=0           
            time.sleep(1)