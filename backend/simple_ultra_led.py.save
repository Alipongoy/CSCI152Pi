import RPi.GPIO as GPIO
import time

trig = 16
echo = 18

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(16, GPIO.OUT)
	GPIO.setup(18, GPIO.IN)
	GPIO.setup(13, GPIO.OUT)

def distanceInmeters(trignum, echonum):
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
	distance =  during * 340 / 2
	return distance

def loop():
	while True:
		distance = distanceInMeters(16,18)
		print 'Distance for sensor: ', format(distance, '.3f'), 'm'
		if distance < 1.5:
			GPIO.output(13,0)
		else: GPIO.output(13,1)
	print ''
	time.sleep(3)

def destroy():
	GPIO.cleanup()
if __name__ == "__main__":
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
