import os
import shutil

path = input("Enter the path")
lof = os.listdir(path)

for file in lof :
    name,ext = os.path.splitext(file)
    ext = ext[1]
    if ext == "":
        continue
    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)
    else :
        os.mkdir(path+"/"+ext)
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)
     