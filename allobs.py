import os
from clean import clean
from decimate import decimate
import sys
#This script will activate clean and decimate on all observations for a single pulsar.
#print "pulsar is:", str(sys.argv[1])

mainDir = "/fred/oz002/users/mmiles/timing"

#Specify which pulsar you want to investigate
pulsar = sys.argv[1] #input("Input the pulsar that you want to analyse: ")
#Convert the answer to a string so it can be added to the path
#pulsar = str(pulsar)
#First pass script: unsure if this will work

#Call the clean.py function on the pulsar and all of its observations
for obs in os.listdir(os.path.join(mainDir, pulsar)):
    clean(pulsar, obs)

#Call the decimate.py function on the cleaned pulsar and all of its observations
for obs in os.listdir(os.path.join(mainDir, pulsar)):
    decimate(pulsar, obs)