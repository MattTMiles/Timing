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


MainDir = "/fred/oz002/users/mmiles/templates/2D_Templates"
os.chdir(MainDir)

pulsar_dir = os.path.join(MainDir, pulsar)
pol_profs = os.path.join(pulsar_dir,'pol_profs')
os.chdir(pulsar_dir)

meerpipe = '/fred/oz005/users/aparthas/MSP_Census/PTA'
meerpipe_pulsar = '/fred/oz005/users/aparthas/MSP_Census/PTA/'+pulsar

folder = "portrait"
try:
    os.mkdir(os.path.join(os.getcwd(),folder))
except:
    pass

folder_dir = os.path.join(pulsar_dir,folder)

os.chdir(meerpipe_pulsar)
for epoch in os.listdir(meerpipe_pulsar):
    if not os.path.isfile(pol_profs+'/'+epoch+'.isdone'):
        epochdir = os.path.join(meerpipe_pulsar,epoch)
        os.chdir(epochdir)
        for beam in os.listdir(epochdir):
            beam_dir = os.path.join(epochdir,beam)
            os.chdir(beam_dir)
            for freq in os.listdir(beam_dir):
                freqdir = os.path.join(beam_dir,freq)
                os.chdir(freqdir)
                decimated_dir = os.path.join(freqdir,'decimated')
                os.chdir(decimated_dir)
                os.system('cp *Tf4* '+pol_profs)
                os.chdir(pol_profs)
                os.system('touch '+epoch+'.isdone')


os.chdir(pol_profs)
for files in os.listdir(pol_profs):
    if files.startswith('J'):
        if files.endswith('ar'):
            if not os.path.isfile(files+'.mohsen'):
                p = sproc.Popen("pam -mE /fred/oz002/users/mmiles/templates/2D_Templates/my_pars/"+pulsar+".par --update_dm "+files,shell=True)
                p.wait()
                p = sproc.call("python /fred/oz005/users/mshamoha/federico/rfihunter_nogate.py 0 "+files,shell=True)
                
                p = sproc.Popen("paz -E 5 -e paz "+files,shell=True)
                p.wait()

#Now in the directory containing the relevant files
#put all the zapped Tf4.ar files in a metafile
#os.system("python /fred/oz005/users/mshamoha/federico/rfihunter_nogate.py 0 *zap.Tf4*ar")

#p = sproc.call("python /fred/oz005/users/mshamoha/federico/rfihunter_nogate.py 0 *zap.Tf4*ar",shell=True)
#p.wait()

#os.system("pam -mE /fred/oz002/users/mmiles/templates/2D_Templates/my_pars/"+pulsar+".par --update_dm *mohsen")
#p = sproc.Popen("pam -mE /fred/oz002/users/mmiles/templates/2D_Templates/my_pars/"+pulsar+".par --update_dm *mohsen",shell=True)
#p.wait()

'''
#This should already be done for all pulsars so this can be commented out unless there is a reset

p = sproc.Popen('cp `find ../timing -name "*Tpf128"` .',shell=True)
p.wait()

p = sproc.Popen("paz -E 5 -e paz *Tpf128",shell=True)
p.wait()

#Install the correct ephemeris to all the data
p=sproc.Popen("pam -mE /fred/oz002/users/mmiles/templates/msp_ephemerides/"+pulsar+".par --update_dm *paz",shell=True)
p.wait()
'''
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


ftu = os.popen("ls *paz | head -1").read().strip("\n")

std = '/fred/oz002/users/mmiles/templates/msp_templates/'+pulsar+'.std'
#From this, create a constant profile
#os.system("psrsmooth -W J*_Tf4_tot.ar")
#p = sproc.Popen("psrsmooth -W J*_Tf4_tot.ar",shell=True)
#p.wait()
#os.system("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_constant_portrait.py *.sm "+ftu+" constant_profile."+pulsar+".port")
p = sproc.Popen("rm metafile", shell=True)
p.wait()
p = sproc.Popen("ls *paz > metafile", shell=True)
p.wait()
p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_constant_portrait.py "+std+" "+ftu+" constant_profile."+pulsar+".port",shell=True)
#p.wait()

#os.system("pam -Tp -e Tp.port constant_profile."+pulsar+".port")
p = sproc.Popen("pam -Tp -e Tp.port constant_profile."+pulsar+".port",shell=True)
p.wait()
#os.system("paz -E 5 -e paz.port constant_profile."+pulsar+".Tp.port")
p = sproc.Popen("paz -E 5 -e paz.port constant_profile."+pulsar+".Tp.port",shell=True)
p.wait()

#Creates constant profile
##have to put the pythonpath in here because for some reason it's defaulting to the skylake one##
p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppalign.py -M metafile -T -I constant_profile."+pulsar+".Tp.paz.port -o metafile_average."+pulsar+".Tp.port --niter 2",shell=True)

#Clean the metafile_average file
p = sproc.call("~/.conda/envs/py2/bin/python /fred/oz005/users/mshamoha/federico/rfihunter_nogate.py 0 metafile_average."+pulsar+".Tp.port",shell=True)

#Creates the average metadata model/2D model
p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppspline.py -d metafile_average."+pulsar+".Tp.port.mohsen -o 2D.spline."+pulsar+".spl -N None -n 10 -s --plots -a 2D.portrait."+pulsar+".Tp.paz.port",shell=True)

#Same as above but creates a normalised version
p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppspline.py -d metafile_average."+pulsar+".Tp.port.mohsen -o 2D.spline."+pulsar+".spl -N prof -n 10 -s --plots -a 2D.portrait."+pulsar+".Tp.paz.norm.port",shell=True)

#making difference plot:
p = sproc.call("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_residual_plots.py -m 2D.spline."+pulsar+".spl -d metafile_average."+pulsar+".Tp.port.mohsen --nowb -r 0.5",shell=True)

#Moves the residuals to the residuals folder
p = sproc.Popen("cp metafile*resids.png ../../residuals/",shell=True)
p.wait()

#Creates a dedispersed version to use with pat
p=sproc.Popen("pam -D -e ddisp *norm.port",shell=True)
p.wait()

#Copy the portraits to the repository
template_repo = '/fred/oz002/users/mmiles/templates/2D_Templates/Template_repo'
p=sproc.Popen("cp *port "+template_repo,shell=True)
p.wait()

#Copy the dedispersed version to the repository
p=sproc.Popen("cp *ddisp "+template_repo,shell=True)
p.wait()

#Timing code from here
timingdata = os.path.join(pulsar_dir,'256_highsnr')
os.chdir(timingdata)

p = sproc.Popen("pat -A FDM -f tempo2 -P -s /fred/oz002/users/mmiles/templates/2D_Templates/Template_repo/2D.portrait."+pulsar+".Tp.paz.norm.ddisp 2*Tpf128_256 > "+pulsar+".portrait_tim_256", shell=True)
p.wait()

print(pulsar+' has been timed with pat')

p = sproc.Popen("cp *portrait_tim_256 /fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/2Dportrait_tims_256", shell=True)
p.wait()

p = sproc.Popen("ls "+pulsar_dir+"/timing_64/*Tpf128_64 > timing_metafile2",shell=True)
p.wait()

p = sproc.call("~/.conda/envs/py2/bin/python ~/soft/timing/pptoas.py -d timing_metafile2 -m "+pol_profs+"/2D*.spl -o 2D."+pulsar+".tim.Tf128p_64",shell=True)

p = sproc.Popen("ls "+pulsar_dir+"/timing_256/*Tpf128_256 > timing_metafile3",shell=True)
p.wait()

p = sproc.call("~/.conda/envs/py2/bin/python ~/soft/timing/pptoas.py -d timing_metafile3 -m "+pol_profs+"/2D*.spl -o 2D."+pulsar+".tim.Tf128p_256",shell=True)


