import os
import glob
import sys
import errno
import itertools
import subprocess as sproc 

MainDir = "/fred/oz002/users/mmiles/templates/"
os.chdir(MainDir)

pulsar = sys.argv[1]
pulsar_dir = os.path.join(MainDir,pulsar)
os.chdir(pulsar_dir)

Dec_dir = os.path.join(pulsar_dir,"Dec_run")
filedir = os.path.join(pulsar_dir,"timing")

os.chdir(Dec_dir)

p = sproc.Popen("psradd -TPF -o grand.added_50snr `psrstat -c snr=pdmp -c snr -Q 2*added | awk '$2>50' | awk '{print $(1)}'`",shell=True)
p.wait()

p = sproc.Popen("psradd -TPF -o grand.added_100snr `psrstat -c snr=pdmp -c snr -Q 2*added | awk '$2>100' | awk '{print $(1)}'`",shell=True)
p.wait()

p = sproc.Popen("psradd -TPF -o grand.added_150snr `psrstat -c snr=pdmp -c snr -Q 2*added | awk '$2>150' | awk '{print $(1)}'`",shell=True)
p.wait()

p = sproc.Popen('psrsmooth -W grand*snr', shell=True)
p.wait()

try:
    p = sproc.Popen('mv *50snr.sm '+pulsar+'.std_dec_50snr', shell=True)
    p.wait()
except:
    pass
try:
    p = sproc.Popen('mv *100snr.sm '+pulsar+'.std_dec_100snr', shell=True)
    p.wait()
except:
    pass

try:
    p = sproc.Popen('mv *150snr.sm '+pulsar+'.std_dec_150snr', shell=True)
    p.wait()
except:
    pass