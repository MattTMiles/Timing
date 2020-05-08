import os
import sys

MainDir = "/fred/oz002/users/mmiles/templates/"
os.chdir(MainDir)

pulsar = sys.argv[1]

#for pulsar in os.listdir(MainDir):
#    if pulsar.startswith("J"):
pulsar_dir = os.path.join(MainDir,pulsar)
os.chdir(pulsar_dir)

os.mkdir(os.path.join(pulsar_dir,"highest_775"))
os.mkdir(os.path.join(pulsar_dir,"highest_856"))

dir_856 = os.path.join(pulsar_dir,"856")
dir_775 = os.path.join(pulsar_dir,"775")
dir_642 = os.path.join(pulsar_dir,"642") 

if os.path.isdir(dir_856):
    os.chdir(dir_856)
    highest = os.popen("psrstat -c snr=pdmp -j FTp -c snr -Q 1D* | sort -k2n | tail -1 |  awk '{print $(NF-1)}'").read().strip("\n")
    os.system("psrsmooth -W "+highest)
    os.system("mv "+highest+".sm "+pulsar_dir+"/highest_856/")

if os.path.isdir(dir_775):
    os.chdir(dir_775)
    highest = os.popen("psrstat -c snr=pdmp -j FTp -c snr -Q 1D* | sort -k2n | tail -1 |  awk '{print $(NF-1)}'").read().strip("\n")
    os.system("psrsmooth -W "+highest)
    os.system("mv "+highest+".sm "+pulsar_dir+"/highest_775/")
    os.chdir(pulsar_dir+"/highest_775")
    os.system("mv "+highest+".sm "+pulsar+".std")
    os.system("cp "+pulsar+".std "+MainDir+"/1obs_smoothed")

if os.path.isdir(dir_642):
    os.chdir(dir_642)
    highest = os.popen("psrstat -c snr=pdmp -j FTp -c snr -Q 1D* | sort -k2n | tail -1 |  awk '{print $(NF-1)}'").read().strip("\n")
    os.mkdir(os.path.join(pulsar_dir,"highest_642"))
    os.system("psrsmooth -W "+highest)
    os.system("mv "+highest+".sm "+pulsar_dir+"/highest_642/")

