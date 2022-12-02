from flask import Flask , Response, render_template , request 
from pykafka import KafkaClient
from pykafka.common import OffsetType
import numpy as np
import cv2


app = Flask(__name__)

#############################################

vid = cv2.VideoCapture(0)
client = KafkaClient(hosts="localhost:9092")
topic = client.topics[b'ImageFlux']
switch = 1
#############################################


def streaming():  
    global vid
    consumer = topic.get_simple_consumer(auto_offset_reset=OffsetType.LATEST,reset_offset_on_start=True)
    for message in consumer:
        if switch :
            nparr = np.fromstring(message.value, np.uint8)
            frame_recieved = cv2.imdecode(nparr,cv2.IMREAD_COLOR)
            ret, buffer = cv2.imencode('.jpeg', frame_recieved)
            frame = buffer.tobytes()
            yield (b'--frame\n'
                   b'Content-Type: image/jpeg\n\n' + frame + b'\n')
                #--frame
                #Content-Type: image/jpeg
                #
                #<jpeg data>
        else :
            pass


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route('/buttons',methods=['POST'])
def buttons ():
    global switch , vid
    if request.form.get('Camera Off') == 'Off':
        switch = 0
    if request.form.get('Camera On') == 'On':
        switch = 1
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    
    return Response(streaming(), mimetype='multipart/x-mixed-replace; boundary=frame')
    
if __name__ == "__main__":
    app.debug = True
    app.run(host='localhost', port=9874)