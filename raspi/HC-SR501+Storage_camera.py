
from picamera import PiCamera
from time import sleep
import datetime
import sys, os
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from uuid import uuid4
import RPi.GPIO as GPIO
import time

PROJECT_ID = "smart-refrigerator1"

cred = credentials.Certificate("./serviceAccountKey.json")
default_app = firebase_admin.initialize_app(cred, {
    'storageBucket': f"{PROJECT_ID}.appspot.com"
})

camera = PiCamera()

def fileUpload(file):
    bucket = storage.bucket()
    blob = bucket.blob(file)
    new_token = uuid4()
    metadata = {"firebaseStorageDownloadTokens": new_token}
    blob.metadata = metadata

    blob.upload_from_filename(filename='./Images/'+file, content_type='image/jpeg')
    print(blob.public_url)

def execute_camera():
    suffix = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.jpg'
    filename =suffix

    camera.capture('/home/hungry/Images/' + filename)
    fileUpload(filename)

pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

time.sleep(2)
print('Ready')

chk = 0
try:
    while True:
        if(GPIO.input(pin)==1):
            print('motion')
            chk += 1
            if chk >= 2:
                execute_camera()
                chk = 0
        else:
            print('noting')
        time.sleep(1)

except KeyboardInterrupt:
    pass
    print('Exit with ^C. Goodbye!')
    GPIO.cleanup()
    exit()