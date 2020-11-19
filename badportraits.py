#This makes a 2D template of the file (bad portrait off of a single observation), it also does bad timing.

import os
import sys
import subprocess as sproc 
import shlex
import matplotlib

pulsar = sys.argv[1]

#Takes the first eligible file in the list to make a portrait out of 
activedir = '/fred/oz002/users/mmiles/templates/2D_Templates'
pulsar_dir = os.path.join(activedir,pulsar)
data_dir = os.path.join(pulsar_dir,'pol_profs')
'''
os.chdir(data_dir)
for file in sorted(os.listdir(data_dir)):
    if file.startswith('J') & file.endswith('.Tf4.ch.ar'):
        os.system('pam -D -e ddisp '+file)
        os.system('mv *ddisp /fred/oz002/users/mmiles/templates/2D_Templates/bad_portraits')
        break
'''
os.chdir('/fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/bad_portraits_sm')

'''
#Creates a timing file using the 'bad portrait' - this will time against the epoch that the portrait is made from, but it shouldn't be so significant to alter the average timing
p = sproc.Popen("pat -A FDM -f tempo2 -P -s /fred/oz002/users/mmiles/templates/2D_Templates/bad_portraits/"+pulsar+"* "+pulsar_dir+"/timing_256/2*Tpf128* > "+pulsar+".bad_portrait_tim", shell=True)
p.wait()
'''
#Same as above but for higher snr data 
p = sproc.Popen("pat -A FDM -f tempo2 -P -s /fred/oz002/users/mmiles/templates/2D_Templates/bad_portraits/"+pulsar+"*sm "+pulsar_dir+"/256_highsnr/2*Tpf128* > "+pulsar+".bad_portrait_tim_highsnr", shell=True)
p.wait()


