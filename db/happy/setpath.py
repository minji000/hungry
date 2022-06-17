import os

dir_path=r'C:\Users\User\Desktop\happy'

res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)

print(res)
print(res[-4])
lastimg=res[-4]
direc_path  ="C:\\Users\\User\\Desktop\\happy"
file_path  = direc_path +'\\' + lastimg
print(file_path)