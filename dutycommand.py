#This is because I want to quickly do this in a batch script and didn't want to write a .sh

import os
import sys

#Load these modules as a work around for the broken pathways I've somehow created
os.system("module load numpy/1.16.3-python-2.7.14")
os.system("module load scipy/1.0.0-python-2.7.14")
os.system("module --ignore-cache load psrchive/1e36de3a8")

pulsar = sys.argv[1]
templates = "/fred/oz002/users/mmiles/templates"
pulsar_dir = os.path.join(templates,pulsar)
os.chdir(pulsar_dir)
for obs in os.listdir(pulsar_dir):
    if obs.startswith("2"):
        obs_dir = os.path.join(pulsar_dir,obs)
        os.chdir(obs_dir)

        beamno = os.listdir(obs_dir)[0]
        beamno_dir = os.path.join(obs_dir, beamno)
        os.chdir(beamno_dir)

        #Move through frequency directory
        freq = os.listdir(beamno_dir)[0]
        freq_dir = os.path.join(beamno_dir, freq)
        os.chdir(freq_dir)

        os.system("python /fred/oz005/users/mshamoha/federico/rfihunter_nogate.py 0 *ar ; psradd *.mohsen -o added.mohsen ; pam -mTFp added.mohsen ; psrsmooth added.mohsen ; rm 2*.mohsen")