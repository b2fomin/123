import RPi.GPIO as GPIO
import time

PINS=[24,25,8,7,12,16,20,21]
GPIO.setmode(GPIO.BCM)
def line_up(led_number,period):
    GPIO.output(led_number,True)
    time.sleep(period)
    GPIO.output(led_number,False)

def blink(led_number,blink_count,blink_period):
    GPIO.setup(led_number,GPIO.OUT)
    for _ in range(blink_count):
        line_up(led_number,blink_period)
        time.sleep(blink_period)

def running_light(count,period):
    GPIO.setup(PINS,False)
    for number in range(count):
        line_up(PINS[number%len(PINS)],period)


running_light(4,0.5)