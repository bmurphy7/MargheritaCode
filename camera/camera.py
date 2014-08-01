#python code for raspberry pi camera
#camera connects very easily, see raspberry pi's website

import picamera
import datetime

stamp = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S') #time stamp for file name
camera = picamera.PiCamera()
camera.vflip = True 			#flips vertically
camera.hflip = True			#flips horizontally
camera.capture('./Rpi_pics/%s.png' % stamp) #takes picture and saves it to Rpi_pics directory

print 'Nice Photo!'
