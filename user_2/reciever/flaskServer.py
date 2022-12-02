# -*- coding: utf-8 -*-
# @Author: BOUFALA Yacine
# @Date:   2022-11-24 17:54:57
# @Last Modified by:   BOUFALA Yacine
# @Last Modified time: 2022-12-02 15:20:39


from flask import Flask , Response, render_template , request 
from multiprocessing import Process
from consumer import Consumer

app = Flask(__name__)


def gueuller():
    return Consumer().runAudioConsumer()

def streaming():  
    return Consumer().runVideoConsumer()

def own_Streaming():
    return Consumer().runMyOwnVideoConsumer()


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    audio = Process(target = gueuller )
    audio.start()
    return Response(     streaming(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/my_own_video')
def my_own_video():
    
    return Response( own_Streaming(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.debug = True
    app.run(host='localhost', port=9874)