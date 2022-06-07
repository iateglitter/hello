import os
import shutil
source=input("enter source folder name")
destination = input("enter destination folder name")
listOfFiles = os.listdir()
for file in listOfFiles:
    shutil.copy(source+"/"+file,destination+"/")