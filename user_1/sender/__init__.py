# -*- coding: utf-8 -*-
# @Author: BOUFALA Yacine
# @Date:   2022-11-25 14:37:00
# @Last Modified by:   BOUFALA Yacine
# @Last Modified time: 2022-12-02 12:39:36

from producter import Producer
from multiprocessing import Process
from time import sleep


def initAudio():
    Producer(topic='AudioFlux_1').runAudioProducer()


def initVideo():
    Producer(topic='ImageFlux_1').runImageProducer()


if __name__ == '__main__':
    audio = Process( target =  initAudio)  
    audio.start() 

    video = Process( target = initVideo)   
    video.start()
    
