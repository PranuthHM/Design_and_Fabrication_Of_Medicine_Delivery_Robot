import cv2
import os
import time
import numpy as np
import time
import pandas as pd
import pygame
import time
from gtts import gTTS
from mutagen.mp3 import MP3
import time
import numpy as np
import time
from datetime import datetime
import cv2
from movement import *
from sensors import *
from lcd import *

def text_to_speech(text1):
    if len(text1) < 16:
        lcd_byte(0x01, LCD_CMD)
        lcd_string(f"{text1}",LCD_LINE_1)
        time.sleep(1)
    else:
        lcd_byte(0x01, LCD_CMD)
        d1 = text1[:16]
        d2 = text1[16:]
        lcd_string(f"{d1}",LCD_LINE_1)
        lcd_string(f"{d2}",LCD_LINE_2)
        time.sleep(1)
        
    myobj = gTTS(text=text1, lang='en-us', tld='com', slow=False)
    myobj.save("voice.mp3")
    print('\n------------Playing--------------\n')
    song = MP3("voice.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load('voice.mp3')
    pygame.mixer.music.play()
    time.sleep(song.info.length)
    pygame.quit()


# Create Local Binary Patterns Histograms for face recognization
##recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the trained mode
recognizer.read('trainer/trainer.yml')
##recognizer.read('/home/pi/Desktop/face_recog_folder/Raspberry-Face-Recognition-master/trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX


df=pd.read_csv('names.csv')

text_to_speech('Welcome to NURSE ROBOT')

while True:
    SWITCH()
        
    now = datetime.now()
    TIME = now.strftime('%H:%M')
    print(TIME)
    time.sleep(1)
    
    SWITCH()

    if TIME == '14:30':
        counter1 = 0
        while True:
            counter1 += 1
            if counter1 > 3:
                break
            
            if counter1 == 1:
                PATH1()
            if counter1 == 2:
                PATH2()
            if counter1 == 3:
                PATH3()
                
            kcount = 0
            ucount = 0
            tcount =0
            text_to_speech('please look into the camera')
            print('please look into the camera')
            print(counter1)
            
            # Initialize and start the video frame capture
            cam = cv2.VideoCapture(0)
            while True:
                # Read the video frame
                ret, im =cam.read()

                # Convert the captured frame into grayscale
                gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

                # Get all face from the video frame
                faces = faceCascade.detectMultiScale(gray, 1.2,5)


                # For each face in faces
                for(x,y,w,h) in faces:
                    tcount += 1

                    # Create rectangle around the face
                    cv2.rectangle(im, (x,y), (x+w,y+h), (0,255,0), 4)

                    # Recognize the face belongs to which ID
                    Id,i = recognizer.predict(gray[y:y+h,x:x+w])

                    print(Id, i)

                    if i < 60:
                        kcount += 1
                        name=df.loc[(df['id']==Id)]['name'].values[0]
                        cv2.putText(im, name, (x,y-40), font, 2, (255,255,255), 3)
                    else:
                        ucount += 1
                        cv2.putText(im, "unknown", (x,y-40), font, 2, (255,255,255), 3)

                # Display the video frame with the bounded rectangle
                cv2.imshow('im',im)
                
                # If 'q' is pressed, close program
                if cv2.waitKey(100) & tcount > 10:
                    break
           
            cam.release()
            # Close all windows
            cv2.destroyAllWindows()
            print(f'kcuount {kcount}')
            if kcount > 1:
                    text_to_speech('please place your finger on sensors')
                    heartRate = HEART_BEAT()
                    print('{} your heart rate is {}'.format(name, heartRate))
     
                    temp = TEMP()
                    print('{} your temperature is {}'.format(name, temp))
                    
                    print('{} take your medecine'.format(name))
                    time.sleep(1)
                    text_to_speech('{} take your medecine'.format(name))

                    print(counter1)
                    if counter1 == 1:
                        ONE()
                    if counter1 == 2:
                        TWO()
                    if counter1 == 3:
                        THREE()
                    
                    SPRAY()
                    
            else:
                    print('Face not recognised')
                    text_to_speech('Face not recognised')


