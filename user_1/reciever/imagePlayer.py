# -*- coding: utf-8 -*-
# @Author: mockingbird
# @Date:   2022-12-01 15:28:44
# @Last Modified by:   BOUFALA Yacine
# @Last Modified time: 2022-12-02 04:05:00


import numpy as np
import cv2


class ImagePlayer:


    def __init__(self):
        self.videoo = cv2.VideoCapture(0)
        self.IS_ACTIVE = True


    def stop_stream(self):
        raise Exception("Stream is not active !")


    def getFrame(self, data):
        if self.IS_ACTIVE:

            bytes_array = np.fromstring(data, np.uint8)
            frame_recieved = cv2.imdecode(bytes_array,cv2.IMREAD_COLOR)
            ret, buffer = cv2.imencode('.jpeg', frame_recieved)
            frame = buffer.tobytes()
            yield (b'--frame\n'
                   b'Content-Type: image/jpeg\n\n' + frame + b'\n')

        else :
            pass