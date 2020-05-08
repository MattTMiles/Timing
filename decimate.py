import os

def decimate(pulsar, obs):
    MainDir = "/fred/oz002/users/mmiles/timing/"

    os.chdir(MainDir)

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

    for files in os.listdir(freq_dir):
        if files.endswith(".r"):
            #p scrunches and f scrunches into 32 subbands, then changes the extension to pf32
            os.system("pam -p -f 32 -e pf32 "+files)
            
            #Removes any files left with the .r extension
            os.system("rm "+files)
 
        #Below joins all 8 second periods into a single file
        os.system("psradd -o "+obs_dir+".pf32 *.pf32")

    #Removes the files that start with 2 and end with .pf32
    os.system("rm 2*.pf32")
    #Writes a check file to show that decimate has acted on the observation
    checkfile = freq_dir + "/" + "obs.decimated"
    with open(checkfile,"w") as x:
        x.write("this process has already been done")
    
    #Change into the pulsar directory to act on the .pf32 file
    os.chdir(pulsar_dir)
    
    #Creates a version that is integrated in frequency and given the extension F
    os.system("pam -F "+obs_dir+".pf32 -e F")

    #Creates a version that is integrated in time and given the extension T
    os.system("pam -T "+obs_dir+".pf32 -e T")
   
    #Makes a beep to signal its done
    print('\007')
