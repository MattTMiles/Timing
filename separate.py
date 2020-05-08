#This script separates the templates that have been created into folders
# per their bandwidth

import os
import errno
import sys

#Specify parent directory
MainDir = "/fred/oz002/users/mmiles/templates/"
os.chdir(MainDir)

pulsar=sys.argv[1]

#for pulsar in os.listdir(MainDir):
#    if pulsar.startswith("J"):
        
#Change to requested pulsar directory
pulsar_dir = os.path.join(MainDir,pulsar)
os.chdir(pulsar_dir)

#Removes accidentally created files
#os.system("rm 2*.Tp")
#Create directories for the bandwidths
Tp_dir = os.path.join(pulsar_dir,"Tp_templates")
try:
    os.mkdir(Tp_dir)
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    pass
os.chdir(Tp_dir)
try:
    os.mkdir(os.path.join(Tp_dir,"775"))
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    pass
dir_775 = os.path.join(Tp_dir,"775")

try:
    os.mkdir(os.path.join(Tp_dir,"856"))
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    pass
dir_856 = os.path.join(Tp_dir,"856")

os.chdir(pulsar_dir)
for template in os.listdir(pulsar_dir):
    if template.startswith("1D_"):
        bw = os.popen("psrstat -c bw "+template+" | awk '{print $(NF)}'").read().strip("bw=").strip("\n")
        if bw == "856":
            os.system("mv "+template+" "+dir_856)
        elif bw == "775.75":
            os.system("mv "+template+" "+dir_775)
        else:
            print("weird obs:", os.getcwd())
            print("different bandwidth:", bw)
            try:
                os.mkdir(os.path.join(Tp_dir, bw))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
                pass
            os.system("mv "+template+" "+os.path.join(Tp_dir, bw))
                    