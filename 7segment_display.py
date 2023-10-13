import tm1637 #pip3 install raspberrypi-tm1637
import time
from datetime import datetime

#to display 0 0 0 0
tm = tm1637.TM1637(clk = 18, dio = 17) # gpio18 = pin12    &&    gpio17 = pin11
clear = [0,0,0,0]
tm.write(clear)
time.sleep(5)

#to display sliding text
S = 'This is pretty cool'
tm.scroll(S,delay=250)
time.sleep(2)
tm.write(clear)
time.sleep(1)

#to display time
now = datetime.now()
hh = int(datetime.strftime(now,'%H'))
mm = int(datetime.strftime(now,'%M'))
tm.numbers(hh,mm,colon=True)
time.sleep(2)
tm.write(clear)
