import os
import numpy as np 
#import pandas as pd
import glob
#from pathlib import Path
import errno
import sys
#from astropy.table import Table
#from astropy.io import ascii

print('this is the update script for creating the initial template data')

#Changing directory
chdirpath1 = "/fred/oz002/users/mmiles/templates/"
os.chdir(chdirpath1)

#cwd = os.getcwd()
#targets = open("the_rest.list")
pulsar = sys.argv[1]
print(pulsar)
#for pulsar in targets:
#pulsar = pulsar.strip(' \n')
#print({pulsar})

#Make a directory for the data under MATTIME
pulsar_dir = os.path.join(chdirpath1, pulsar)

#Creates a timing directory
try:
    os.mkdir(os.path.join(pulsar_dir,"timing"))
except FileExistsError:
    pass

timing_dir = os.path.join(pulsar_dir,"timing")
#Change into the directory where all the data is
timing = "/fred/oz005/timing/"

#Move into the MEERTIME timing directory
os.chdir(timing)
print('In this directory',os.getcwd())
#In MEERTIME timing directory
pulsarpath = os.path.join(timing, pulsar)

#Move into the pulsar directory with command below
os.chdir(pulsarpath)
#In individual pulsar directory
print('In this directory', os.getcwd())

#Create a for loop for the observations and roll through these
for obs in sorted(os.listdir(pulsarpath)):
    observationpath = os.path.join(pulsarpath,obs)
    #Move into the direcotry for the individual observation
    os.chdir(observationpath)
    print('In this directory', os.getcwd())
    #In individual pulsar directory
    
    #Move into the beamno directory
    beamno = os.listdir(observationpath)[0]
    beamnopath = os.path.join(observationpath, beamno)
    #Move into the directory for the beam number
    os.chdir(beamnopath)
    print('In this directory', os.getcwd())
    
    #Move into the frequency directory
    freq = os.listdir(beamnopath)[0]
    freqpath = os.path.join(beamnopath, freq)
    #Move into the directory for the frequency
    os.chdir(freqpath)
    print('In this directory', os.getcwd())
    
    #Set up file count system
    filecount = len(glob.glob1(freqpath, "*.ar"))
    #print('there are %s files in observation %s for pulsar %s' % (filecount, obs, pulsar))
    
    #Okay, now create the symbolic links
    print('creating soft links and directory')
    
    #Make a directory in MATTIME based on the information in the MEERTIME directory traced above
    #Make an if path to detect if there is already a .linked file present
    #checkfile2 = mkdirpath2+'/done.txt'
    #print(checkfile2)
    #if os.path.isfile(checkfile2):
    #    print(' done.txt exists')
    #    print('already copied/linked %s archives for %s' %(filecount, obs))
    #else:
        #print('does not exist')
        #Creating soft links to the MEERTIME directory from MATTIME
    for archive in os.listdir(freqpath):
        try:
            os.symlink(os.path.join(freqpath, archive), os.path.join(timing_dir, archive))
        except FileExistsError:
            pass
    
os.chdir(timing_dir)
#This cleans the .ar files and changes them to .r
for archives in sorted(os.listdir(timing_dir)):
    if archives.endswith(".ar"):
        if not os.path.isfile(archives.strip("ar")+"r"):
            os.system("paz -r -e r "+archives)
#p and T scrunch
for archives in sorted(os.listdir(timing_dir)):
    if archives.endswith(".r"):
        if not os.path.isfile(archives.strip("r")+"Tp"):
            os.system("pam -Tp -e Tp "+archives)
#F scrunch down to 8 subbands
for archives in sorted(os.listdir(timing_dir)):
    if archives.endswith(".Tp"):
        if not os.path.isfile(archives.strip("Tp")+"Tpf128"):
            os.system("pam -f128 -e Tpf128 "+archives)

for archives in sorted(os.listdir(timing_dir)):
    if archives.endswith(".Tp"):
        if not os.path.isfile(archives.strip("Tp")+"TpF"):
            os.system("pam -F -e TpF "+archives)

