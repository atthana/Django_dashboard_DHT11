import Adafruit_DHT
import time
import RPi.GPIO as GPIO
import gengraph
from datetime import datetime

sensor = Adafruit_DHT.DHT11
pin = 21
GPIO.setwarnings(False)

data_temp = []
data_time = []

while True:
#for i in range(5):
        
    humid, temp = Adafruit_DHT.read_retry(sensor, pin)
    dt = datetime.now().strftime('%H:%M:%S')
    data_time.append(dt)

    if humid != None and temp != None:
        text_temp = '{:.2f}'.format(temp)
        data_temp.append(float(text_temp))
        print(dt)
        print('Temp: {}'.format(temp) + " c'")
        print('Humid: {}'.format(humid) + " %")
        print('------------')
        time.sleep(5)
    else:
        print('Error')
        time.sleep(5)
        
gengraph.GenGraph(data_time, data_temp,'Daily Temperature')
        


