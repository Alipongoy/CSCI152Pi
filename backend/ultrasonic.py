#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

#TRIG = 11
#ECHO = 12
#TRIG2 = 15
#ECHO2 = 16
keyArray = [{'trigNumber': 16, 'echoNumber':18, 'description':'front sensor'}, {'trigNumber': 29, 'echoNumber':31, 'description':'back sensor'}, {'trigNumber': 13, 'echoNumber': 17, 'description':'light sensor'}]

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
            GPIO.setup(dictionaryObject['echoNumber'], GPIO.IN)

#def displayLED(trignum):
#    GPIO.output(trignum,1)
#
#def hideLED(trignum):
#    GPIO.output(trignum,0)

def toggleLED(trignum, isTaken):
    if isTaken:
        GPIO.output(trignum,1)
    else:
        GPIO.output(trignum,0)



def isSpotTaken():
    frontDistance = distanceInMeters(keyArray[0].trigNumber, keyArray[0].echoNumber)
    backDistance = distanceInMeters(keyArray[1].trigNumber, keyArray[1].echoNumber)
    return (frontDistance < 1 and backDistance < 1)




def distanceInMeters(trignum, echonum):
    """
Calculates the distance of an ultrasonic sensor to an object.
@param {Integer} [trignum] The trigger number of the sensor.
@param {Integer} [echonum] The echo number of the sensor.
@return {Float} [during] The distance of the sensor to object in distance.
"""
        GPIO.output(trignum, 0)
        time.sleep(0.000002)

        GPIO.output(trignum, 1)
        time.sleep(0.00001)
        GPIO.output(trignum, 0)


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
        for dictionaryObject in keyArray:
            if (dictionaryObject.description != 'light sensor'):
                #Calculates the distance
                        distance = distanceInMeters(dictionaryObject['trigNumber'], dictionaryObject['echoNumber'])
                        print 'Distance for ', dictionaryObject['description'], ': ', format(distance, '.3f') , 'm'
        print ''

        # Number of times output is displayed to screen
        # Shows LED if spot is taken
        toggleLED(13, isSpotTaken())
        time.sleep(1)

def destroy():
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
        try:
            loop()
        except KeyboardInterrupt:
            destroy()
