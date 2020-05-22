#This is because I want to quickly do this in a batch script and didn't want to write a .sh

import os
import sys

pulsar = sys.argv[1]
templates = "/fred/oz002/users/mmiles/templates"
pulsar_dir = os.path.join(templates,pulsar)
os.chdir(pulsar_dir)

obs = os.listdir(pulsar_dir)[0]
obs_dir = os.path.join(pulsar_dir,obs)
os.chdir(obs_dir)

beamno = os.listdir(obs_dir)[0]
beamno_dir = os.path.join(obs_dir, beamno)
os.chdir(beamno_dir)

#Move through frequency directory
freq = os.listdir(beamno_dir)[0]
freq_dir = os.path.join(beamno_dir, freq)
os.chdir(freq_dir)

os.system("paz -r -e r *.ar ; psradd -PT *.r -o added.ar ; pam -mTFp added.ar ; psrsmooth added.ar ; rm *.r")