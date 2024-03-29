import os
import sys
import subprocess as sproc 
import shlex
import matplotlib.pyplot as plt

pulsar = sys.argv[1]

MainDir = "/fred/oz002/users/mmiles/templates/2D_Templates"
os.chdir(MainDir)

pulsar_dir = os.path.join(MainDir, pulsar)
os.chdir(pulsar_dir)

#256 sub-integration data is being pointed to
active_Dir = os.path.join(pulsar_dir,"timing_64")
os.chdir(active_Dir)

p = sproc.Popen("ls *Tpf128_64 > timing_metafile",shell=True)
p.wait()

#Normal pulse-portraiture fitting
#If this doesn't get removed when updating it'll just copy the same data twice, leading to a wrong timing file
try:
    p = sproc.Popen("rm 2D."+pulsar+".tim", shell=True)
    p.wait()
except:
    pass

p = sproc.call("~/.conda/envs/py2/bin/python ~/soft/timing/pptoas.py -d timing_metafile -m "+pulsar_dir+"/pol_profs/2D*.spl -o 2D."+pulsar+".tim",shell=True)
p = sproc.call("cp 2D."+pulsar+".tim /fred/oz002/users/mmiles/templates/2D_Templates/pp_timing/pp_2dtoas_64/" ,shell=True)

#Pulse-portraiture fitting without fitting for DM or bary
try:
    p = sproc.Popen("rm 2D_noDM*tim", shell=True)
    p.wait()
except:
    pass

p = sproc.call("~/.conda/envs/py2/bin/python ~/soft/timing/pptoas.py --fix_DM --no_bary -d timing_metafile -m "+pulsar_dir+"/pol_profs/2D*.spl -o 2D_noDM."+pulsar+".tim",shell=True)

p = sproc.call("cp 2D_noDM*tim /fred/oz002/users/mmiles/templates/2D_Templates/pp_timing/pp_2dtoas_noDMfit_64/" ,shell=True)