# -*- coding: utf-8 -*-
# @Author: BOUFALA Yacine
# @Date:   2022-12-02 00:31:37
# @Last Modified by:   BOUFALA Yacine
# @Last Modified time: 2022-12-02 02:57:41

from consumer import Consumer

def getAudio():
	Consumer().runAudioConsumer()


def getImage():
	Consumer().runVideoConsumer()

if __name__ == '__main__':
	# getAudio()
	getImage()