# -*- coding: utf-8 -*-
# @Author: mockingbird
# @Date:   2022-12-01 15:15:15
# @Last Modified by:   mockingbird
# @Last Modified time: 2022-12-01 16:01:31


import cv2
from producter import Producer


class ImageStream :
	
	def __init__(self):
		self.hosts="localhost:9092"
		self.topic = "ImageFlux"
		self.video = cv2.VideoCapture(0)
		

	async def stop_stream(self):
		 self.video.release()


	def send_image_stream(self):
        while (True):
        	try:
            	ret, im = vid.read()
            	frame = cv2.resize(im, (500, 500))
            	frame = cv2.flip(frame, 1)
            	frame_bytes = cv2.imencode(".jpeg", frame)[1].tobytes()
           		Producer(self.host, self.topic).runProducer(frame_bytes)
           	except:
           		exit(0)