import RPi.GPIO as GPIO
from time import sleep
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

def shake_input():
	'''
	GPIO.setmode(GPIO.BOARD)
	shake_input_pin = 32
	GPIO.setup(shake_input_pin, GPIO.IN)
	
	return GPIO.input(shake_input_pin)
	'''
	spi = busio.SPI(clock=board.SCK,
					MISO=board.MISO,
					MOSI=board.MOSI)
	
	cs = digitalio.DigitalInOut(board.D5)
	mcp = MCP.MCP3008(spi, cs)
	
	return AnalogIn(mcp, MCP.P0).value
	

def test():
	for i in range(30):
		shake_value = shake_input()
		print(shake_value)
		sleep(0.5)
	
	
if __name__ == '__main__':
	test()


