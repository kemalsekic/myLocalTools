import os
import subprocess

txtFile = "myApps\kemgen.txt"
cmderFile = "C:\\Users\\sekick\\Desktop\\KemoRELX\\cmder_mini\\Cmder.exe"
cmd = "cd /"

def openCMDER():
    cmd1 = subprocess.Popen(cmderFile, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = cmd1.communicate()
    # with open(cmd1,"wb") as out, open(err,"wb") as err: subprocess.Popen("cd /",stdout=out,stderr=err)
    print('cd /'.format(out))
    input()

def openTxtFile():
    os.open(txtFile, os.O_RDWR|os.O_CREAT)
    print("Executed date check complete")

# openTxtFile()
openCMDER()