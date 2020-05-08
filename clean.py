import os
import glob

#Let a user input a pulsar and observation to do this script indivdually

def clean(pulsar,obs):
    MainDir = "/fred/oz002/users/mmiles/timing/"

    os.chdir(MainDir)

#    pulsar = input("Input the pulsar to be investigated:")
#    obs = input("Input the observation to be investigated:")

    #Change to requested pulsar directory
    pulsar_dir = os.path.join(MainDir,pulsar)
    os.chdir(pulsar_dir)

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

    #This uses paz on each subintergration in the directory, and rewrites them with the extension .r

    for files in os.listdir(os.getcwd()):
        if files.endswith(".ar"):
            os.system("paz -r -e r "+files)
            #Removes any files that still have a .ar extension attached
            os.system("rm "+files)
    #Leaves an artefact in the file showing that the observation has been cleaned
    checkfile = freq_dir + "/" + "obs.cleaned"
    with open(checkfile,"w") as x:
        x.write("this process has already been done") 
    
    
