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
timing_dir = os.path.join(pulsar_dir,'timing')
portrait_dir = '/fred/oz002/users/mmiles/templates/2D_Templates/2D_ddisp'
patfile_dir = '/fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/2Dportrait_tims'

#Make the timing files
os.chdir(patfile_dir)

p = sproc.Popen('rm '+pulsar+'*', shell=True)
p.wait()

p = sproc.Popen('pat -A FDM -f tempo2 -P -s '+portrait_dir+'/*'+pulsar+'* '+timing_dir+'/*Tpf128 > '+pulsar+'.portrait_tim', shell=True)
p.wait()

