# -*- coding: utf-8 -*-
# @Author: BOUFALA Yacine
# @Date:   2022-11-24 17:54:57
# @Last Modified by:   BOUFALA Yacine
# @Last Modified time: 2022-11-25 14:41:57

from threading import Thread
from datetime import datetime
from pykafka import KafkaClient
from pykafka.exceptions import SocketDisconnectedError, LeaderNotAvailable

class Producer:


    def __init__(self):
        self.KAFKA_ADDR = "localhost:9092"
        self.KAFKA_TOPIC = "myTopic"
        self.client = KafkaClient(hosts=self.KAFKA_ADDR, ) 
        self.topic = self.client.topics[self.KAFKA_TOPIC]


    def runProducer(self, frame_to_send, is_active=True): 
        with self.topic.get_producer( min_queued_messages=1, max_queued_messages=1, delivery_reports=True ) as producer:
            try:
                while is_active:
                    try:
                        partition_key = str.encode(str(datetime.now()))
                        
                        producer.produce(frame_to_send , partition_key=partition_key)
                        
                        msg, exc = producer.get_delivery_report(block=True)

                        if exc is not None:
                            print(f"Failed to deliver msg {msg.partition_key}: {repr(exc)}")
                        else:
                            print(f"Successfully delivered msg {msg.partition_key}")
                    except:
                        print("An error occurred while processing.")
                        
                print("waiting for all messages to be written")
                producer._wait_all()

            except (SocketDisconnectedError, LeaderNotAvailable):
                print("Reconnecting...")