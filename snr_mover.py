import os
import subprocess
from subprocess import Popen, PIPE
import sys
import errno

#Specify parent directory
MainDir = "/fred/oz002/users/mmiles/templates/2D_Templates"
os.chdir(MainDir)

pulsar = sys.argv[1]

#for pulsar in os.listdir(MainDir):
#    if pulsar.startswith("J"):
#Change to requested pulsar directory
pulsar_dir = os.path.join(MainDir,pulsar)
os.chdir(pulsar_dir)
try:
    os.mkdir('256_highsnr')
except:
    pass
high_snr = os.path.join(pulsar_dir,'256_highsnr')
dir_256 = os.path.join(pulsar_dir,"timing_256")

os.chdir(dir_256)
for ints in os.listdir(dir_256):
    if ints.startswith("2"):
        snr = os.popen("psrstat -c snr=pdmp -c snr -Q "+ints+" | awk '{print $(NF)}'").read().split()
        if float(snr[0]) > 100:
            os.system("cp ./"+ints+" "+high_snr)
            
'''
if os.path.isdir(dir_775):
    os.chdir(dir_775)
    try:
        os.mkdir(os.path.join(dir_775,"high_snr"))
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass
    #os.system("rm 1D*")
    os.chdir(dir_775)
    for ints in os.listdir(dir_775):
        if ints.startswith("1D"):
            snr = os.popen("psrstat -c snr=pdmp -j FTp -c snr -Q "+ints+" | awk '{print $(NF)}'").read().split()
            if float(snr[0]) > 40:
                os.system("cp ./"+ints+" ./high_snr/")

if os.path.isdir(dir_642):
    os.chdir(dir_642)
    try:
        os.mkdir(os.path.join(dir_642,"high_snr"))
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass
    #os.system("rm 1D*")
    os.chdir(dir_642)
    for ints in os.listdir(dir_642):
        if ints.startswith("1D"):
            snr = os.popen("psrstat -c snr=pdmp -j FTp -c snr -Q "+ints+" | awk '{print $(NF)}'").read().split()
            if float(snr[0]) > 40:
                os.system("cp ./"+ints+" ./high_snr/")
'''
