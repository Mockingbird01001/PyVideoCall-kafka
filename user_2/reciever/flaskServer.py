from flask import Flask , Response, render_template , request 
# from pykafka import KafkaClient
# from pykafka.common import OffsetType
# import numpy as np
# import cv2
from multiprocessing import Process
from consumer import Consumer

app = Flask(__name__)


def gueuller():
    return Consumer().runAudioConsumer()

def streaming():  
    return Consumer().runVideoConsumer()


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    audio = Process(target = gueuller )
    audio.start()

    return Response(streaming(), mimetype='multipart/x-mixed-replace; boundary=frame')
    
if __name__ == "__main__":
    app.debug = True
    app.run(host='localhost', port=9874)