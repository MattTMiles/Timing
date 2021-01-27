import os
import numpy as np
import subprocess as sproc 


#Specify parent directory
MainDir = "/fred/oz002/users/mmiles/templates/2D_Templates"
os.chdir(MainDir)

meerpipe = '/fred/oz005/users/aparthas/MSP_Census/PTA'
os.chdir(meerpipe)

for pulsar in os.listdir(meerpipe):
    if pulsar.startswith('J'):
        if not os.path.isdir(MainDir+'/'+pulsar):
            os.mkdir(MainDir+'/'+pulsar)
            pulsardir = os.path.join(meerpipe,pulsar)
            for obs in os.listdir(pulsardir):
                obsdir = os.path.join(pulsardir,obs)
                os.chdir(obsdir)
                for beam in os.listdir(obsdir):
                    beamdir = os.path.join(obsdir,beam)
                    os.chdir(beamdir)
                    for freq in os.listdir(beamdir):
                        freqdir = os.path.join(beamdir,freq)
                        os.chdir(freqdir)
                        p = sproc.Popen('cp *add '+MainDir+'/'+pulsar, shell=True)
                        p.wait()
                        print(pulsar+'added to the collection')




