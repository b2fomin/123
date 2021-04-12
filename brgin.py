import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt

PINS=[10,9,11,5,6,13,19,26]
PINS_=[24,25,8,7,12,16,20,21]
GPIO.setmode(GPIO.BCM)
GPIO.setup(PINS_,GPIO.OUT)
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

def light_number(number,PINS=PINS):
    GPIO.setup(PINS,GPIO.OUT)
    GPIO.output(PINS,False)
    A=list(reversed(dec_to_binList(number)))
    for i in range(len(A)):
        if A[i]==1:
            GPIO.output(PINS[i],True)

def define_voltage():
    while True:
        for j in range(256):
            light_number(j)
            time.sleep(0.001)
            if GPIO.input(4)==0:
                print(j)
                GPIO.output(PINS_,False)    
                if j!=0:
                    for i in range(8//(255//j)):
                        GPIO.output(PINS_[i],True)     
                break

def read():
    while True:
        number=int(input())
        if number==-1:
            break
        light_number(number)
        GPIO.output(17,number)
    GPIO.cleanup()

def bin_search():
    while True:
        left=0
        right=255
        while left<right:
            light_number((left+right)//2)
            time.sleep(0.001)
            if GPIO.input(4)==1:
                left=(left+right)//2
            else:
                right=(left+right)//2
        print(right)
        

if __name__=='__main__':
    define_voltage()
    GPIO.cleanup()
