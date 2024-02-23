import time
import RPi.GPIO as GPIO
import os
import Adafruit_DHT
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

SW = 16
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

BZ = 8
GPIO.setup(BZ, GPIO.OUT)
GPIO.output(BZ, False)

relay = 5
GPIO.setup(relay, GPIO.OUT)
GPIO.output(relay, False)

HR_SENSOR = 12
tempFlag = 0
bpFlag = 0
hrFlag = 0
GPIO.setup(HR_SENSOR,GPIO.IN)

sensor = Adafruit_DHT.DHT11
pin = 4

def HEART_BEAT():
     global tempFlag
     global bpFlag
     global hrFlag
     tempFlag = 0
     bpFlag   = 0
     hrFlag   = 1
     if hrFlag == 1 :
      print('Hold The finger On sensor')
      #time.sleep(1) 
      sensorCounter = 0
      startTime     = 0
      endTime       = 0
      rateTime      = 0
      while sensorCounter < 1 and  hrFlag == 1:
        if (GPIO.input(HR_SENSOR)):
          if sensorCounter == 0:
            startTime = int(round(time.time()*1000))
            #print startTime
          sensorCounter = sensorCounter + 1
          #print sensorCounter
          while(GPIO.input(HR_SENSOR)):
            if hrFlag == 0:
              break
            pass

      time.sleep(1)      
      endTime  = int(round(time.time()*1000))
      #print endTime
      rateTime = endTime - startTime
      #print rateTime
      rateTime = rateTime / sensorCounter
      heartRate = (60000 / rateTime) #/ 3 
      heartRate = abs(heartRate)
      heartRate=int(heartRate+20)
      return heartRate

def TEMP():
    _, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return temperature
    
def SWITCH():
    if GPIO.input(SW) == False:
        print('Emergency')
        GPIO.output(BZ, True)
        time.sleep(1)
        GPIO.output(BZ, False)
        time.sleep(1)

def SPRAY():
    GPIO.output(relay, True)
    time.sleep(1)
    GPIO.output(relay, False)
    time.sleep(1)
    print('sorinkle spray')
SPRAY()