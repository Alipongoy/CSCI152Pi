#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

#TRIG = 11
#ECHO = 12
#TRIG2 = 15
#ECHO2 = 16
keyArray = [{'trigNumber': 16, 'echoNumber':18, 'description':'front sensor'},
	    {'trigNumber': 31, 'echoNumber':29, 'description':'back sensor'},
	    {'trigNumber': 11, 'echoNumber':'NA', 'description':'red light'},
	    {'trigNumber': 13, 'echoNumber':'NA', 'description':'green light'},
	    {'trigNumber': 15, 'echoNumber':'NA', 'description':'white light'}]

#dic1 = {'trigNumber': 11, 'echoNumber':12, 'description':'front sensor'}
#dic2 = {'trignumber': 15, 'echonumber':16, 'description':'back sensor'}
#
#dic1["trigNumber"]
#11
#
#dic1["echoNumber"]
#12
#
#dic1["description"]
#front sensor





def setup():
    GPIO.setmode(GPIO.BOARD)
    # This sets up the GPIO in and out pins. Using a for in loop
    for dictionaryObject in keyArray:
        # Sets up each trigNumber to GPIO.OUT
        GPIO.setup(dictionaryObject['trigNumber'], GPIO.OUT)
        # Sets up each echoNumber to GPIO.IN
        if (dictionaryObject['echoNumber'] != "NA"):
            GPIO.setup(dictionaryObject['echoNumber'], GPIO.IN)

#def displayLED(trignum):
#    GPIO.output(trignum,1)
#
#def hideLED(trignum):
#    GPIO.output(trignum,0)

#switch between lights depending on available/unavailable
def toggleLED(isTaken):
    if isTaken:
        lightRed()
    else:
        lightGreen()

#turn on red light
def lightRed():
    GPIO.output(11,1)
    GPIO.output(13,0)
    GPIO.output(15,0)

#turn on green light
def lightGreen():
    GPIO.output(11,0)
    GPIO.output(13,1)
    GPIO.output(15,0)

#turn on white light to show system on
def whiteLight():
    GPIO.output(11,1)
    GPIO.output(13,1)
    GPIO.output(15,1)

"""
determine is spot is taken
taken when frontDistant & back distance are < 1
"""
def isSpotTaken():
    frontDistance = distanceInMeters(keyArray[0]['trigNumber'], keyArray[0]['echoNumber'])
    backDistance = distanceInMeters(keyArray[1]['trigNumber'], keyArray[1]['echoNumber'])
    return (frontDistance < 1 and backDistance < 1)




"""
Calculates the distance of an ultrasonic sensor to an object.
@param {Integer} [trignum] The trigger number of the sensor.
@param {Integer} [echonum] The echo number of the sensor.
@return {Float} [during] The distance of the sensor to object in distance.
"""
def distanceInMeters(trignum, echonum):
    GPIO.output(trignum, 0)
    time.sleep(0.000002)

    GPIO.output(trignum, 1)
    time.sleep(0.00001)
    GPIO.output(trignum, 0)

    print trignum
    while GPIO.input(echonum) == 0:
        a = 0
    time1 = time.time()
    while GPIO.input(echonum) == 1:
        a = 1
    time2 = time.time()

    during = time2 - time1
    distance = during * 340 / 2
    return distance

def loop():
    while True:
	whiteLight()
        for dictionaryObject in keyArray:
            if (dictionaryObject["echoNumber"] != 'NA'):
                #Calculates the distance
                        distance = distanceInMeters(dictionaryObject['trigNumber'], dictionaryObject['echoNumber'])
                        print 'Distance for ', dictionaryObject['description'], ': ', format(distance, '.3f'), 'm'
        # Number of times output is displayed to screen
        # Shows LED if spot is taken
	toggleLED(isSpotTaken())
	time.sleep(1)

def destroy():
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
