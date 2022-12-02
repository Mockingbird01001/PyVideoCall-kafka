# -*- coding: utf-8 -*-
# @Author: BOUFALA Yacine
# @Date:   2022-11-25 14:37:00
# @Last Modified by:   BOUFALA Yacine
# @Last Modified time: 2022-12-02 02:57:36


from imageStreamer import ImageStream
from audioStreamer import AudioStream
from multiprocessing import Process
from time import sleep

def initAudio():
    AudioStream().send_audio_stream()


def initVideo():
    ImageStream().send_image_stream()


if __name__ == '__main__':
    # audio = Process( target =  initAudio)  
    # audio.start()

    video = Process( target = initVideo)   
    video.start()
    
