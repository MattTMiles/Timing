import os
import sys

#This creates TOAs and DMs from the 2D templates. This code needs a python 2 environment with module psrchive/1e36de3a8 loaded

MainDir = "/fred/oz002/users/mmiles/templates/2D_Templates"
os.chdir(MainDir)

pulsar = sys.argv[1]

#for pulsar in os.listdir(MainDir):
#if pulsar.startswith("J"):
pulsar_dir = os.path.join(MainDir, pulsar)
os.chdir(pulsar_dir)

folder = "pol_profs"
folder_dir = os.path.join(pulsar_dir,folder)
os.chdir(folder_dir)

#This line of code creates the 
os.system("~/.conda/envs/py2/bin/python ~/soft/timing/pptoas.py -d metafile -m 2D.spline.*.spl -o "+pulsar+".tim")