# -*- coding: utf-8 -*-
# @Author: BOUFALA Yacine
# @Date:   2022-11-25 14:34:37
# @Last Modified by:   BOUFALA Yacine
# @Last Modified time: 2022-12-02 02:55:30


import pyaudio as pyu


class AudioPlayer :

    def __init__(self):
        self.CHUNK = 2048
        self.FORMAT = pyu.paFloat32
        self.CHANNELS = 2
        self.RATE = 4100
        self.INPUT = False
        self.OUTPUT = True
        self.audio = pyu.PyAudio()
        self.stream = self.audio.open(format=self.FORMAT, 
                                      channels=self.CHANNELS, 
                                      rate=self.RATE, 
                                      input=self.INPUT, 
                                      output=self.OUTPUT,
                                      frames_per_buffer=self.CHUNK)


    def stop_stream(self):
        self.stream.stop_stream()


    def close(self):
        self.stream.close()
        self.audio.terminate()