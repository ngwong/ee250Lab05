import RPi.GPIO as GPIO
import time

led = 11

#delay in seconds and amount of times to blink
def blink(delay, amount):
	GPIO.setup(led, GPIO.OUT)
	for i in range (0, amount):
		GPIO.output(led, GPIO.HIGH)
		time.sleep(delay)
		GPIO.output(led, GPIO.LOW)
		time.sleep(delay)	

def Main():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	blink(.5, 5)

if __name__ == '__main__':
	Main()
