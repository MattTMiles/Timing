import os
import sys
import subprocess as sproc 
import shlex
import matplotlib
matplotlib.use('Agg')
#This makes a 2D template of the file
pulsar = sys.argv[1]


MainDir = "/fred/oz002/users/mmiles/templates/2D_Templates"
os.chdir(MainDir)

pulsar_dir = os.path.join(MainDir, pulsar)
os.chdir(pulsar_dir)

folder = "pol_profs"
folder_dir = os.path.join(pulsar_dir,folder)
os.chdir(folder_dir)

#Now in the directory containing the relevant files
#put all the zapped Tf4.ar files in a metafile
#os.system("python /fred/oz005/users/mshamoha/federico/rfihunter_nogate.py 0 *zap.Tf4*ar")

p = sproc.call("python /fred/oz005/users/mshamoha/federico/rfihunter_nogate.py 0 *zap.Tf4*ar",shell=True)
#p.wait()

#os.system("pam -mE /fred/oz002/users/mmiles/templates/2D_Templates/my_pars/"+pulsar+".par --update_dm *mohsen")
p = sproc.Popen("pam -mE /fred/oz002/users/mmiles/templates/2D_Templates/my_pars/"+pulsar+".par --update_dm *mohsen",shell=True)
p.wait()
#os.system("paz -E 5 -e paz *mohsen")
p = sproc.Popen("paz -E 5 -e paz *mohsen",shell=True)
p.wait()
#os.system("ls J*paz > metafile")
p = sproc.Popen("ls J*paz > metafile",shell=True)
p.wait()
#Specify the file to use (ftu) just as the first .mohsen file

ftu = os.popen("ls J*_Tf4_tot.ar | head -1").read().strip("\n")

#From this, create a constant profile
#os.system("psrsmooth -W J*_Tf4_tot.ar")
p = sproc.Popen("psrsmooth -W J*_Tf4_tot.ar",shell=True)
p.wait()
#os.system("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_constant_portrait.py *.sm "+ftu+" constant_profile."+pulsar+".port")

p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_constant_portrait.py *.sm "+ftu+" constant_profile."+pulsar+".port",shell=True)
#p.wait()

#os.system("pam -Tp -e Tp.port constant_profile."+pulsar+".port")
p = sproc.Popen("pam -Tp -e Tp.port constant_profile."+pulsar+".port",shell=True)
p.wait()
#os.system("paz -E 5 -e paz.port constant_profile."+pulsar+".Tp.port")
p = sproc.Popen("paz -E 5 -e paz.port constant_profile."+pulsar+".Tp.port",shell=True)
p.wait()

#Creates constant profile
##have to put the pythonpath in here because for some reason it's defaulting to the skylake one##
#os.system("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppalign.py -M metafile -T -I constant_profile."+pulsar+".Tp.paz.port -o metafile_average."+pulsar+".Tp.port --niter 2")
p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppalign.py -M metafile -T -I constant_profile."+pulsar+".Tp.paz.port -o metafile_average."+pulsar+".Tp.port --niter 2",shell=True)
#p.wait()
#Clean the metafile_average file
#os.system("~/.conda/envs/py2/bin/python /fred/oz005/users/mshamoha/federico/rfihunter_nogate.py 0 metafile_average."+pulsar+".Tp.port")
p = sproc.call("~/.conda/envs/py2/bin/python /fred/oz005/users/mshamoha/federico/rfihunter_nogate.py 0 metafile_average."+pulsar+".Tp.port",shell=True)
#p.wait()
#Creates the average metadata model/2D model
#os.system("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppspline.py -d metafile_average."+pulsar+".Tp.port.mohsen -o 2D.spline."+pulsar+".spl -N None -n 10 -s --plots -a 2D.portrait."+pulsar+".Tp.paz.port")
p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppspline.py -d metafile_average."+pulsar+".Tp.port.mohsen -o 2D.spline."+pulsar+".spl -N None -n 10 -s --plots -a 2D.portrait."+pulsar+".Tp.paz.port",shell=True)
#p.wait()

#os.system("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppspline.py -d metafile_average."+pulsar+".Tp.port.mohsen -o 2D.spline."+pulsar+".spl -N prof -n 10 -s --plots -a 2D.portrait."+pulsar+".Tp.paz.norm.port")
p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppspline.py -d metafile_average."+pulsar+".Tp.port.mohsen -o 2D.spline."+pulsar+".spl -N prof -n 10 -s --plots -a 2D.portrait."+pulsar+".Tp.paz.norm.port",shell=True)
#p.wait()
#os.system("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppgauss.py -d metafile_average."+pulsar+".Tp.port -o 2D.spline."+pulsar+".spl -o 2D.portrait."+pulsar+".Tp.paz.port")
### making difference plot:

#os.system("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_residual_plots.py -m 2D.spline."+pulsar+".spl -d metafile_average."+pulsar+".Tp.port.mohsen --nowb -r 0.5")
p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_residual_plots.py -m 2D.spline."+pulsar+".spl -d metafile_average."+pulsar+".Tp.port.mohsen --nowb -r 0.5",shell=True)
#p.wait()

#os.system("cp metafile*resids.png ../../residuals/")
p = sproc.Popen("cp metafile*resids.png ../../residuals/",shell=True)
p.wait()

os.system("pam -F -e portF 2D.portrait*norm.port")
'''

MainDir = "/fred/oz002/users/mmiles/templates/2D_Templates"
Dir_to_use = "/fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/1Dtims/"
os.chdir(Dir_to_use)
os.system("pat -A FDM -f tempo2 -s /fred/oz002/users/mmiles/templates/msp_templates/"+pulsar+".std /fred/oz002/users/mmiles/templates/2D_Templates/"+pulsar+"/pol_profs/J*mohsen > "+pulsar+".tim")
'''
