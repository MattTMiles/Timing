import os
import sys
import subprocess as sproc 
import shlex
import matplotlib.pyplot as plt

pulsar = sys.argv[1]

current = os.getcwd()

#256 sub-integration data is being pointed to
active_Dir = os.path.join(current,"obs")
os.chdir(active_Dir)

p = sproc.Popen("ls *Tpf128_64 > timing_metafile",shell=True)
p.wait()

#os.chdir(current)
#Normal pulse-portraiture fitting
#If this doesn't get removed when updating it'll just copy the same data twice, leading to a wrong timing file
try:
    p = sproc.Popen("rm "+current+"/2Ddemo."+pulsar+".tim", shell=True)
    p.wait()
except:
    pass

p = sproc.call("~/.conda/envs/py2/bin/python ~/soft/timing/pptoas.py -d timing_metafile -m "+current+"/2D*.spl -o "+current+"/2Ddemo."+pulsar+".tim",shell=True)

#Pulse-portraiture fitting without fitting for DM or bary
try:
    p = sproc.Popen("rm "+current+"/2Ddemo_noDM*tim", shell=True)
    p.wait()
except:
    pass

p = sproc.call("~/.conda/envs/py2/bin/python ~/soft/timing/pptoas.py --fix_DM --no_bary -d timing_metafile -m "+current+"/2D*.spl -o "+current+"/2Ddemo_noDM."+pulsar+".tim",shell=True)

