import RPi.GPIO as GPIO

led = 11

def blink():
	GPIO.setup(led, GPIO.OUT)
	for i in range (0, 5):
		GPIO.output(led, GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(led, GPIO.LOW)
		time.sleep(0.1)	

def Main():
	GPIO.setmode(GPIO.BOARD)
	blink()

if __name__ = '__main__':
	Main()
