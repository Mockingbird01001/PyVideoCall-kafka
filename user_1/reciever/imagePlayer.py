# -*- coding: utf-8 -*-
# @Author: mockingbird
# @Date:   2022-12-01 15:28:44
# @Last Modified by:   mockingbird
# @Last Modified time: 2022-12-01 16:20:28


import numpy as np
import cv2

class ImagePlayer:

	def stop_stream(self):
		cv2.destroyAllWindows()


	def frame2image(self, data):
    	try:
	        nparr = np.fromstring(data, np.uint8)
	        frame_recieved = cv2.imdecode(nparr,cv2.IMREAD_COLOR)
	        et, buffer = cv2.imencode('.jpeg', frame_recieved)
            frame = buffer.tobytes()
            yield (b'--frame\n'
                   b'Content-Type: image/jpeg\n\n' + frame + 
                   b'\n')

	        if cv2.waitKey(1):
    	    	break
    	except:
    		exit(0)