#Makes tim files

import numpy as np
import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import sys
import subprocess as sproc

pulsar = sys.argv[1]

parent_dir = '/fred/oz002/users/mmiles/templates'
pulsar_dir = os.path.join(parent_dir,pulsar)
#timing_dir = os.path.join(pulsar_dir,'timing')
MSP_timing_dir = os.path.join(pulsar_dir,'MSP_PTA')
portrait_dir = '/fred/oz002/users/mmiles/templates/2D_Templates/2D_ddisp'
template_dir = '/fred/oz002/users/mmiles/templates/msp_templates'
patfile_dir2D = '/fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/2Dportrait_tims'
patfile_dir1D = '/fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/1Dtims'
PTA_dir = '/fred/oz005/users/aparthas/MSP_Census/PTA'
timing_dir = os.path.join(PTA_dir,pulsar)
patfile_MSP = '/fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/MSP_PTA_tims'
#Make the timing files

#2D
os.chdir(patfile_MSP)

p = sproc.Popen('rm '+pulsar+'*', shell=True)
p.wait()

p = sproc.Popen('pat -A FDM -C "snr" -f "tempo2 IPTA" -P -s '+portrait_dir+'/*'+pulsar+'*scrunched '+timing_dir+'/*/*/1284/decimated/*t32f116p*ar > '+pulsar+'.portrait_msp_pta_tim', shell=True)
p.wait()
'''
#1D
os.chdir(patfile_dir1D)

p = sproc.Popen('rm '+pulsar+'*', shell=True)
p.wait()

p = sproc.Popen('pat -A FDM -C "snr" -f tempo2 -s '+template_dir+'/*'+pulsar+'* '+timing_dir+'/*Tpf128 > '+pulsar+'.tim1D', shell=True)
p.wait()
'''