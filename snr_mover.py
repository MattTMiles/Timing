import os
import subprocess
from subprocess import Popen, PIPE
import sys
import errno
import glob
import numpy as np

#Specify parent directory
#MainDir = "/fred/oz002/users/mmiles/templates/2D_Templates"
#os.chdir(MainDir)

target = '/fred/oz002/users/mmiles/MSP_DR/subband_comps/tophalf_highsnr_psradd_check/'

pulsar = sys.argv[1]


pulsar_dir = os.path.join(target,pulsar)
os.chdir(pulsar_dir)

og_dir = '/fred/oz002/users/mmiles/MSP_DR/MSP_data/high_snr_psradd/'
pulsar_og_dir = os.path.join(og_dir,pulsar)

os.chdir(pulsar_og_dir)
print(pulsar_og_dir)

snrs =[]
for arch in glob.glob("J*dly"):
    print(arch)
    snr = os.popen("psrstat -c snr=pdmp -c snr -j DFTp -Q "+arch+" | awk '{print $(NF)}'").read().split()
    snr = float(snr[0])
    print(snr)
    snrs.append(snr)

snrs = np.array(snrs)
meansnr = snrs.mean()

for arch in glob.glob("J*dly"):
    snr = os.popen("psrstat -c snr=pdmp -c snr -j DFTp -Q "+arch+" | awk '{print $(NF)}'").read().split()
    snr = float(snr[0])

    if snr > meansnr:
        os.symlink(os.path.join(pulsar_og_dir,arch), os.path.join(pulsar_dir,arch))



