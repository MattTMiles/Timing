import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import os
import sys
import subprocess as sproc 

pulsar = sys.argv[1]

maindir = "/fred/oz002/users/mmiles/templates/2D_Templates"
pulsar_dir = os.path.join(maindir,pulsar)

os.chdir(pulsar_dir)

try:
    os.system("mkdir timing_64")
except:
    pass
try:
    os.system("mkdir timing_256")
except:
    pass

t64dir = os.path.join(pulsar_dir,"timing_64")
t256dir = os.path.join(pulsar_dir,"timing_256")
timing_dir = os.path.join(pulsar_dir,"timing")

os.chdir(timing_dir)

p = sproc.Popen("psradd -I 64 -e Tpf128_64 20*Tpf128", shell = True)
p.wait()

p = sproc.Popen("psradd -I 256 -e Tpf128_256 20*Tpf128", shell = True)
p.wait()

p = sproc.Popen("mv *Tpf128_64 "+t64dir, shell = True)
p.wait()

p = sproc.Popen("mv *Tpf128_256 "+t256dir, shell = True)
p.wait()

