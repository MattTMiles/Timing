import os


MainDir = "/fred/oz002/users/mmiles/templates/"
os.chdir(MainDir)

ActiveDir = "/fred/oz002/users/mmiles/templates/aligned_smoothed/"

for pulsar in os.listdir(MainDir):
    if pulsar.startswith("J"):
        #Change to requested pulsar directory
        #pulsar_dir = os.path.join(MainDir,pulsar)
        #os.chdir(pulsar_dir)
            
        #This creates a comparison file to see the improvement from previous standard profiles
        #Sets up a standard test file for comparison between the new and old standards
        testfile = os.popen("ls /fred/oz002/users/mmiles/timing/"+pulsar+"/*.T | head -1").read()
        testfile = testfile.strip("\n")
        os.system("pam -F -e TF "+str(testfile))
        testfile = str(testfile)+"F"
        #Retrieve the goodness-of-fit from the old standard
        old_gof = os.popen("pat -A FDM -f 'tempo2 IPTA' -C 'gof' -s /fred/oz005/timing_processed/meertime_templates/"+pulsar+".std "+str(testfile)+" | awk '{print $(NF)}'").read()
        old_gof = old_gof.strip("\n")
        try:
            old_gof = old_gof.splitlines()[1]
        except IndexError:
            old_gof = pulsar+" didn't work"
        #Retrieve the goodness-of-fit from the new standard
        #snrpick = os.popen("psrstat -c snr=pdmp -j FTpD -c snr -Q 1D* | sort -k2n | awk '{print $(NF-1)}' | tail -1").read().strip("\n")
        
        #os.system("psrsmooth "+snrpick)
        #Try this with the smoothed version
        #new_gof = os.popen("pat -A FDM -f 'tempo2 IPTA' -C 'gof' -s /fred/oz002/users/mmiles/templates/"+pulsar+"/"+snrpick+".sm "+str(testfile)+" | awk '{print $(NF)}'").read()
        
        #Try this with the non-smoothed
        new_gof = os.popen("pat -A FDM -f 'tempo2 IPTA' -C 'gof' -s /fred/oz002/users/mmiles/templates/msp_templates/"+pulsar+".std "+str(testfile)+" | awk '{print $(NF)}'").read()
        new_gof = new_gof.strip("\n")
        try:
            new_gof = new_gof.splitlines()[1]
        except IndexError:
            new_gof = pulsar+" didn't work"

        #Writes the output to the comparison file
        os.system("echo "+pulsar+" "+str(old_gof)+" "+str(new_gof)+" >> "+MainDir+"/aligned_smoothed/current_compfile")
        #try:
        #    if float(old_gof) < float(new_gof):
        #        os.system("echo "+pulsar+" "+str(new_gof)+">> "+MainDir+"/bad_standards")
        #except ValueError:
        #    os.system("echo "+pulsar+" valuerror >> "+MainDir+"/bad_standards")