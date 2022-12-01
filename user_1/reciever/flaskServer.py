# -*- coding: utf-8 -*-
# @Author: mockingbird
# @Date:   2022-12-01 15:57:25
# @Last Modified by:   mockingbird
# @Last Modified time: 2022-12-01 16:37:04

from flask import Flask , Response, render_template , request 
from imagePlayer import ImagePlayer
from audioPlayer import AudioPlayer
from threading import Thread


status = False
app = Flask(__name__)
consumer = Consumer()


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route('/buttons',methods=['POST'])
def buttons ():
    if request.form.get('Camera Off') == 'Off':
        status = False
        stopAll()
        
    if request.form.get('Camera On') == 'On':
        status = True

    return render_template('index.html')


async def stopAll():
    end_audio = Thread(target=stopAudio, args=(,))
    end_video = Thread(target=stopVidio, args=(,))
    end_audio.start()
    end_video.start()


async def stopAudio():
    try:
        consumer.stop_audio_stream()
    except: 
        print('already closed !')

async def stopVidio():
    try:
        consumer.stop_vidio_stream()
    except: 
        print('already closed !')

async def startAudio():
    if status:
    	try:
            consumer.runAudioConsumer()
        finally:
            stopAudio()
    else: 
        pass


async def startVideo():
    if status:
        try:
            consumer.runVideoConsumer()
        finally:
            stopVidio()
    else: 
        pass


@app.route('/video_feed')
def video_feed():
	# activer le flux de la webcam
	startAudio()
	# mixed-replace permet de remplacer la frame precedente par la suivante 
    return Response(startVideo(), mimetype='multipart/x-mixed-replace; boundary=frame') 

    
if __name__ == "__main__":
    app.debug = True
    app.run(host='localhost', port=9874)