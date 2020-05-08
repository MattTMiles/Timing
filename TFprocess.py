import os
import glob
import sys

#Let a user input a pulsar and observation to do this script indivdually

MainDir = "/fred/oz002/users/mmiles/templates/"
os.chdir(MainDir)

#    pulsar = input("Input the pulsar to be investigated:")
#    obs = input("Input the observation to be investigated:")

pulsar = sys.argv[1]

#for pulsar in os.listdir(MainDir):
#    if pulsar.startswith("J"):
        #Creating reference file to keep track of what's been done, kept in the main directory
os.chdir(MainDir)

#Change to requested pulsar directory
pulsar_dir = os.path.join(MainDir,pulsar)
os.chdir(pulsar_dir)

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

                #Creates a p scrunched version
                #os.system("pam -p -e mohsenp *mohsen")
                #Creates a p and f scrunched version
                #os.system("pam -F -e mohsenFp *mohsenp")
                
                #Adds to create an observation F and p scrunched version
                os.system("psradd *mohsenFp -o "+obs+".Fp")
                #Adds to create an observation T and P scrunched version
                #os.system("psradd -T *mohsenp -o "+obs+".Tp")

                #F scrunches the T scrunched version into 32 channels
                #os.system("pam -f32 -e Tf32p *.Tp")

                #os.system("mv *.Tf32p "+pulsar_dir+"/Tf32p")
                os.system("mv *.Fp "+pulsar_dir+"/Fp")

os.chdir(os.path.join(pulsar_dir,"Fp"))
os.system("pam -t8 -e Fpt8 *.Fp")
os.system("pam -T -e FpT *.Fp")