#This makes a 2D portrait of the file using the pulse portraiture code
#From line 103 this also times the files using pat. Comment out below that line if that isn't wanted

import os
import sys
import subprocess as sproc 
import shlex
import matplotlib
import glob
matplotlib.use('Agg')

pulsar = sys.argv[1]

#For an observation folder make sure you get rid of rfi and install the ephemeris first
'''
os.chdir(pulsar_dir)
for files in os.listdir(pulsar_dir):
    if files.startswith('J'):
        if files.endswith('ar'):
            if not os.path.isfile(files+'.mohsen'):
                p = sproc.Popen("pam -mE /fred/oz002/users/mmiles/templates/msp_ephemerides/"+pulsar+".par --update_dm "+files,shell=True)
                p.wait()
                p = sproc.call("python /fred/oz005/users/mshamoha/federico/rfihunter_nogate.py 0 "+files,shell=True)
                
                p = sproc.Popen("paz -E 2 -e paz "+files,shell=True)

'''

#This is used to construct the metafile

ftu = os.popen("ls *paz | head -1").read().strip("\n")

std = pulsar+'.std'

#Create a constant profile
p = sproc.Popen("rm metafile", shell=True)
p.wait()
p = sproc.Popen("ls *paz > metafile", shell=True)
p.wait()
p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_constant_portrait.py "+std+" "+ftu+" constant_profile."+pulsar+".port",shell=True)


p = sproc.Popen("pam -Tp -e Tp.port constant_profile."+pulsar+".port",shell=True)
p.wait()

p = sproc.Popen("paz -E 2 -e paz.port constant_profile."+pulsar+".Tp.port",shell=True)
p.wait()

#Creates constant profile

p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppalign.py -M metafile -T -I constant_profile."+pulsar+".Tp.paz.port -o metafile_average."+pulsar+".Tp.port --niter 2",shell=True)
print('metafile_average portrait is created')

#Clean the metafile_average file
p = sproc.call("~/.conda/envs/py2/bin/python /fred/oz005/users/mshamoha/federico/rfihunter_nogate.py 0 metafile_average."+pulsar+".Tp.port",shell=True)

#Creates the average metadata model/2D model
#p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppspline.py -d metafile_average."+pulsar+".Tp.port.mohsen -o 2D.spline."+pulsar+".spl -N None -n 10 -s --plots -a 2D.portrait."+pulsar+".Tp.paz.port",shell=True)
p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppspline.py -d grand.paz -o 2D.spline."+pulsar+".spl -N None -n 10 -s --plots -a 2D.portrait."+pulsar+".Tp.paz.port",shell=True)

#Same as above but creates a normalised version
#p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppspline.py -d metafile_average."+pulsar+".Tp.port.mohsen -o 2D.spline."+pulsar+".spl -N prof -n 10 -s --plots -a 2D.portrait."+pulsar+".Tp.paz.norm.port",shell=True)
p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppspline.py -d grand.paz  -o 2D.spline."+pulsar+".spl -N prof -n 10 -s --plots -a 2D.portrait."+pulsar+".Tp.paz.norm.port",shell=True)

#making difference plot:
#p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_residual_plots.py -m 2D.spline."+pulsar+".spl -d metafile_average."+pulsar+".Tp.port.mohsen --nowb -r 0.5",shell=True)
p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_residual_plots.py -m 2D.spline."+pulsar+".spl -d grand.pazp  --nowb -r 0.5",shell=True)

#Moves the residuals to the residuals folder

#Creates a dedispersed version to use with pat
p=sproc.Popen("pam -D -e ddisp *norm.port",shell=True)
p.wait()

'''
#Copy the portraits to the repository
template_repo = '/fred/oz002/users/mmiles/templates/2D_Templates/Template_repo'
p=sproc.Popen("cp *port "+template_repo,shell=True)
p.wait()

#Copy the dedispersed version to the repository
p=sproc.Popen("cp *ddisp "+template_repo,shell=True)
p.wait()
'''
