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

folder = "timing"
folder_dir = os.path.join(pulsar_dir,folder)
os.chdir(folder_dir)

timing_256 = os.path.join(pulsar_dir,"timing_256")
timing_64 = os.path.join(pulsar_dir,"timing_64")

#For the 64 and 256 timing
os.chdir(timing_64)
p = sproc.Popen("pat -A FDM -f tempo2 -s /fred/oz002/users/mmiles/templates/msp_templates/"+pulsar+".std 2*Tpf128_64 > "+pulsar+".tim1D_64", shell=True)
p.wait()
p = sproc.Popen("cp *.tim1D_64 /fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/1Dtims_64", shell=True)

p = sproc.Popen("pat -A FDM -f tempo2 -P -s /fred/oz002/users/mmiles/templates/2D_Templates/Template_repo/2D.portrait."+pulsar+".Tp.paz.norm.ddisp 2*Tpf128_64 > "+pulsar+".portrait_tim_64", shell=True)
p.wait()
p = sproc.Popen("cp *portrait_tim_64 /fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/2Dportrait_tims_64", shell=True)
p.wait()

os.chdir(timing_256)
p = sproc.Popen("pat -A FDM -f tempo2 -s /fred/oz002/users/mmiles/templates/msp_templates/"+pulsar+".std 2*Tpf128_256 > "+pulsar+".tim1D_256", shell=True)
p.wait()
p = sproc.Popen("cp *.tim1D_256 /fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/1Dtims_256", shell=True)

p = sproc.Popen("pat -A FDM -f tempo2 -P -s /fred/oz002/users/mmiles/templates/2D_Templates/Template_repo/2D.portrait."+pulsar+".Tp.paz.norm.ddisp 2*Tpf128_256 > "+pulsar+".portrait_tim_256", shell=True)
p.wait()
p = sproc.Popen("cp *portrait_tim_256 /fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/2Dportrait_tims_256", shell=True)
p.wait()