# -*- coding: utf-8 -*-
# @Author: BOUFALA Yacine
# @Date:   2022-11-25 14:37:00
# @Last Modified by:   mockingbird
# @Last Modified time: 2022-12-01 15:56:09


from imageStreamer import ImageStream
from audioStreamer import AudioStream
from threading import Thread

def initStream():
	audio = Thread(target=AudioStream().send_audio_stream(), args=(,))	
	video = Thread(target=ImageStream().send_image_stream(), args=(,))	
	audio.start()
	video.start()


if __name__ == "__main__":
	# send video stream
	initStream()