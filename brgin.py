import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt

PINS=[10,9,11,5,6,13,19,26]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(4,GPIO.IN)

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

def define_voltage():
    for j in range(256):
        light_number(j)
        time.sleep(0.001)
        if GPIO.input(4)==0:
            return j

def read():
    while True:
        number=int(input())
        light_number(number)
        GPIO.output(17,number)

if __name__=='__main__':
    while True:
        print(define_voltage())
    GPIO.cleanup()
