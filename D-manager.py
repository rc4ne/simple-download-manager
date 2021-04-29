import os
import shutil

PATH = "C:\\Users\\Sachin\\Downloads"
ARR = os.listdir(PATH)

#### CHECKING FOR EXT FOLDER ####
def checkNmakefolder(f,ext):
    if not os.path.exists(PATH+"\\"+ext):
        os.makedirs(PATH+"\\"+ext)
    movefile(f,ext)

#### MOVING THE FILE ####
def movefile(f,ext):
    shutil.move(PATH+"\\"+f, PATH+"\\"+ext+"\\"+f)
    # print("File moved Successfully!")

#### MAIN DRIVER CODE ####
for f in ARR:
    ext = f.split(".")[-1]
    if os.path.isfile(PATH+"\\"+f):
        checkNmakefolder(f,ext)
    else:
        # print("Directory found!")
        pass
