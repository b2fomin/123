import RPi.GPIO as GPIO
import time

PINS=[24,25,8,7,12,16,20,21]
GPIO.setmode(GPIO.BCM)
GPIO.setup(PINS,GPIO.OUT)
def line_up(led_number,period):
    GPIO.output(led_number,True)
    time.sleep(period)
    GPIO.output(led_number,False)



line_up(PINS[2],2)