import datetime
import os 
import time
import  threading

def makejson():
 path = 'C:\\Users\\User\\Downloads\\yolov5-master\\runs\\detect' 
 detectfile_list = os.listdir(path) 
 sortlist=sorted(detectfile_list)
 print (sortlist)
 lastdetect=sortlist[-1]
 print(lastdetect)

 detectpath3 = 'C:\\Users\\User\\Downloads\\yolov5-master\\runs\\detect\\'+lastdetect
 file_list3 = os.listdir(detectpath3) 
 finaldetecttxt=file_list3[-2]

 print(00000000000000000000000000000000000000000000000000)
 print (file_list3)
 print (finaldetecttxt)
 print(00000000000000000000000000000000000000000000000000)
 finalpath=detectpath3+'\\'+finaldetecttxt
 print(finalpath)


 f = open(finalpath, "r")

 data = f.read().split(",")
 data = [s.strip() for s in data]

 print("garlic:" , data.count('garlic'))
 print("potato:" , data.count('potato'))
 print("egg:" , data.count('egg'))
 print("spam:" , data.count('spam'))
 print("leek:" , data.count('leek'))
 print("apple:" , data.count('apple'))
 print("rotten apple:" , data.count('rotten apple'))
 print("donut:" , data.count('donut'))
 print("paprika:" , data.count('paprika'))
  

 jj=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
 k=int(jj)

 a=data.count('garlic')
 b=data.count('potato')
 c=data.count('egg')
 d=data.count('spam')
 e=data.count('leek')
 f=data.count('apple')
 g=data.count('donut')
 h=data.count('paprika')
 i=data.count('rotten apple')
 
 
 num_a = str(a)
 num_b = str(b)
 num_c = str(c)
 num_d = str(d)
 num_e = str(e)
 num_f = str(f)
 num_g = str(g)
 num_h = str(h)
 num_i = str(i)
 
 soso=[
   {
       "id":k,
       "garlic": num_a,
       "potato": num_b,
       "egg": num_c,
       "spam": num_d,
       "leek": num_e,
       "apple":num_f,
       "donut":num_g,
       "paprika":num_h,
       "rotten apple":num_i,
       
   }
 ]
 
 import json
 fileName = jj+'.json'
 jsonString = soso
 print(jsonString)
 #jsonString = json.loads(jsonString)
 
 file = open(fileName, "w")
 json.dump(jsonString, file)
 file.close()

 threading.Timer(30,makejson).start()
 
makejson()