import os
import shutil

source = input("enter source folder name:- ")
destination = input('enter destination folder name:- ')

source = source + '/'
destination = destination + '/'

lof = os.listdir(source)
for file in lof:
    shutil.copy((source+file), destination)