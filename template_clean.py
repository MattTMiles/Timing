import os
import glob

#Let a user input a pulsar and observation to do this script indivdually


MainDir = "/fred/oz002/users/mmiles/templates/"
os.chdir(MainDir)

#    pulsar = input("Input the pulsar to be investigated:")
#    obs = input("Input the observation to be investigated:")

for pulsar in os.listdir(MainDir):
    if pulsar.startswith("J"):
        #Creating reference file to keep track of what's been done, kept in the main directory
        os.chdir(MainDir)
        os.system("echo "+pulsar+" >> donefile")
        
        #Change to requested pulsar directory
        pulsar_dir = os.path.join(MainDir,pulsar)
        os.chdir(pulsar_dir)
        
        for obs in os.listdir(pulsar_dir):
            if not obs.endswith(".mohsened"):
                if not os.path.isfile(obs+".mohsened"):
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

                        #This uses cleans each subintergration in the directory, and rewrites them with the extension .mohsen
                        #count=os.system("`ls -1 *.mohsen 2>/dev/null | wc -l`")
                        #if os.system("find *mohsen | wc -l") == 0:
                        dutycycle = os.system("cat "+pulsar_dir+"/dutycycle")
                        os.system("python /fred/oz005/users/mshamoha/federico/rfihunter_nogate.py *ar "+str(dutycycle))

                        os.chdir(pulsar_dir)

                        checkfile = pulsar_dir + "/" +obs+".mohsened"
                        with open(checkfile,"w") as x:
                            x.write("this obs is mohsened")
            
        
