import os
import shutil
source=input('enter the folders name-')
destination=input('enter the folders name-')
source=source+'/'
destination=destination+'/'
listOfFiles=os.listdir(source)
for file in listOfFiles:
    shutil.copy((source+file),destination)
