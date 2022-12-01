# -*- coding: utf-8 -*-
# @Author: BOUFALA Yacine
# @Date:   2022-11-25 12:58:59
# @Last Modified by:   mockingbird
# @Last Modified time: 2022-12-01 15:32:28

import numpy as np
import pyaudio as pyu
from producter import Producer


class AudioStream :

    def __init__(self):
        self.audioTopic = 'audioFlux'
        self.CHUNK = 1024
        self.FORMAT = pyu.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.audio = pyu.PyAudio()
        self.stream = self.audio.open(format=self.FORMAT, 
                                      channels=self.CHANNELS, 
                                      rate=self.RATE, 
                                      input=True, 
                                      frames_per_buffer=self.CHUNK)

    async def stop_stream(self):
        self.stream.stop_stream()


    def send_audio_stream(self):
        try:
            while self.stream.is_active():
                Producer(self.audioTopic).runProducer(self.stream.read(self.CHUNK))
        except:
            print("An error occurred while sending audio stream.")
            self.close()
        finally:
            self.close()


    def close(self):
        self.stream.close()
        self.pyu.terminate()