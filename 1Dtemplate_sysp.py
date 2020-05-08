import os
import glob
import sys

#Let a user input a pulsar and observation to do this script indivdually
#This is a modified verison of the 1Dtemplate script that allows the user to specify a pulsar using sys.argv

MainDir = "/fred/oz002/users/mmiles/templates/"
os.chdir(MainDir)

pulsar = sys.argv[1]
#for pulsar in os.listdir(MainDir):
#    if pulsar.startswith("J"):
#Creating reference file to keep track of what's been done, kept in the main directory
os.chdir(MainDir)
os.system("echo "+pulsar+" >> 1D_donefile")

#Change to requested pulsar directory
pulsar_dir = os.path.join(MainDir,pulsar)
os.chdir(pulsar_dir)

for obs in os.listdir(pulsar_dir):
    if not obs.endswith(".mohsened"):
        #if not os.path.isfile(obs+".mohsened"):
        if obs.startswith("2"):
            #Change to requested observation directory
            obs_dir = os.path.join(pulsar_dir, obs)

            #Move through beam number directory
            beamno = os.listdir(obs_dir)[0]
            beamno_dir = os.path.join(obs_dir, beamno)
            os.chdir(beamno_dir)

            #Move through frequency directory
            freq = os.listdir(beamno_dir)[0]
            freq_dir = os.path.join(beamno_dir, freq)
            os.chdir(freq_dir)

            #This p,F, and T scrunches the data
            os.system("pam -FTp -e mohsenFTp *.mohsen")
            
            #This adds it into a single archive.
            os.system("psradd *.mohsenFTp -o 1D."+obs)

            #This moves the added file up to the pulsar directory
            os.system("mv 1D."+obs+" "+pulsar_dir)
            os.chdir(pulsar_dir)

            #This is for writing a checkfile, currently not needed so commented out
            #checkfile = pulsar_dir + "/" +obs+".added"
            #with open(checkfile,"w") as x:
            #    x.write("this obs is mohsened")

    
