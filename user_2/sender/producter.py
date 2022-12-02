# -*- coding: utf-8 -*-
# @Author: BOUFALA Yacine
# @Date:   2022-11-24 17:54:57
# @Last Modified by:   BOUFALA Yacine
# @Last Modified time: 2022-12-02 16:11:34


from datetime import datetime
from pykafka import KafkaClient
from pykafka.exceptions import SocketDisconnectedError, LeaderNotAvailable
import cv2
import pyaudio as pyu

class Producer:


    def __init__(self, topic, host="192.168.111.200:9092"):
        self.KAFKA_TOPIC = topic
        self.client = KafkaClient(hosts=host) 
        self.CHUNK = 2048
        self.FORMAT = pyu.paFloat32
        self.CHANNELS = 1
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


    def runAudioProducer(self):
        with self.client.topics[self.KAFKA_TOPIC].get_producer( min_queued_messages=1, max_queued_messages=1, delivery_reports=True ) as producer:
            try:
            
                while self.stream.is_active():

                    try:
                            
                        try:
                            partition_key = str.encode(str(datetime.now()))
                            
                            frame_to_send = self.stream.read(self.CHUNK)

                            producer.produce(frame_to_send , partition_key=partition_key)

                            msg, exc = producer.get_delivery_report(block=True)

                            if exc is not None:
                                print(f"Failed to deliver msg {msg.partition_key}: {repr(exc)}")
                            else:
                                print(f"Successfully delivered msg {msg.partition_key} topic {self.KAFKA_TOPIC}")

                        except:
                            self.closeAudio()
                            raise Exception("Stream is not active !")

                    except:
                        print("An error occurred while processing.")
                        
            except (SocketDisconnectedError, LeaderNotAvailable):
                print("Reconnecting...")
                exit(0)


    def closeAudio(self):
        self.stream.close()
        self.audio.terminate()   


    def runImageProducer(self, is_active=True): 
        video = cv2.VideoCapture(0)

        with self.client.topics[self.KAFKA_TOPIC].get_producer( min_queued_messages=1, max_queued_messages=1, delivery_reports=True ) as producer:
            try:
            
                while is_active:

                    try:
                            
                        try:
                            partition_key = str.encode(str(datetime.now()))
                            
                            rem, im = video.read()
                            frame = cv2.resize(im, (500, 500))
                            frame = cv2.flip(frame, 1)
                            frame_to_send = cv2.imencode(".png", frame)[1].tobytes()
                            producer.produce(frame_to_send , partition_key=partition_key)

                            msg, exc = producer.get_delivery_report(block=True)

                            if exc is not None:
                                print(f"Failed to deliver msg {msg.partition_key}: {repr(exc)}")
                            else:
                                print(f"Successfully delivered msg {msg.partition_key} topic {self.KAFKA_TOPIC}")

                        except:
                            self.IS_ACTIVE = False
                            self.video.release()
                            raise Exception("Stream is not active !")

                    except:
                        print("An error occurred while processing.")
                        
            except (SocketDisconnectedError, LeaderNotAvailable):
                print("Reconnecting...")
                exit(0)