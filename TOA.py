import os
import sys
import subprocess as sproc 
import shlex
#This creates TOAs and DMs from the 2D templates. 

MainDir = "/fred/oz002/users/mmiles/templates/2D_Templates"
os.chdir(MainDir)

pulsar = sys.argv[1]

#for pulsar in os.listdir(MainDir):
#if pulsar.startswith("J"):
pulsar_dir = os.path.join(MainDir, pulsar)
os.chdir(pulsar_dir)

folder = "timing_64"
folder_dir = os.path.join(pulsar_dir,folder)
os.chdir(folder_dir)

#F scrunch the data, comment out once done
p = sproc.Popen("pam -F -e TpF_64 2*Tpf128_64", shell=True)
p.wait()


'''
#1D timing
p = sproc.Popen("pat -A FDM -f tempo2 -s /fred/oz002/users/mmiles/templates/msp_templates/"+pulsar+".std 2*Tpf128 > "+pulsar+".tim1D", shell=True)
p.wait()
p = sproc.Popen("cp *.tim1D /fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/1Dtims", shell=True)
#2D timing
p = sproc.Popen("pat -A FDM -f tempo2 -s /fred/oz002/users/mmiles/templates/2D_Templates/Fscrunched/*"+pulsar+"* 2*Tpf128 > "+pulsar+".tim2D", shell=True)
p.wait()
p = sproc.Popen("cp *.tim2D /fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/2DFscrunched_tims", shell=True)

#F srunched data
'''
p = sproc.Popen("pat -A FDM -f tempo2 -s /fred/oz002/users/mmiles/templates/msp_templates/"+pulsar+".std 2*TpF_64 > "+pulsar+"_F.tim1D_64", shell=True)
p.wait()
p = sproc.Popen("cp *_F.tim1D_64 /fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/1Dtims_F_64", shell=True)
p.wait()
'''
#2D timing
p = sproc.Popen("pat -A FDM -f tempo2 -s /fred/oz002/users/mmiles/templates/2D_Templates/Fscrunched/*"+pulsar+"* 2*TpF > "+pulsar+"_F.tim2D", shell=True)
p.wait()
p = sproc.Popen("cp *_F.tim2D /fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/2DFscrunched_tims_F", shell=True)
'''
#pat portrait timing
#Only works if you submit a dedispersed file
#Currently takes an J0023+0923 as an incorrect portrait to time with
'''
p = sproc.Popen("pat -A FDM -f tempo2 -P -s /fred/oz002/users/mmiles/templates/2D_Templates/Template_repo/2D.portrait."+pulsar+".Tp.paz.norm.8subbands 2*Tpf128_256 > "+pulsar+".highsnrtim", shell=True)
p.wait()
p = sproc.Popen("cp *highsnrtim /fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/highsnr_256", shell=True)
p.wait()
'''
'''
p = sproc.Popen("pat -A FDM -f tempo2 -P -s /fred/oz002/users/mmiles/templates/2D_Templates/Template_repo/2D.portrait."+pulsar+".Tp.paz.norm.ddisp 2*TpF > "+pulsar+".portrait_tim_F", shell=True)
p.wait()
p = sproc.Popen("cp *portrait_tim_F /fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/2Dportrait_tims_F", shell=True)
p.wait()
'''
'''
#Try and redo the bad portrait timing
p = sproc.Popen("pat -A FDM -f tempo2 -P -s /fred/oz002/users/mmiles/templates/2D_Templates/bad_portraits/2D.portrait."+pulsar+".Tp.paz.norm.8subbands 2*Tpf128_256 > "+pulsar+".highsnrtim", shell=True)
p.wait()
p = sproc.Popen("cp *highsnrtim /fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/highsnr_256", shell=True)
p.wait()
'''