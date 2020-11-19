import os
import sys
import subprocess as sproc 
import glob
import numpy as np 
#import pandas as pd 

pulsar = sys.argv[1]

msp_ephs = '/fred/oz002/users/mmiles/templates/msp_ephemerides'
meerpipe_data = '/fred/oz002/users/mmiles/templates/meerpipe_data'
meerpipe_dir = '/fred/oz005/users/aparthas/MSP_Census/PTA/'
pulsar_dir = os.path.join(meerpipe_dir,pulsar)

os.chdir(meerpipe_data)

try:
    os.mkdir(os.path.join(meerpipe_data,pulsar))
except:
    pass
meer_pulsar = os.path.join(meerpipe_data,pulsar)

#This is to grab the grand added profiles from renees directories
os.chdir(meer_pulsar)
os.system('cp /fred/oz005/users/rspiewak/msp_census_output/'+pulsar+'/pol_profs/J*_Tf4_tot.ar .')

#This is to grab the timing data required
os.chdir(pulsar_dir)
for epoch in os.listdir(pulsar_dir):
    epochdir = os.path.join(pulsar_dir,epoch)
    os.chdir(epochdir)
    for subdir in os.listdir(epochdir):
        subdir = os.path.join(epochdir,subdir)
        os.chdir(subdir)
        for subdir2 in os.listdir(subdir):
            subdir2 = os.path.join(subdir, subdir2)
            os.chdir(subdir2)
            decimated = os.path.join(subdir2,'decimated')
            os.chdir(decimated)
            #Creates the sym link to the data I need
            try:
                os.system('cp *t32f116p* '+meer_pulsar+'/')
            except:
                pass

#This does the things to the data that I need it to do
#First create the 1D standard
os.chdir(meer_pulsar)
#Implement the ephemeris
os.system('pam -mE '+msp_ephs+'/'+pulsar+'.par --update_dm *tot.ar')

#Create the 1D standard
os.system('pam -F -e F *tot.ar')
os.system('psrsmooth -W *tot.F')
os.system('mv *sm '+pulsar+'.meerpipe_std')

#Change the data to the form that I want
os.system('pam -T -e Tf116p *t32f116p*')
#Install the ephemeris on these files
os.system('pam -mE '+msp_ephs+'/'+pulsar+'.par --update_dm *Tf116p')

#Create the 2D portraits
ftu = os.popen("ls *Tf116p | head -1").read().strip("\n")

p = sproc.Popen("paz -E 5 -e paz *Tf116p",shell=True)
p.wait()

p = sproc.Popen("ls *paz > metafile",shell=True)
p.wait()

std = pulsar+'.meerpipe_std'

p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_constant_portrait.py "+std+" "+ftu+" constant_profile."+pulsar+".port",shell=True)

p = sproc.Popen("pam -Tp -e Tp.port constant_profile."+pulsar+".port",shell=True)
p.wait()

p = sproc.Popen("paz -E 5 -e paz.port constant_profile."+pulsar+".Tp.port",shell=True)
p.wait()

p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppalign.py -M metafile -T -I constant_profile."+pulsar+".Tp.paz.port -o metafile_average."+pulsar+".Tp.port --niter 2",shell=True)

#Clean the metafile_average file
p = sproc.call("~/.conda/envs/py2/bin/python /fred/oz005/users/mshamoha/federico/rfihunter_nogate.py 0 metafile_average."+pulsar+".Tp.port",shell=True)

#Creates the average metadata model/2D model
p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppspline.py -d metafile_average."+pulsar+".Tp.port.mohsen -o 2D.spline."+pulsar+".spl -N None -n 10 -s --plots -a 2D.portrait."+pulsar+".Tp.paz.port",shell=True)

#Same as above but creates a normalised version
p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppspline.py -d metafile_average."+pulsar+".Tp.port.mohsen -o 2D.spline."+pulsar+".spl -N prof -n 10 -s --plots -a 2D.portrait."+pulsar+".Tp.paz.norm.port",shell=True)

#making difference plot:
p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_residual_plots.py -m 2D.spline."+pulsar+".spl -d metafile_average."+pulsar+".Tp.port.mohsen --nowb -r 0.5",shell=True)

#dedispersed version for pat
p=sproc.Popen("pam -D -e ddisp *norm.port",shell=True)
p.wait()

portrait_dir = '/fred/oz002/users/mmiles/templates/2D_Templates'

#Time it using pat
p = sproc.Popen("pat -A FDM -f tempo2 -P -s 2D.portrait."+pulsar+".Tp.paz.norm.ddisp 2*Tf116p > "+pulsar+".pat_Tf116p.tim", shell=True)
p.wait()

p = sproc.Popen("pat -A FDM -f tempo2 -P -s 2D.portrait."+pulsar+".Tp.paz.norm.ddisp "+portrait_dir+"/"+pulsar+"/timing_64/*Tpf128_64 > "+pulsar+".pat_Tpf128_64.tim", shell=True)
p.wait()

p = sproc.Popen("pat -A FDM -f tempo2 -P -s 2D.portrait."+pulsar+".Tp.paz.norm.ddisp "+portrait_dir+"/"+pulsar+"/timing_256/*Tpf128_256 > "+pulsar+".pat_Tpf128_256.tim", shell=True)
p.wait()

print(pulsar+' has been timed with pat')

#Time it using pptoas (wideband timing)
p = sproc.Popen("ls *Tf116p > timing_metafile1",shell=True)
p.wait()

p = sproc.call("~/.conda/envs/py2/bin/python ~/soft/timing/pptoas.py -d timing_metafile1 -m 2D*.spl -o 2D."+pulsar+".tim.Tf116p",shell=True)

p = sproc.Popen("ls "+portrait_dir+"/timing_64/*Tpf128_64 > timing_metafile2",shell=True)
p.wait()

p = sproc.call("~/.conda/envs/py2/bin/python ~/soft/timing/pptoas.py -d timing_metafile2 -m 2D*.spl -o 2D."+pulsar+".tim.Tf128p_64",shell=True)

p = sproc.Popen("ls "+portrait_dir+"/timing_256/*Tpf128_256 > timing_metafile3",shell=True)
p.wait()

p = sproc.call("~/.conda/envs/py2/bin/python ~/soft/timing/pptoas.py -d timing_metafile3 -m 2D*.spl -o 2D."+pulsar+".tim.Tf128p_256",shell=True)
