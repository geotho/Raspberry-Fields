from time import sleep
from collections import defaultdict
import RPi.GPIO as GPIO

CODE = {
'a':'01',
'b':'1000',
'c':'1010',
'd':'100',
'e':'0',
'f':'0010',
'g':'110',
'h':'0000',
'i':'00',
'j':'0111',
'k':'101',
'l':'0100',
'm':'11',
'n':'10',
'o':'111',
'p':'0110',
'q':'1101',
'r':'010',
's':'000',
't':'1',
'u':'001',
'v':'0001',
'w':'011',
'x':'1001',
'y':'1011',
'z':'1100',
'1':'01111',
'2':'00111',
'3':'00011',
'4':'00001',
'5':'00000',
'6':'10000',
'7':'11000',
'8':'11100',
'9':'11110',
'0':'11111',
}

def morse(str):
	for char in str:
		if char == ' ':
			sleep(0.8)
		else:
			for ditdash in CODE[char]:
				if ditdash == '0':
					blink(7, 0.2, 0.2)
				else: 
					blink(7, 0.6, 0.2)
				sleep(0.4)
	return

def blink(pin, on, off):
	GPIO.output(7, True)
	sleep(on)
	GPIO.output(7, False)
	sleep(off)
	return

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

sleep(3)
morse("sms")
sleep(2)
morse("sos")
sleep(2)
	