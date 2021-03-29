import RPi.GPIO as GPIO
import time

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
    for i in range(repetitionsNumber):
        for number in range(256):
            light_number(number,round(256/frequency,1))

if __name__=='__main__':
    repetition=int(input('Enter number: '))
    repeat(repetition,256*2)
    GPIO.cleanup()
