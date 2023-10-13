#Tgram BotFather api
#   API: 6663880889:AAFa6cIryY-BKaWFjuEzi-Z392_BpXPXTOM

#Commands
#   sudo pip3 install telepot
#   sudo pip install telepot

#Program starts
import time
import telepot
import RPi.GPIO as GPIO
from telepot.loop import MessageLoop

GPIO.setmode(GPIO.BOARD)

GPIO.setup(13,GPIO.OUT)
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command : %s' % command)

    bot.sendMessage(chat_id,"Command Recieved");

    if command == '/on':
        GPIO.output(13,GPIO.HIGH)
    elif command == '/off':
        GPIO.output(13,GPIO.LOW)

bot = telepot.Bot('6663880889:AAFa6cIryY-BKaWFjuEzi-Z392_BpXPXTOM') #<---API

MessageLoop(bot,handle).run_as_thread()
print('I am listening')

while 1:
    time.sleep(10)

#Program ends

