# -*- coding: utf-8 -*-
# @Author: BOUFALA Yacine
# @Date:   2022-11-25 12:58:59
# @Last Modified by:   BOUFALA Yacine
# @Last Modified time: 2022-12-02 02:55:23

from producter import Producer
import numpy as np
import pyaudio as pyu
from time import sleep

class AudioStream :

    def __init__(self):
        self.audioTopic = 'AudioFlux'
        self.CHUNK = 2048
        self.FORMAT = pyu.paFloat32
        self.CHANNELS = 2
        self.RATE = 4100
        self.INPUT = True
        self.OUTPUT = False
        self.audio = pyu.PyAudio()
        self.stream = self.audio.open(format=self.FORMAT, 
                                      channels=self.CHANNELS, 
                                      rate=self.RATE, 
                                      input=self.INPUT, 
                                      output=self.OUTPUT,
                                      frames_per_buffer=self.CHUNK)

    def stop_stream(self):
        self.stream.stop_stream()


    def send_audio_stream(self):
        try:
            while self.stream.is_active():
                
                data = self.stream.read(self.CHUNK)
                Producer(topic=self.audioTopic).runProducer(data)

            raise Exception("Stream is not active !")
        except:
            print("An error occurred while sending audio stream.")
            self.close()
        finally:
            self.close()


    def close(self):
        self.stream.close()
        self.audio.terminate()