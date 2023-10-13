import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)
while True:
    GPIO.output(13,GPIO.HIGH)
    sleep(1)
    GPIO.output(13,GPIO.LOW)
    sleep(1)

# gpio pin --> led+ --> led- --> Ground