#This code is for quickly fixing the templates that broke through the -W tag
import os 
import sys

MainDir = "/fred/oz002/users/mmiles/templates/"
os.chdir(MainDir)

pulsar = sys.argv[1]

#for pulsar in os.listdir(MainDir):
#    if pulsar.startswith("J"):
        
#Change to requested pulsar directory
pulsar_dir = os.path.join(MainDir,pulsar)
os.chdir(pulsar_dir)

#Makes the directory for the files to live in
#os.system("mkdir Tf32p")

Tf32p_dir = os.path.join(pulsar_dir,"Tf32p")


os.chdir(Tf32p_dir)

os.system("psrsmooth grand.TFp")
os.system("mv grand.TFp.sm "+pulsar+".std")
os.system("cp "+pulsar+".std /fred/oz002/users/mmiles/templates/staging")