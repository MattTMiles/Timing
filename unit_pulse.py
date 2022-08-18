import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import os


main = '/fred/oz002/users/mmiles/templates/2D_Templates/unit_grand'
os.chdir(main)

'''
d={}

for J in os.listdir(os.getcwd()): 
    snr = os.popen("psrstat "+J+" -c snr=pdmp -c snr | awk '{ print $NF }'").read().split('snr=')[1].split('\n')[0] 
    snr = float(snr) 
    time = os.popen("psrstat "+J+" -c length | awk '{ print $NF }'").read().split('length=')[1].split('\n')[0]  
    time = float(time) 
    pulsarname = J.split('_Tf4_tot.ar')[0] 
    freq = os.popen("psrcat "+pulsarname+" -c F0 -x | awk '{print $1}'").read() 
    try: 
        freq = float(freq) 
        pulses = freq*time 
        unit_snr = snr/(np.sqrt(pulses)) 
        d[J] = unit_snr 
    except ValueError: 
        if pulsarname == "J0955-6150":
            freq = 500.15004501350404
        elif pulsarname == "J1652-4838":
            freq = 264.17985364436106
        elif pulsarname == "J2039-3616":
            freq = 305.34351145038164
        elif pulsarname == "J0125-2327":
            freq = 272.0792294716221
        elif pulsarname == "J2150-0326":
            freq = 284.84347850855954
        else:
            freq = 'notwork' 
            d[J] = freq 
'''

perc = {}

for J in os.listdir(os.getcwd()):
    pulsarname = J.split("_Tf4")[0]
    os.chdir('/fred/oz002/users/mmiles/templates/2D_Templates/'+pulsarname)
    obslist = glob.glob("*ar")
    numobs = len(obslist)
    i=0
    for obs in obslist:
        snr = os.popen("psrstat "+obs+" -c snr=pdmp -c snr | awk '{ print $NF }'").read().split('snr=')[1].split('\n')[0]
        snr = float(snr) 
        time = os.popen("psrstat "+obs+" -c length | awk '{ print $NF }'").read().split('length=')[1].split('\n')[0]  
        time = float(time)
        freq = os.popen("psrcat "+pulsarname+" -c F0 -x | awk '{print $1}'").read()

        try: 
            freq = float(freq)
            pulses = freq*time 
            unit_snr = snr/(np.sqrt(pulses))
            if unit_snr > 1:
                i=i+1
            
        except ValueError: 
            if pulsarname == "J0955-6150":
                freq = 500.15004501350404
            elif pulsarname == "J1652-4838":
                freq = 264.17985364436106
            elif pulsarname == "J2039-3616":
                freq = 305.34351145038164
            elif pulsarname == "J0125-2327":
                freq = 272.0792294716221
            elif pulsarname == "J2150-0326":
                freq = 284.84347850855954
            else:
                freq = 'notwork' 
                
                perc[J] = freq
            pulses = freq*time 
            unit_snr = snr/(np.sqrt(pulses))
            if unit_snr > 1:
                i=i+1


    perc[J] = (i/numobs)

