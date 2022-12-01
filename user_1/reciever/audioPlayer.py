# -*- coding: utf-8 -*-
# @Author: BOUFALA Yacine
# @Date:   2022-11-25 14:34:37
# @Last Modified by:   mockingbird
# @Last Modified time: 2022-12-01 16:20:38


import pyaudio as pyu


class AudioPlayer :

	def __init__(self):
		self.RATE = 4100
		self.CHUNK = 2024
		self.CHANNELS = 1
		self.OUTPUT = True
		self.audio = pyaudio.PyAudio()
		self.FORMAT = pyaudio.paFloat32
		self.stream = audio.open(format=FORMAT, 
								 channels=CHANNELS, 
								 rate=RATE, 
								 output = OUTPUT, 
								 frames_per_buffer=CHUNK)


	def bytes2Audio(self, data):
		try:
            while self.stream.is_active():
                stream.write(data)
        except:
            print("An error occurred while sending audio stream.")
            self.close()
        finally:
            self.close()


	def stop_stream(self):
        self.stream.stop_stream()


    def close(self):
        self.stream.close()
        self.pyu.terminate()