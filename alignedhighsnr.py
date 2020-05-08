import os
import sys
import subprocess
import shlex

MainDir = "/fred/oz002/users/mmiles/templates/"
os.chdir(MainDir)

ActiveDir = "/fred/oz002/users/mmiles/templates/1obs_smoothed/"

pulsar = sys.argv[1]

#for pulsar in os.listdir(MainDir):
#    if pulsar.startswith("J"):
pulsar_dir = os.path.join(MainDir, pulsar)
os.chdir(pulsar_dir)

dir_775 = os.path.join(pulsar_dir,"775")
dir_856 = os.path.join(pulsar_dir,"856")
dir_642 = os.path.join(pulsar_dir,"642")

if os.path.isdir(dir_775):
    os.chdir(dir_775)
    os.chdir(os.path.join(dir_775,"high_snr"))

    os.system("psradd *DSFTR -o "+pulsar+"_added_775_highsnr")
    #Creates a smoothed version of the added file
    os.system("psrsmooth -W *added_775_highsnr")
    #Moves this back into the parent directory
    os.system("mv *added_775_highsnr* "+pulsar_dir+"/")

if os.path.isdir(dir_856):
    os.chdir(dir_856)
    os.chdir(os.path.join(dir_856,"high_snr"))

    os.system("psradd *DSFTR -o "+pulsar+"_added_856_highsnr")
    #Creates a smoothed version of the added file
    os.system("psrsmooth -W *added_856_highsnr")
    #Moves this back into the parent directory
    os.system("mv *added_856_highsnr* "+pulsar_dir+"/")

if os.path.isdir(dir_642):
    os.chdir(dir_642)
    os.chdir(os.path.join(dir_642,"high_snr"))

    os.system("psradd *DSFTR -o "+pulsar+"_added_642_highsnr")
    #Creates a smoothed version of the added file
    os.system("psrsmooth -W *added_642_highsnr")
    #Moves this back into the parent directory
    os.system("mv *added_642_highsnr* "+pulsar_dir+"/")

    