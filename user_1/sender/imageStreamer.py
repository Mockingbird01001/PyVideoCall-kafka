# -*- coding: utf-8 -*-
# @Author: mockingbird
# @Date:   2022-12-01 15:15:15
# @Last Modified by:   BOUFALA Yacine
# @Last Modified time: 2022-12-02 03:02:51


import cv2
from producter import Producer


class ImageStream :
    
    def __init__(self):
        self.topic = "ImageFlux"
        self.video = cv2.VideoCapture(0)
        self.IS_ACTIVE = True
        

    def stop_stream(self):
        self.IS_ACTIVE = False
        self.video.release()


    def send_image_stream(self):
        try:
            
            while self.IS_ACTIVE:
                try:
                    ret, im = self.video.read()
                    frame = cv2.resize(im, (500, 500))
                    frame = cv2.flip(frame, 1)
                    frame_bytes = cv2.imencode(".jpeg", frame)[1].tobytes()
                    Producer(topic=self.topic).runProducer(frame_bytes)
                except:
                    self.stop_stream()
                    raise Exception("Stream is not active !")
        except:
            exit(0)