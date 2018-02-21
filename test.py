import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

import time

CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

led = 11

#delay in seconds and amount of times to blink
def blink(delay, amount):
	GPIO.setup(led, GPIO.OUT)
	for i in range (amount):
		GPIO.output(led, GPIO.HIGH)
		time.sleep(delay)
		GPIO.output(led, GPIO.LOW)
		time.sleep(delay)	

def read_light(delay, amount):
	for i in range (amount):
		print(mcp.read_adc(i))
		time.sleep(delay)

def Main():
	#GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	blink(.5, 5)
	read_light(.1, 50)

if __name__ == '__main__':
	Main()
