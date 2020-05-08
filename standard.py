import os

#Specify parent directory
MainDir = "/fred/oz002/users/mmiles/templates/"
os.chdir(MainDir)

#Move through pulsar directories
for pulsar in os.listdir(MainDir):
    if pulsar.startswith("J"):
        pulsar_dir = os.path.join(MainDir,pulsar)
        os.chdir(pulsar_dir)
        if not os.path.isfile("highsnr_standardsfin"):

            os.system("echo done > highsnr_standardsfin")
            #Specify the directories for the different possible bandwidths
            dir_856 = os.path.join(pulsar_dir,"856")
            dir_775 = os.path.join(pulsar_dir,"775")
            dir_642 = os.path.join(pulsar_dir,"642")

            #Search and change into the relevant bandwidth directories
            if os.path.isdir(dir_856):
                os.chdir(dir_856)
                os.chdir(os.path.join(dir_856, "high_snr"))
                os.system("pam -T -m 1D*")
                os.system("psradd 1D* -o 1D."+pulsar+".856_highsnr")
                os.system("pam -T -m 1D."+pulsar+".856_highsnr")
                os.system("mv 1D."+pulsar+".856_highsnr "+pulsar_dir)
                os.chdir(pulsar_dir)

            if os.path.isdir(dir_775):
                os.chdir(dir_775)
                os.chdir(os.path.join(dir_775, "high_snr"))
                os.system("pam -T -m 1D*")
                os.system("psradd 1D* -o 1D."+pulsar+".775_highsnr")
                os.system("pam -T -m 1D."+pulsar+".775_highsnr")
                os.system("mv 1D."+pulsar+".775_highsnr "+pulsar_dir)
                os.chdir(pulsar_dir)

            if os.path.isdir(dir_642):
                os.chdir(dir_642)
                os.chdir(os.path.join(dir_642, "high_snr"))
                os.system("pam -T -m 1D*")
                os.system("psradd 1D* -o 1D."+pulsar+".642_highsnr")
                os.system("pam -T -m 1D."+pulsar+".642_highsnr")
                os.system("mv 1D."+pulsar+".642_highsnr "+pulsar_dir)
                os.chdir(pulsar_dir)
        
        
