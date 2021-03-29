import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt

PINS=[10,9,11,5,6,13,19,26]
GPIO.setmode(GPIO.BCM)

def dec_to_binList(dec_number):
    answer=str(bin(dec_number))[2:]
    answer=answer.zfill(len(PINS))
    A=[]
    for i in answer:
        A.append(int(i))
    return A

def light_number(number,_time):
    GPIO.setup(PINS,GPIO.OUT)
    GPIO.output(PINS,False)
    A=list(reversed(dec_to_binList(number)))
    for i in range(len(A)):
        if A[i]==1:
            GPIO.output(PINS[i],True)
    time.sleep(_time)

def repeat(repetitionsNumber,frequency):
    for i in range(repetitionsNumber//2):
        for number in range(256):
            light_number(number,float(256)/frequency)
        for number in range(255,-1,-1):
            light_number(number,float(256)/frequency)

def make_array(frequency):
    A=[]
    i=0
    while i <=1:
        A.append(int(256*np.sin(i)))
        i+=float(2*np.pi)/frequency
    plt.plot(np.array(A),np.sin(np.array(A)))
    plt.show()
    return A

def sinus(_time,frequency):
    A=make_array(frequency)
    for _ in range(_time//2):
        for j in A:
            light_number(j,float(0.5)/len(A))
        for j in reversed(A):
            light_number(j,float(0.5)/len(A))

if __name__=='__main__':
    try:
        repeatnumber=abs(int(input('Enter number: ')))
        sinus(repeatnumber,10000)
    except:
        pass
    GPIO.cleanup()
