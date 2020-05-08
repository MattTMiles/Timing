#This script fixes the time of the files according to their MJD

import os
import sys

#Uncomment for archive version
'''
archive=sys.argv[1]

MJD = os.popen("psredit -c ext:stt_imjd "+archive+" -Q").read().split()[1]
MJD = float(MJD)

if MJD >= 58526 and MJD < 58526.211: 
    os.system("~/soft/timing/./offsetT1.psh -e fixed"+archive)
elif MJD >= 58526.211 and MJD < 58550.149:
    os.system("~/soft/timing/./offsetT2.psh -e fixed"+archive) 
elif MJD >= 58550.149 and MJD < 58550.14921:
    os.system("~/soft/timing/./offsetT3.psh -e fixed"+archive) 
elif MJD >= 58550.14921 and MJD < 58557.14847:
    os.system("~/soft/timing/./offsetT4.psh -e fixed"+archive)
elif MJD >= 58557.14847 and MJD < 58575.960:
    os.system("~/soft/timing/./offsetT5.psh -e fixed"+archive)
elif MJD >= 58575.960 and MJD < 58633.999:
    os.system("~/soft/timing/./offsetT6.psh -e fixed"+archive)
elif MJD >= 58633.999 and MJD < 58693.500:
    os.system("~/soft/timing/./offsetT.psh -e fixed"+archive)
elif MJD >= 58693.500:
    archive = archive

'''
#Uncomment for entire directory

Dir = os.getcwd()
#Specify the extension of the files you want to alter
ext = "Fp"
for archive in os.listdir(Dir):
    if archive.startswith("20") and archive.endswith(ext):
        MJD = os.popen("psredit -c ext:stt_imjd "+archive+" -Q").read().split()[1]
        MJD = float(MJD)
        if MJD > 58526 and MJD < 58526.2108912037: 
            os.system("~/soft/timing/./offsetT1.psh -e "+ext+" "+archive)
        elif MJD >= 58526.2108912037 and MJD < 58550.14921296296:
            os.system("~/soft/timing/./offsetT2.psh -e "+ext+" "+archive)
        elif MJD >= 58550.14921296296 and MJD < 58550.14921296296:
            os.system("~/soft/timing/./offsetT3.psh -e "+ext+" "+archive)
        elif MJD >= 58550.14921296296 and MJD < 58557.14847222222:
            os.system("~/soft/timing/./offsetT4.psh -e "+ext+" "+archive)
        elif MJD >= 58557.14847222222 and MJD < 58575.95951388889:
            os.system("~/soft/timing/./offsetT5.psh -e "+ext+" "+archive)
        elif MJD >= 58575.95951388889 and MJD < 58633.99930555555:
            os.system("~/soft/timing/./offsetT6.psh -e "+ext+" "+archive)
        elif MJD >= 58633.99930555555 and MJD < 58693:
            os.system("~/soft/timing/./offsetT.psh -e "+ext+" "+archive)
        elif MJD >= 58693:
            archive = archive
