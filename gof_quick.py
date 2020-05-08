import os
import sys

# Quickly creates a goodness-of-fit comparison between the template
#and a randomly selected T,F scrunched archive

MainDir = "/fred/oz002/users/mmiles/templates/"
os.chdir(MainDir)
pulsar = sys.argv[1]
#for pulsar in os.listdir(MainDir):
#    if pulsar.startswith("J"):
#        if not pulsar.startswith("J0437"):
#Change to requested pulsar directory
pulsar_dir = os.path.join(MainDir,pulsar)
os.chdir(pulsar_dir)
    
#This creates a comparison file to see the improvement from previous standard profiles
#Sets up a standard test file for comparison between the new and old standards
testfile = os.popen("ls /fred/oz002/users/mmiles/timing/"+pulsar+"/*.T | head -1").read()
testfile = testfile.strip("\n")
os.system("pam -F -e TF "+str(testfile))
testfile = str(testfile)+"F"
#Retrieve the goodness-of-fit from the old standard
#old_gof = os.popen("pat -A FDM -f 'tempo2 IPTA' -C 'gof' -s /fred/oz005/timing_processed/meertime_templates/"+pulsar+".std "+str(testfile)+" | awk '{print $(NF)}'").read()
#old_gof = old_gof.strip("1\n")

#Retrieve the goodness-of-fit from the new standard
#snrpick = os.popen("psrstat -c snr=pdmp -j FTpD -c snr -Q 1D* | sort -k2n | awk '{print $(NF-1)}' | tail -1").read().strip("\n")
#os.system("psrsmooth "+snrpick)
#Try this with the smoothed version
#new_gof = os.popen("pat -A FDM -f 'tempo2 IPTA' -C 'gof' -s /fred/oz002/users/mmiles/templates/"+pulsar+"/"+snrpick+".sm "+str(testfile)+" | awk '{print $(NF)}'").read()
#Try this with the non-smoothed
#new_gof = os.popen("pat -A FDM -f 'tempo2 IPTA' -C 'gof' -s /fred/oz002/users/mmiles/templates/"+pulsar+"/"+snrpick+" "+str(testfile)+" | awk '{print $(NF)}'").read()
#new_gof = new_gof.strip("1\n")

#Collects the gof for all the profiles in the folder
for files in os.listdir(pulsar_dir):
    if files.startswith("1D"):
        gof = os.popen("pat -A FDM -f 'tempo2 IPTA' -C 'gof' -s /fred/oz002/users/mmiles/templates/"+pulsar+"/"+files+" "+str(testfile)+" | awk '{print ($NF)}'").read().strip("\n")
        gof = gof.splitlines()[1]
        #gof = os.popen("pat -A FDM -f 'tempo2 IPTA' -C 'gof' -s /fred/oz002/users/mmiles/templates/"+pulsar+"/"+files+" "+str(testfile)).read().strip("\n")
        #print(files, gof[2:])

        #Uncomment below if you want a comparison with the previous standard
        old_gof = os.popen("pat -A FDM -f 'tempo2 IPTA' -C 'gof' -s /fred/oz005/timing_processed/meertime_templates/"+pulsar+".std "+str(testfile)+" | awk '{print $(NF)}'").read().strip("\n")
        old_gof = old_gof.splitlines()[1]
        print(files,"old gof:",old_gof, "new gof:",gof)


#os.system("pat -A FDM -f 'tempo2 IPTA' -C 'gof' -s /fred/oz002/users/mmiles/templates/"+pulsar+"/1D* "+str(testfile))