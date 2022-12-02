# -*- coding: utf-8 -*-
# @Author: BOUFALA Yacine
# @Date:   2022-11-24 17:54:57
# @Last Modified by:   BOUFALA Yacine
# @Last Modified time: 2022-12-02 02:59:51


from datetime import datetime
from pykafka import KafkaClient
from pykafka.exceptions import SocketDisconnectedError, LeaderNotAvailable

class Producer:


    def __init__(self, topic, host="localhost:9092"):
        self.KAFKA_TOPIC = topic
        self.client = KafkaClient(hosts=host) 


    def runProducer(self, frame_to_send, is_active=True): 
        with self.client.topics[self.KAFKA_TOPIC].get_producer( min_queued_messages=1, max_queued_messages=1, delivery_reports=True ) as producer:
            try:
            
                partition_key = str.encode(str(datetime.now()))                    
                producer.produce(frame_to_send , partition_key=partition_key)
                        
            except (SocketDisconnectedError, LeaderNotAvailable):
                print("Reconnecting...")
                exit(0)