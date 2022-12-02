# -*- coding: utf-8 -*-
# @Author: BOUFALA Yacine
# @Date:   2022-11-24 17:54:57
# @Last Modified by:   BOUFALA Yacine
# @Last Modified time: 2022-12-02 12:08:55


# from audioPlayer import AudioPlayer
from pykafka import KafkaClient
from pykafka.common import OffsetType
from pykafka.exceptions import SocketDisconnectedError, LeaderNotAvailable
from threading import Thread
import cv2
import numpy as np 
import pyaudio as pyu 


class Consumer:
    
    def __init__(self, host="localhost:9092", audio_topic='AudioFlux_1', video_topic='ImageFlux_1'):
        self.KAFKA_ADDR = host
        self.KAFKA_AUDIO_TOPIC = audio_topic
        self.KAFKA_VIDEO_TOPIC = video_topic
        self.client = KafkaClient(hosts = self.KAFKA_ADDR)
        self.CHUNK = 2048
        self.FORMAT = pyu.paFloat32
        self.CHANNELS = 1
        self.RATE = 3200
        self.INPUT = False
        self.OUTPUT = True
        self.audio = pyu.PyAudio()
        self.stream = self.audio.open(format=self.FORMAT, 
                                      channels=self.CHANNELS, 
                                      rate=self.RATE, 
                                      input=self.INPUT, 
                                      output=self.OUTPUT,
                                      frames_per_buffer=self.CHUNK)


    def stop_audio_stream(self):
        self.stream.stop_stream()


    def runAudioConsumer(self):
        consumer = self.client.topics[self.KAFKA_AUDIO_TOPIC].get_simple_consumer(auto_offset_reset=OffsetType.LATEST, reset_offset_on_start=True)
        try:
            for message in consumer:
            
                if message is not None:
                    self.stream.write(message.value)
            
            self.stream.close()
            self.audio.terminate()
        except (SocketDisconnectedError, LeaderNotAvailable):
            print("Reconnecting...")
            consumer.close()


    def runVideoConsumer(self):
        while True:
            consumer = self.client.topics[self.KAFKA_VIDEO_TOPIC].get_simple_consumer(auto_offset_reset=OffsetType.LATEST, reset_offset_on_start=True)
            try:
                for message in consumer:
                    if message is not None:

                        bytes_array = np.fromstring(message.value, np.uint8)
                        frame_recieved = cv2.imdecode(bytes_array,cv2.IMREAD_COLOR)
                        ret, buffer = cv2.imencode('.png', frame_recieved)
                        frame = buffer.tobytes()
                        yield (b'--frame\n'
                               b'Content-Type: image/png\n\n' + frame + b'\n')

            except (SocketDisconnectedError, LeaderNotAvailable):
                print("Reconnecting...")
                consumer.close()