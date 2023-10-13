import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
while True:
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(15,GPIO.HIGH)
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(18,GPIO.HIGH)
    sleep(0.5)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(15,GPIO.LOW)
    GPIO.output(16,GPIO.LOW)
    GPIO.output(18,GPIO.LOW)
    sleep(0.5)
     
# gpio pin --> led+ --> led- --> Ground