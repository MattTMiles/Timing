import os

MainDir = "/fred/oz002/users/mmiles/templates/best"
os.chdir(MainDir)

for pulsar in os.listdir(MainDir):
    if pulsar.startswith("J"):
        pulsar_dir = os.path.join(MainDir, pulsar)
        os.chdir(os.path.join(MainDir, pulsar))
        print(pulsar)
        #best = os.popen("psrstat -c snr=pdmp -j FTp -c snr -Q *.Tp.sm | awk 'NR==1{print $(1)}'").read().strip("\n")
        os.system("cp *std ../standards")
        #os.system("cp "+best+" /fred/oz002/users/mmiles/templates/aligned_smoothed/")
                
        
'''
pulsar = "J1405-4656"
os.chdir(os.path.join(MainDir, pulsar))
print(pulsar)
os.system("mv *added_856.sm "+pulsar+"_aligned.std")
os.system("cp "+pulsar+"_aligned.std /fred/oz002/users/mmiles/templates/aligned_smoothed/")
'''