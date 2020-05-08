#This code enters the pulsar directories for the templates, and: 
# 1. Changes their names to replace a '.' with a '_" so a command will work
# 2. Activates a pam command that creates a .sh script that will rotate the pulse profile 
# 3. Activates the .sh script so perfectly aligned profiles are created
# 4. psradds these profiles together
# 5. Smooths these profiles so that they can be used as standards

import os
import sys
import subprocess
import shlex

MainDir = "/fred/oz002/users/mmiles/templates/"
os.chdir(MainDir)

ActiveDir = "/fred/oz002/users/mmiles/templates/1obs_smoothed/"

pulsar = sys.argv[1]

#for pulsar in os.listdir(MainDir):
#    if pulsar.startswith("J"):
pulsar_dir = os.path.join(MainDir, pulsar)
os.chdir(pulsar_dir)

dir_775 = os.path.join(pulsar_dir,"775")
dir_856 = os.path.join(pulsar_dir,"856")
dir_642 = os.path.join(pulsar_dir,"642")

if os.path.isdir(dir_775):
    os.chdir(dir_775)
    for entries in os.listdir(os.getcwd()):
        if entries.startswith("1D."):
            #Replaces the first . with _
            replace = entries.replace(".","_")
            os.system("mv "+entries+" "+replace)
    #Creates the list of files to rotate
    os.system("ls 1D* >> rot.list")
    #Creates the script to rotate the files 
    #The backslashes in the gawk command are important as they pass the text properly
    os.system("pat -R -s /fred/oz002/users/mmiles/templates/1obs_smoothed/"+pulsar+".std -M rot.list | gawk '{print \"pam -e DSFTR -r\", $4, $1}' > make_rot.sh")
    #Activates the .sh script
    os.system("sh make_rot.sh")
    #Adds the aligned files together
    os.system("psradd *DSFTR -o "+pulsar+"_added_775")
    #Creates a smoothed version of the added file
    os.system("psrsmooth -W *added_775")
    #Moves this back into the parent directory
    os.system("mv *sm "+pulsar_dir+"/")

if os.path.isdir(dir_856):
    os.chdir(dir_856)
    for entries in os.listdir(os.getcwd()):
        if entries.startswith("1D."):
            #Replaces the first . with _
            replace = entries.replace(".","_")
            os.system("mv "+entries+" "+replace)
    #Creates the list of files to rotate
    os.system("ls 1D* >> rot.list")
    #Creates the script to rotate the files 
    os.system("pat -R -s /fred/oz002/users/mmiles/templates/1obs_smoothed/"+pulsar+".std -M rot.list | gawk '{print \"pam -e DSFTR -r\", $4, $1}' > make_rot.sh")
    #Activates the .sh script
    os.system("sh make_rot.sh")
    #Adds the aligned files together
    os.system("psradd *DSFTR -o "+pulsar+"_added_856")
    #Creates a smoothed version of the added file
    os.system("psrsmooth -W *added_856")
    #Moves this back into the parent directory
    os.system("mv *sm "+pulsar_dir+"/")

if os.path.isdir(dir_642):
    os.chdir(dir_642)
    for entries in os.listdir(os.getcwd()):
        if entries.startswith("1D."):
            #Replaces the first . with _
            replace = entries.replace(".","_")
            os.system("mv "+entries+" "+replace)
    #Creates the list of files to rotate
    os.system("ls 1D* >> rot.list")
    #Creates the script to rotate the files 
    os.system("pat -R -s /fred/oz002/users/mmiles/templates/1obs_smoothed/"+pulsar+".std -M rot.list | gawk '{print \"pam -e DSFTR -r\", $4, $1}' > make_rot.sh")
    #Activates the .sh script
    os.system("sh make_rot.sh")
    #Adds the aligned files together
    os.system("psradd *DSFTR -o "+pulsar+"_added_642")
    #Creates a smoothed version of the added file
    os.system("psrsmooth -W *added_642")
    #Moves this back into the parent directory
    os.system("mv *sm "+pulsar_dir+"/")
