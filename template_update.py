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
chdirpath1 = "/fred/oz002/users/mmiles/templates"
os.chdir(chdirpath1)

#cwd = os.getcwd()
#targets = open("the_rest.list")
pulsar = sys.argv[1]
#for pulsar in targets:
#pulsar = pulsar.strip(' \n')
#print({pulsar})

#Make a directory for the data under MATTIME
mkdirpath1 = os.path.join(chdirpath1, pulsar)

#This exception just skips over the pulsars that are already written
#try:
#    os.mkdir(mkdirpath1)
#except OSError as exc:
#    if exc.errno != errno.EEXIST:
#        raise
#    pass
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
for obs in os.listdir(pulsarpath):
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
    mkdirpath2 = os.path.join(mkdirpath1, obs, beamno, freq)
    try:
        os.makedirs(mkdirpath2)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass
    #Make an if path to detect if there is already a .linked file present
    print('currently in directory: ', os.getcwd())
    checkfile2 = mkdirpath2+'/done.txt'
    print(checkfile2)
    if os.path.isfile(checkfile2):
        print(' done.txt exists')
        print('already copied/linked %s archives for %s' %(filecount, obs))
    else:
        print('does not exist')
        #Creating soft links to the MEERTIME directory from MATTIME
        for archive in os.listdir(freqpath):
            os.symlink(os.path.join(freqpath, archive), os.path.join(mkdirpath2, archive))
        checkfile = mkdirpath2 + "/" + "done.txt" 
        with open(checkfile,"w") as x:
            x.write("this process has already been done")

