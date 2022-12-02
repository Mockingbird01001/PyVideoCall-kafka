# -*- coding: utf-8 -*-
# @Author: BOUFALA Yacine
# @Date:   2022-11-24 17:54:57
# @Last Modified by:   BOUFALA Yacine
# @Last Modified time: 2022-12-02 04:01:19


# from audioPlayer import AudioPlayer
from pykafka import KafkaClient
from pykafka.common import OffsetType
from pykafka.exceptions import SocketDisconnectedError, LeaderNotAvailable
from audioPlayer import AudioPlayer
from imagePlayer import ImagePlayer
from threading import Thread


class Consumer:
    
    def __init__(self, host="localhost:9092", audio_topic='AudioFlux', video_topic='ImageFlux'):
        self.KAFKA_ADDR = host
        self.KAFKA_AUDIO_TOPIC = audio_topic
        self.KAFKA_VIDEO_TOPIC = video_topic
        self.client = KafkaClient(hosts = self.KAFKA_ADDR)
        self.player = AudioPlayer()
        self.videoo = ImagePlayer()


    def stop_audio_stream(self):
        self.player.stop_stream()


    def stop_vidio_stream(self):
        self.videoo.stop_stream()


    def runAudioConsumer(self):
        consumer = self.client.topics[self.KAFKA_AUDIO_TOPIC].get_simple_consumer(auto_offset_reset=OffsetType.LATEST, reset_offset_on_start=True)
        try:
            for message in consumer:
                if message is not None:
                    self.player.stream.write(message.value)

        except (SocketDisconnectedError, LeaderNotAvailable):
            print("Reconnecting...")
            consumer.close()


    def runVideoConsumer(self):
        consumer = self.client.topics[self.KAFKA_VIDEO_TOPIC].get_simple_consumer(auto_offset_reset=OffsetType.LATEST, reset_offset_on_start=True)
        try:
            for message in consumer:
                if message is not None:
                    self.videoo.getFrame(message.value)

        except (SocketDisconnectedError, LeaderNotAvailable):
            print("Reconnecting...")
            consumer.close()