import RPi.GPIO as GPIO
import time

PINS=[24,25,8,7,12,16,20,21]
GPIO.setmode(GPIO.BCM)
def line_up_or_down(led_number,period,state):
    GPIO.output(led_number,state)
    time.sleep(period)
    GPIO.output(led_number,not state)

def blink(led_number,blink_count,blink_period):
    GPIO.setup(led_number,GPIO.OUT)
    for _ in range(blink_count):
        line_up_or_down(led_number,blink_period,True)
        time.sleep(blink_period)

def running_light_or_dark(count,period,state):
    GPIO.setup(PINS,GPIO.OUT)
    GPIO.output(PINS[0:count if count<len(PINS) else len(PINS)],state)
    for number in range(count):
        line_up_or_down(PINS[number%len(PINS)],period,not state)
        GPIO.output(PINS[number%len(PINS)],state)

def dec_to_binList(dec_number):
    answer=str(bin(dec_number))[2:]
    answer=answer.zfill(len(PINS))
    A=[]
    for i in answer:
        A.append(int(i))
    return A

def light_number(number):
    GPIO.setup(PINS,GPIO.OUT)
    GPIO.output(PINS,False)
    A=list(reversed(dec_to_binList(number)))
    for i in range(len(A)):
        if A[i]==1:
            GPIO.output(PINS[i],True)

def running_pattern(pattern,direction,count,period):
    GPIO.setup(PINS,GPIO.OUT)
    A=list(reversed(dec_to_binList(pattern)))
    for _ in range(count):
        GPIO.output(PINS,False)
        for i in range(len(A)):
            if A[i]==1:
                GPIO.output(PINS[i],True)
        if direction=="left":
            A=[A[-1]]+A[:-1]
        else:
            A=A[1:]+[A[0]]
        time.sleep(period)

def f(led_number,freq):
    GPIO.setup(PINS,GPIO.OUT)
    GPIO.output(PINS,False)
    p=GPIO.PWM(led_number,freq)
    p.start(0)
    for dc in range(0,101,5):
        p.ChangeDutyCycle(dc)
        time.sleep(0.1)
    for dc in range(100,-1,-5):
        p.ChangeDutyCycle(dc)
        time.sleep(0.1)
    p.stop()

