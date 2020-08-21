import os
import sys

#This makes a 2D template of the file

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
'''
#Now in the directory containing the relevant files
#put all the zapped Tf4.ar files in a metafile
os.system("python /fred/oz005/users/mshamoha/federico/rfihunter_nogate.py 0 *zap.Tf4*ar")
os.system("pam -mE /fred/oz002/users/mmiles/templates/2D_Templates/my_pars/"+pulsar+".par --update_dm *mohsen")
os.system("paz -E 5 -e paz *mohsen")
os.system("ls J*paz > metafile")
#Specify the file to use (ftu) just as the first .mohsen file
ftu = os.popen("ls J*_Tf4_tot.ar | head -1").read().strip("\n")
#From this, create a constant profile
os.system("psrsmooth -W J*_Tf4_tot.ar")
os.system("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_constant_portrait.py *.sm "+ftu+" constant_profile."+pulsar+".port")
os.system("pam -Tp -e Tp.port constant_profile."+pulsar+".port")
os.system("paz -E 5 -e paz.port constant_profile."+pulsar+".Tp.port") 

#Creates constant profile
##have to put the pythonpath in here because for some reason it's defaulting to the skylake one##
os.system("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppalign.py -M metafile -T -I constant_profile."+pulsar+".Tp.paz.port -o metafile_average."+pulsar+".Tp.port --niter 2")

#Clean the metafile_average file
os.system("~/.conda/envs/py2/bin/python /fred/oz005/users/mshamoha/federico/rfihunter_nogate.py 0 metafile_average."+pulsar+".Tp.port")

#Creates the average metadata model/2D model
os.system("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppspline.py -d metafile_average."+pulsar+".Tp.port.mohsen -o 2D.spline."+pulsar+".spl -N None -n 10 -s --plots -a 2D.portrait."+pulsar+".Tp.paz.port")

os.system("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppspline.py -d metafile_average."+pulsar+".Tp.port.mohsen -o 2D.spline."+pulsar+".spl -N prof -n 10 -s --plots -a 2D.portrait."+pulsar+".Tp.paz.norm.port")

#os.system("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppgauss.py -d metafile_average."+pulsar+".Tp.port -o 2D.spline."+pulsar+".spl -o 2D.portrait."+pulsar+".Tp.paz.port")
### making difference plot:
'''
os.system("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_residual_plots.py -m 2D.spline."+pulsar+".spl -d metafile_average."+pulsar+".Tp.port.mohsen --nowb -r 0.5")
os.system("cp metafile*resids.png ../../residuals/")
