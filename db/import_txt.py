import os
import time
import  threading

def runimport_txt():
 right = 'C:\\Users\\User\\Desktop\\count'
 right1 = os.listdir(right) 
 right2=right1[-7]
 print (right1)
 print (right)

 do ='python uploadtxt.py '+right2+ ' set present_foodlist'
 print(do)

 os.system(do)
 #os.system('firestore-import --accountCredentials serviceAccountKey.json --backupFile book.json')
 #os.system()
 
 threading.Timer(30,runimport_txt).start()

runimport_txt()