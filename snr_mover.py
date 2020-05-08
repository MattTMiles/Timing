import os
import subprocess
from subprocess import Popen, PIPE
import sys
import errno

#Specify parent directory
MainDir = "/fred/oz002/users/mmiles/templates/"
os.chdir(MainDir)

pulsar = sys.argv[1]

#for pulsar in os.listdir(MainDir):
#    if pulsar.startswith("J"):
#Change to requested pulsar directory
pulsar_dir = os.path.join(MainDir,pulsar)
os.chdir(pulsar_dir)
Tp_dir = os.path.join(pulsar_dir,"Tp_templates")
dir_856 = os.path.join(Tp_dir,"856")
dir_775 = os.path.join(Tp_dir,"775")
dir_642 = os.path.join(Tp_dir,"642") 

if os.path.isdir(dir_856):
    os.chdir(dir_856)
    try:
        os.mkdir(os.path.join(dir_856,"high_snr"))
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass
    #os.system("rm 1D*")
    os.chdir(dir_856)
    for ints in os.listdir(dir_856):
        if ints.startswith("1D"):
            snr = os.popen("psrstat -c snr=pdmp -j FTp -c snr -Q "+ints+" | awk '{print $(NF)}'").read().split()
            if float(snr[0]) > 40:
                os.system("cp ./"+ints+" ./high_snr/")

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
