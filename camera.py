#photo=========================
from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1280, 720)
camera.start_preview()

camera.start_recording('/home/pi/new1.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()

#video=========================

#from time import sleep
#from picamera import PiCamera

#camera = PiCamera()
#camera.resolution = (1280, 720)
#camera.start_preview()
#sleep(0.5)
#camera.capture('/home/pi/new1.jpg')
#camera.stop_preview()


