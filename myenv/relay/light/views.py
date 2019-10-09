from django.shortcuts import render
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
from datetime import datetime, date
from django.http import HttpResponse
import json

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

sensor = Adafruit_DHT.DHT11
pin = 21

IN1 = 16
IN2 = 20

GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)

temp_ext = 0
humid_ext = 0


time.sleep(1)

# Create your views here.


def Home(request):

	#==========================
	# person = {'firstname': 'Craig', 'lastname': 'Daniels'}
	data = {'humid': "0", 'temp': 0}
	humid = 0
	temp = 0
	#==========================
	if 'on' in request.POST:
		GPIO.output(16, GPIO.HIGH)
		humid, temp = TempRead()

	elif 'off' in request.POST:
		GPIO.output(16, GPIO.LOW)

	data["humid"] = str(humid)
	data["temp"] = str(temp)

	atmosphere= {
		# 'person': person,
		'data': data,
		'humid': humid,
		}

	return render(request, 'light/home.html',atmosphere)

def Data(request):
	humid, temp = TempRead()
	response = {
		'db_humid': humid,
		'db_temp': temp
	}
	return HttpResponse(json.dumps(response), content_type="application/json")

def TempRead():
	print("come to TempRead")
	humid, temp = Adafruit_DHT.read_retry(sensor, pin)

	if humid != None and temp != None:
		print('Temp: {}'.format(temp))
		print('Humid: {}'.format(humid))
		time.sleep(0.3)
		
	else:
		print('Error')
		time.sleep(0.3)
	return humid, temp




# def Home(request):

# 	#==========================
# 	# person = {'firstname': 'Craig', 'lastname': 'Daniels'}
# 	data = {'humid': "0", 'temp': 0}
# 	weather= "sunny"
# 	humid = 0
# 	temp = 0
# 	#==========================

# 	if 'on' in request.POST:
# 		GPIO.output(16, GPIO.HIGH)
# 		humid, temp = TempRead()
# 	elif 'off' in request.POST:
# 		GPIO.output(16, GPIO.LOW)

# 	data["humid"] = str(humid)
# 	data["temp"] = str(temp)

# 	atmosphere= {
# 		# 'person': person,
# 		'data': data,
# 		'humid': humid,
# 		}

# 	return render(request, 'light/home.html',atmosphere)



# def TempRead():
# 	print("come to while True")
# 	#while True:
# 	humid, temp = Adafruit_DHT.read_retry(sensor, pin)

# 	if humid != None and temp != None:
# 		print('Temp: {}'.format(temp))
# 		print('Humid: {}'.format(humid))
# 		time.sleep(0.3)

# 		# time.sleep(1)
# 		# print('Finish 5 seconds')
# 	else:
# 		print('Error')
# 		time.sleep(0.3)
# 		# time.sleep(1)
# 	return humid, temp

