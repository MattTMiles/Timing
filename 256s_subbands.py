#This creates a scaled 256s median subband timing comparison for an input pulsar name

import numpy as np
import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import sys
import subprocess as sproc
from tqdm import tqdm

parent_dir = '/fred/oz002/users/mmiles/templates'
#pulsar_dir = os.path.join(parent_dir,pulsar)
#timing_dir = os.path.join(pulsar_dir,'timing')
portrait_dir = '/fred/oz002/users/mmiles/templates/2D_Templates/2D_ddisp'
patfile_dir = '/fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/2Dportrait_tims'

subband_timing = []

d1=[]
d2=[]
d3=[]
d4=[]
d5=[]
d6=[]
d7=[]
d8=[]

meds1 = []
meds2 = []
meds3 = []
meds4 = []
meds5 = []
meds6 = []
meds7 = []
meds8 = []

sigmas1 = []
sigmas2 = []
sigmas3 = []
sigmas4 = []
sigmas5 = []
sigmas6 = []
sigmas7 = []
sigmas8 = []

toadf = []
broken = []

os.chdir(patfile_dir)
for timfile in sorted(os.listdir(patfile_dir)):
    if timfile.startswith('J'):
        pulsar = os.path.splitext(timfile)[0]
        print(pulsar)

        try:
            activedata = np.loadtxt(timfile, usecols=3, skiprows=1)
        except:
            broken.append(pulsar)
            continue

        subband_1 = activedata[::8]
        subband_2 = activedata[1::8]
        subband_3 = activedata[2::8]
        subband_4 = activedata[3::8]
        subband_5 = activedata[4::8]
        subband_6 = activedata[5::8]
        subband_7 = activedata[6::8]
        subband_8 = activedata[7::8]

        med_1, med_2, med_3, med_4, med_5, med_6, med_7, med_8 = \
            np.median(subband_1), np.median(subband_2), np.median(subband_3), np.median(subband_4), \
                np.median(subband_5), np.median(subband_6), np.median(subband_7), np.median(subband_8)

        meds1.append(med_1)
        meds2.append(med_2)
        meds3.append(med_3)
        meds4.append(med_4)
        meds5.append(med_5)
        meds6.append(med_6)
        meds7.append(med_7)
        meds8.append(med_8)

        Tobs = len(activedata)
        sigma256_1 = med_1/np.sqrt(Tobs/256)
        sigma256_2 = med_2/np.sqrt(Tobs/256)
        sigma256_3 = med_3/np.sqrt(Tobs/256)
        sigma256_4 = med_4/np.sqrt(Tobs/256)
        sigma256_5 = med_5/np.sqrt(Tobs/256)
        sigma256_6 = med_6/np.sqrt(Tobs/256)
        sigma256_7 = med_7/np.sqrt(Tobs/256)
        sigma256_8 = med_8/np.sqrt(Tobs/256)

        sigmas1.append(sigma256_1)
        sigmas2.append(sigma256_2)
        sigmas3.append(sigma256_3)
        sigmas4.append(sigma256_4)
        sigmas5.append(sigma256_5)
        sigmas6.append(sigma256_6)
        sigmas7.append(sigma256_7)
        sigmas8.append(sigma256_8)

        toadf.append([pulsar, med_1, sigma256_1, med_2, sigma256_2, med_3, sigma256_3, med_4, sigma256_4, \
            med_5, sigma256_5, med_6, sigma256_6, med_7, sigma256_7, med_8, sigma256_8])



toa_labels = ['Pulsar','subband_median1', 'subband_median1_256', 'subband_median2', 'subband_median2_256','subband_median3', 'subband_median3_256',\
    'subband_median4', 'subband_median4_256','subband_median5', 'subband_median5_256','subband_median6', 'subband_median6_256',\
        'subband_median7', 'subband_median7_256','subband_median8', 'subband_median8_256']

df_toa = pd.DataFrame(toadf, columns = toa_labels)

df_toa.to_pickle('256scaled_subbandtoas.pkl')

#The first half of the broken array is where the tim files are empty, the second half is where the tim files are filled with 0's
broken.extend(df_toa[df_toa['subband_median1']==0]['Pulsar'].tolist())

#Wipe out the 0 values so they exhibit as NA's for plotting
plotsigmas1 = sigmas1
plotsigmas1[plotsigmas1==0] = np.nan

plotsigmas2 = sigmas2
plotsigmas2[plotsigmas2==0] = np.nan

plotsigmas3 = sigmas3
plotsigmas3[plotsigmas3==0] = np.nan

plotsigmas4 = sigmas4
plotsigmas4[plotsigmas4==0] = np.nan

plotsigmas5 = sigmas5
plotsigmas5[plotsigmas5==0] = np.nan

plotsigmas6 = sigmas6
plotsigmas6[plotsigmas6==0] = np.nan

plotsigmas7 = sigmas7
plotsigmas7[plotsigmas7==0] = np.nan

plotsigmas8 = sigmas8
plotsigmas8[plotsigmas8==0] = np.nan

t = [892.671000,1015.465000,1115.816000,1238.280000,1346.873000,1444.453000,1522.836000,1663.671000]
cmap = plt.get_cmap('viridis')
norm = mpl.colors.Normalize(vmin=800,vmax=1700)
sm=plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cmapt = (np.array(t)-800)/900

fig, ax = plt.subplots() 
ax.scatter(plotsigmas1, [1]*len(plotsigmas1), color = cmap(cmapt[0]))
ax.scatter(plotsigmas2, [2]*len(plotsigmas2), color = cmap(cmapt[1]))
ax.scatter(plotsigmas3, [3]*len(plotsigmas3), color = cmap(cmapt[2]))
ax.scatter(plotsigmas4, [4]*len(plotsigmas4), color = cmap(cmapt[3]))
ax.scatter(plotsigmas5, [5]*len(plotsigmas5), color = cmap(cmapt[4]))
ax.scatter(plotsigmas6, [6]*len(plotsigmas6), color = cmap(cmapt[5]))
ax.scatter(plotsigmas7, [7]*len(plotsigmas7), color = cmap(cmapt[6]))
ax.scatter(plotsigmas8, [8]*len(plotsigmas8), color = cmap(cmapt[7]))

ax.set(title= 'Subband Median Uncertainty (256s)', xlabel=r'$\mathrm{256s\/ scaled\/ median\/ uncertainty}\/ (\mu s)$', ylabel='Sub-band', xscale = 'log')
cbar = plt.colorbar(sm,ticks=np.linspace(800,1700,10))
cbar.set_label('Frequency')
fig.tight_layout()
plt.show()
