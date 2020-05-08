import os

#Specify parent directory
MainDir = "/fred/oz002/users/mmiles/templates/"
os.chdir(MainDir)

for pulsar in os.listdir(MainDir):
    if pulsar.startswith("J"):
        #Change to requested pulsar directory
        pulsar_dir = os.path.join(MainDir,pulsar)
        os.chdir(pulsar_dir)

        dir_856 = os.path.join(pulsar_dir,"856")
        dir_775 = os.path.join(pulsar_dir,"775")
        dir_642 = os.path.join(pulsar_dir,"642") 

        if os.path.isdir(dir_856):
            os.chdir(dir_856)
            os.mkdir(os.path.join(dir_856,"high_snr"))

        if os.path.isdir(dir_775):
            os.chdir(dir_775)
            os.mkdir(os.path.join(dir_775,"high_snr"))

        if os.path.isdir(dir_642):
            os.chdir(dir_642)
            os.mkdir(os.path.join(dir_642,"high_snr"))
