import numpy as np
import os
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#MOVEMENT
IN1=2
IN2=3
IN3=17
IN4=27

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

GPIO.output(IN1, False)
GPIO.output(IN2, False)
GPIO.output(IN3, False)
GPIO.output(IN4, False)

#DOOR ONE
IN5=23
IN6=24
#DOOR TWO
IN7=10
IN8=22
#DOOR THREE
IN9=11
IN10=9

GPIO.setup(IN5, GPIO.OUT)
GPIO.setup(IN6, GPIO.OUT)
GPIO.setup(IN7, GPIO.OUT)
GPIO.setup(IN8, GPIO.OUT)
GPIO.setup(IN9, GPIO.OUT)
GPIO.setup(IN10, GPIO.OUT)

GPIO.output(IN5, False)
GPIO.output(IN6, False)
GPIO.output(IN7, False)
GPIO.output(IN8, False)
GPIO.output(IN9, False)
GPIO.output(IN10, False)

def FORWORD(t):
    print('FORWORD')
    GPIO.output(IN1,False)
    GPIO.output(IN2, True)
    GPIO.output(IN3,False)
    GPIO.output(IN4,True)
    time.sleep(t)
    
def BACKWORD(t):
    print('FORWORD')
    GPIO.output(IN1,True)
    GPIO.output(IN2, False)
    GPIO.output(IN3,True)
    GPIO.output(IN4,False)
    time.sleep(t)
    
def STOP():
    print('STOP')
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, False)
    time.sleep(1)
    
def RIGHT(t):
    print('RIGHT')
    GPIO.output(IN1,True)
    GPIO.output(IN2, False)
    GPIO.output(IN3,False)
    GPIO.output(IN4,True)
    time.sleep(t)
    
def LEFT(t):
    print('LEFT')
    GPIO.output(IN1,False)
    GPIO.output(IN2, True)
    GPIO.output(IN3,True)
    GPIO.output(IN4,False)
    time.sleep(t)

    
def ONE():
    print ("ONE")
    GPIO.output(IN5,True)
    GPIO.output(IN6, False)
    time.sleep(2)
    GPIO.output(IN5,False)
    GPIO.output(IN6, False)
    time.sleep(5)
    GPIO.output(IN5,False)
    GPIO.output(IN6, True)
    time.sleep(2)
    GPIO.output(IN5,False)
    GPIO.output(IN6, False)
    time.sleep(1)

def TWO():
    print ("TWO")
    GPIO.output(IN7,True)
    GPIO.output(IN8, False)
    time.sleep(2)
    GPIO.output(IN7,False)
    GPIO.output(IN8, False)
    time.sleep(5)
    GPIO.output(IN7,False)
    GPIO.output(IN8, True)
    time.sleep(2)
    GPIO.output(IN7,False)
    GPIO.output(IN8, False)
    time.sleep(1)
    
def THREE():
    print ("THREE")
    GPIO.output(IN9,True)
    GPIO.output(IN10, False)
    time.sleep(2)
    GPIO.output(IN9,False)
    GPIO.output(IN10, False)
    time.sleep(5)
    GPIO.output(IN9,False)
    GPIO.output(IN10, True)
    time.sleep(2)
    GPIO.output(IN9,False)
    GPIO.output(IN10, False)
    time.sleep(1)
    
def PATH1():
    print('PATH1')
    FORWORD(5)
    STOP()
    LEFT(5)
    STOP()
    FORWORD(5)
    STOP()
    RIGHT(5)
    STOP()
    FORWORD(5)
    STOP()
    
def PATH2():
    print('PATH2')
    LEFT(5)
    STOP()
    FORWORD(5)
    STOP()
    FORWORD(5)
    STOP()
    RIGHT(5)
    STOP()
    FORWORD(5)
    STOP()
    
def PATH3():
    print('PATH3')
    FORWORD(5)
    STOP()
    RIGHT(5)
    STOP()
    FORWORD(5)
    STOP()
    FORWORD(5)
    STOP()
    LEFT(5)
    STOP()
