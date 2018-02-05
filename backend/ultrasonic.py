#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

#TRIG = 11
#ECHO = 12
#TRIG2 = 15
#ECHO2 = 16
objectArray = [[11,12], [15,16], ]

def setup():
	GPIO.setmode(GPIO.BOARD)
	for keyPair in objectArray:
		GPIO.setup(keyPair[0], GPIO.OUT)
		GPIO.setup(keyPair[1], GPIO.IN)
	#GPIO.setup(TRIG, GPIO.OUT)
	#GPIO.setup(ECHO, GPIO.IN)
	#GPIO.setup(TRIG2, GPIO.OUT)
	#GPIO.setup(ECHO2, GPIO.IN)

def distance(trignum, echonum):
	GPIO.output(trignum, 0)
	time.sleep(0.000002)

	GPIO.output(trignum, 1)
	time.sleep(0.00001)
	GPIO.output(TRIG, 0)

	
	while GPIO.input(echonum) == 0:
		a = 0
	time1 = time.time()
	while GPIO.input(echonum) == 1:
		a = 1
	time2 = time.time()

	during = time2 - time1
	return during * 340 / 2 * 100

def loop():
	while True:
		sensornum = 1
		for keyPair in objectArray:
			dis = distance(keyPair[0],keyPair[1]) * .01
			print 'Distance ', sensornum, ': ', format(dis, '.3f') , 'm'
			sensornum +=1
		#dis2 = distance(TRIG2,ECHO2) * .01
		#print 'Distance 1: ', format(dis1, '.3f') , 'm'
		#print ''
		#print 'Distance 2: ', format(dis2, '.3f') , 'm'
		print ''
		time.sleep(1)

def destroy():
	GPIO.cleanup()

if __name__ == "__main__":
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
