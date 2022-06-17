import pyrebase
import os
import time
import  threading

def runtime():
      filelist=[f for f in os.listdir(".") if f.endswith(".JPG")]
      for f in filelist:
       os.remove(os.path.join(".", f))

      config={
     "apiKey": "AIzaSyBV1KhfiNJeUT5JfNMC7Zi2VWNCFdigGps",
     "authDomain": "smart-refrigerator1.firebaseapp.com",
     "databaseURL": "https://smart-refrigerator1-default-rtdb.firebaseio.com",
     "projectId": "smart-refrigerator1",
     "storageBucket": "smart-refrigerator1.appspot.com",
     "serviceAccount": "serviceAccountKey.json"
     }

      firebase=pyrebase.initialize_app(config)
      storage=firebase.storage()

      #storage.child("Images/Food_20220527_154205.jpg").download("downloaded.jpg")
      all_files=storage.list_files()
      for file in all_files:
       print(file.name)
       file.download_to_filename(file.name)
       
      print('fin0000000000000000000000000000000')
      print('fin0000000000000000000000000000000')
      print('fin0000000000000000000000000000000')
      
      threading.Timer(60,runtime).start()
      
runtime()
      
      
