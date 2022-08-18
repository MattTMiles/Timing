#This makes a 2D portrait of the file using the pulse portraiture code
#From line 103 this also times the files using pat. Comment out below that line if that isn't wanted

import os
import sys
import subprocess as sproc 
import shlex
import matplotlib
import glob

import numpy as np

matplotlib.use('Agg')

pulsar = sys.argv[1]

ReneeDir = '/fred/oz005/users/rspiewak/msp_census_output'
MainDir = "/fred/oz002/users/mmiles/templates/2D_Templates"

MSP_dir = '/fred/oz002/users/mmiles/MSP_DR/MSP_data/high_snr_psradd'

os.chdir(MSP_dir)

pulsar_dir = os.path.join(MSP_dir, pulsar)
pol_profs = os.path.join(pulsar_dir,'pol_profs')

#ry:
#    os.mkdir(pulsar_dir)
#except:
#    pass

os.chdir(pulsar_dir)

#folder = "portrait"


#try:
#    os.mkdir(os.path.join(os.getcwd(),folder))
#except:
#    pass

#folder_dir = os.path.join(pulsar_dir,folder)

#p=sproc.Popen('pam -mD J*p',shell=True)
#p.wait()
#os.system('touch '+epoch+'.isdone')

'''
This subsection below is to activate the dlyfix and to polarisation scrunch, only uncomment if this isn't already done 
(if this is forgotten it's not a huge deal. dlyfix has an exception catcher for this)


p = sproc.Popen("pam -p -e p J*.ar",shell=True)
p.wait()
p = sproc.Popen('/fred/oz005/users/mkeith/dlyfix/dlyfix -e dly J*.p',shell=True)
p.wait()
'''

#os.chdir(pulsar_dir)
for files in os.listdir(pulsar_dir):
    if files.startswith('J'):
        if files.endswith('dly_16ch'):
            #if not os.path.isfile(files+'.mohsen'):
            p = sproc.Popen("pam -mE /fred/oz002/users/mmiles/MSP_DR/github_ephs/"+pulsar+".par "+files,shell=True)
            p.wait()
            #p = sproc.call("python /fred/oz005/users/mshamoha/federico/rfihunter_nogate.py 0 "+files,shell=True)
            #p = sproc.Popen('paz -r -e paz '+files,shell=True)
            #p.wait()
            #p = sproc.Popen("paz -E 2 -e paz "+files.split('.dly')[0]+'.paz',shell=True)
            #p.wait()


#Get rid of the previous metafile
#p = sproc.Popen('psradd -TPF -o grand.added 2*paz',shell =True)
#p.wait()

#This is used to construct the metafile
'''
filelist = glob.glob('*paz')

dictionary = {}
for x in filelist: 
   key = x[:13] 
   group = dictionary.get(key,[]) 
   group.append(x) 
   dictionary[key] = group 

for key in list(dictionary.keys()): 
   active = dictionary[key] 
   active = str(active)[1:-1] 
   active = active.replace(',','') 
   active = active.replace("'","") 
         
   os.system('psradd -TPF -o '+key+'.addedobs '+active) 

p = sproc.Popen('pam -mT *.addedobs',shell =True)
p.wait()
'''
'''
#If the snr is higher than 100 then add it in to the metafile
for ints in glob.glob('*addedobs'):
    snr = os.popen("psrstat -c snr=pdmp -c snr -Q "+ints+" | awk '{print $(NF)}'").read().split()
    if float(snr[0]) > 100:
        p = sproc.Popen("echo "+ints+">> grandobsmetafile",shell=True)
        p.wait()
'''
#Specify the file to use (ftu) just as the first .mohsen file

ftu = os.popen("ls *dly_8ch | head -1").read().strip("\n")

std = '/fred/oz002/users/mmiles/MSP_DR/github_templates/'+pulsar+'.std'
#From this, create a constant profile
#os.system("psrsmooth -W J*_Tf4_tot.ar")
#p = sproc.Popen("psrsmooth -W J*_Tf4_tot.ar",shell=True)
#p.wait()
#os.system("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_constant_portrait.py *.sm "+ftu+" constant_profile."+pulsar+".port")
p = sproc.Popen("rm metafile", shell=True)
p.wait()

snrs_total = []
for obs in glob.glob('J*dly_16ch'):
    snr = os.popen("psrstat -c snr=pdmp -c snr -Q "+obs+" | awk '{print $(NF)}'").read().split()
    snrs_total.append(float(snr[0]))

snrs_array = np.array(snrs_total)
median_snr = np.median(snrs_array)
std_snr = np.std(snrs_array)

for obs in glob.glob('J*dly_16ch'):
    snr = os.popen("psrstat -c snr=pdmp -c snr -Q "+obs+" | awk '{print $(NF)}'").read().split()
    if float(snr[0]) > median_snr:
        p = sproc.Popen("echo "+obs+" >> metafile",shell=True)
        p.wait()


#p = sproc.Popen("ls J*paz > metafile", shell=True)
#p.wait()
#p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_constant_portrait.py "+std+" "+ftu+" constant_profile."+pulsar+".port",shell=True)
#p.wait()

#p = sproc.Popen("pam -Tp -e Tp.port constant_profile."+pulsar+".port",shell=True)
#p.wait()

#p = sproc.Popen("paz -E 2 -e paz.port constant_profile."+pulsar+".Tp.port",shell=True)
#p.wait()

#p = sproc.Popen('paz -mr J*paz',shell=True)
#p.wait()

p = sproc.Popen('psradd -T -M metafile -o grand.T_16ch',shell=True)
p.wait()

#Creates constant profile
##have to put the pythonpath in here because for some reason it's defaulting to the skylake one##
#p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppalign.py -M metafile -T -I constant_profile."+pulsar+".Tp.port -o metafile_average."+pulsar+".Tp.port --niter 2",shell=True)

#while not os.path.isfile("metafile_average."+pulsar+".Tp.port"):
#    p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppalign.py -M metafile -T -I constant_profile."+pulsar+".Tp.paz.port -o metafile_average."+pulsar+".Tp.port --niter 2",shell=True)

#p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppalign.py -M metafile -I constant_profile."+pulsar+".Tp.paz.port -T -C 15.0 -o metafile_trial."+pulsar+".Tp.port --niter 2",shell=True)

#print('metafile_average portrait is created')

#Clean the metafile_average file
#p = sproc.call("~/.conda/envs/py2/bin/python /fred/oz005/users/mshamoha/federico/rfihunter_nogate.py 0 metafile_average."+pulsar+".Tp.port",shell=True)
#p = sproc.Popen('paz -mr metafile_average.'+pulsar+'.Tp.port',shell=True)
#p.wait()

#Creates the average metadata model/2D model
#p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppspline.py -d metafile_average."+pulsar+".Tp.port -o 2D.spline."+pulsar+".spl -N None -n 10 -s --plots -a 2D.portrait."+pulsar+".Tp.port",shell=True)
p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppspline.py -d grand.T_16ch -o 2D.spline."+pulsar+".spl_16ch -N None -n 10 -s --plots -a 2D.portrait."+pulsar+".Tp.paz.port_16ch",shell=True)

#Same as above but creates a normalised version
#p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppspline.py -d metafile_average."+pulsar+".Tp.port -o 2D.spline."+pulsar+".spl -N prof -n 10 -s --plots -a 2D.portrait."+pulsar+".Tp.norm.port",shell=True)
p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppspline.py -d grand.T_16ch -o 2D.spline."+pulsar+".spl_16ch -N prof -n 10 -s --plots -a 2D.portrait."+pulsar+".Tp.paz.norm.port_16ch",shell=True)

#making difference plot:
#p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_residual_plots.py -m 2D.spline."+pulsar+".spl -d metafile_average."+pulsar+".Tp.port --nowb -r 0.5",shell=True)
p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_residual_plots.py -m 2D.spline."+pulsar+".spl_16ch -d grand.T_16ch --nowb -r 0.5",shell=True)

#Moves the residuals to the residuals folder
#p = sproc.Popen("cp metafile*resids.png ../../residuals/",shell=True)
#p.wait()

#Creates a dedispersed version to use with pat
p=sproc.Popen("pam -D -e ddisp_8ch *norm.port_16ch",shell=True)
p.wait()

#Copy the portraits to the repository
template_repo = '/fred/oz002/users/mmiles/MSP_DR/MSP_data/portraits_high_snr_psradd_16ch'
p=sproc.Popen("cp 2D*port_16ch "+template_repo,shell=True)
p.wait()

#Copy the dedispersed version to the repository
p=sproc.Popen("cp 2D*ddisp_16ch "+template_repo,shell=True)
p.wait()

