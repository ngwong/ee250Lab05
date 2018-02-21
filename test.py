import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

import time

CLK  = 11
MISO = 9
MOSI = 10
CS   = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

light = 0
sound = 1
led = 17

#Sample Values, Real Values need to be tested
light_threshold = 500
sound_threshold = 50

def init():
	#GPIO is set to BCM Mode
	GPIO.setwarnings(False)
	GPIO.setup(led, GPIO.OUT)

#delay in seconds and amount of times to blink
def blink(delay, amount):
	for i in range (amount):
		GPIO.output(led, GPIO.HIGH)
		time.sleep(delay)
		GPIO.output(led, GPIO.LOW)
		time.sleep(delay)	

def blink_once(delay):
	GPIO.output(led, GPIO.HIGH)
	time.sleep(delay)
	GPIO.output(led, GPIO.LOW)

def read_light(delay, amount):
	for i in range (amount):
		light_val = mcp.read_adc(light)
		if (light_val > light_threshold):
			print (str(light_val) + " Bright")
		else:
			print (str(light_val) + " Dark")
		time.sleep(delay)

def read_sound(delay, amount):
	for i in range (amount):
		sound_val = mcp.read_adc(sound)
		print (sound_val)
		if (sound_val > sound_threshold):
			blink_once(delay)
			amount -= 1
		else:
			time.sleep(delay)

def Main():
	init()
	blink(.5, 5)
	read_light(.1, 50)
	blink(.2, 4)
	read_sound(.1, 50)
	blink(.2, 4)

if __name__ == '__main__':
	Main()