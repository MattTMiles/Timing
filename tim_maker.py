import os
import sys

pulsar = sys.argv[1]

MainDir = "/fred/oz002/users/mmiles/templates/"
os.chdir(MainDir)

pulsar_dir = os.path.join(MainDir,pulsar)
os.chdir(pulsar_dir)
'''
os.mkdir(os.path.join(pulsar_dir,"Tf32p"))
os.mkdir(os.path.join(pulsar_dir,"Fp"))
for obs in os.listdir(pulsar_dir):
    if not obs.endswith(".mohsened"):
            if obs.startswith("2"):
                obs_dir = os.path.join(pulsar_dir, obs)
                
                #Move through beam number directory
                beamno = os.listdir(obs_dir)[0]
                beamno_dir = os.path.join(obs_dir, beamno)
                os.chdir(beamno_dir)

                #Move through frequency directory
                freq = os.listdir(beamno_dir)[0]
                freq_dir = os.path.join(beamno_dir, freq)
                os.chdir(freq_dir)
                
                os.system("mv *.Tf32p "+pulsar_dir+"/Tf32p")
                os.system("mv *.Fp "+pulsar_dir+"/Fp")
'''
os.chdir(os.path.join(pulsar_dir,"Tf32p"))
os.system("pat -A FDM -f tempo2 -s /fred/oz002/users/mmiles/templates/1obs_smoothed/"+pulsar+".std *.Tf32p > "+pulsar+"_Tpf32.tim")
#os.system("mv "+pulsar+"_Tpf32.tim "+MainDir+"/parfiles/")

os.chdir(os.path.join(pulsar_dir,"Fp"))
os.system("pat -A FDM -f tempo2 -s /fred/oz002/users/mmiles/templates/1obs_smoothed/"+pulsar+".std *.Fp > "+pulsar+"_Fp.tim")
#os.system("mv "+pulsar+"_Fp.tim "+MainDir+"/parfiles/")