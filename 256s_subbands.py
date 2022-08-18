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
subparent_dir = '/fred/oz002/users/mmiles/templates/2D_Templates'
portrait_dir = '/fred/oz002/users/mmiles/templates/2D_Templates/2D_ddisp'
patfile_dir = '/fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/2Dportrait_tims'
patfile_dir1D = '/fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/1Dtims'
template_dir = '/fred/oz002/users/mmiles/templates/msp_templates'

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

meds1_5 = []
meds2_5 = []
meds3_5 = []
meds4_5 = []
meds5_5 = []
meds6_5 = []
meds7_5 = []
meds8_5 = []

meds1_10 = []
meds2_10 = []
meds3_10 = []
meds4_10 = []
meds5_10 = []
meds6_10 = []
meds7_10 = []
meds8_10 = []

sigmas1 = []
sigmas2 = []
sigmas3 = []
sigmas4 = []
sigmas5 = []
sigmas6 = []
sigmas7 = []
sigmas8 = []

sigmas1_5 = []
sigmas2_5 = []
sigmas3_5 = []
sigmas4_5 = []
sigmas5_5 = []
sigmas6_5 = []
sigmas7_5 = []
sigmas8_5 = []

sigmas1_10 = []
sigmas2_10 = []
sigmas3_10 = []
sigmas4_10 = []
sigmas5_10 = []
sigmas6_10 = []
sigmas7_10 = []
sigmas8_10 = []

snrs1 = []
snrs2 = []
snrs3 = []
snrs4 = []
snrs5 = []
snrs6 = []
snrs7 = []
snrs8 = []

toadf = []
broken = []

os.chdir(patfile_dir)
for timfile in sorted(os.listdir(patfile_dir)):
    if timfile.startswith('J'):
        pulsar = os.path.splitext(timfile)[0]
        if os.path.isdir(os.path.join(subparent_dir,pulsar)):
            print(pulsar)

            try:
                activedata = np.loadtxt(timfile, usecols=3, skiprows=1)
                snrdata = np.loadtxt(timfile, usecols=6, skiprows=1)
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

            snr1 = snrdata[::8]
            snr2 = snrdata[1::8]
            snr3 = snrdata[2::8]
            snr4 = snrdata[3::8]
            snr5 = snrdata[4::8]
            snr6 = snrdata[5::8]
            snr7 = snrdata[6::8]
            snr8 = snrdata[7::8]

            #Construct the 5snr cutoff
            subband_1_5 = [x for x in subband_1[snr1 > 5]]
            subband_2_5 = [x for x in subband_2[snr2 > 5]]
            subband_3_5 = [x for x in subband_3[snr3 > 5]]
            subband_4_5 = [x for x in subband_4[snr4 > 5]]
            subband_5_5 = [x for x in subband_5[snr5 > 5]]
            subband_6_5 = [x for x in subband_6[snr6 > 5]]
            subband_7_5 = [x for x in subband_7[snr7 > 5]]
            subband_8_5 = [x for x in subband_8[snr8 > 5]]

            #Construct the 10snr cutoff
            subband_1_10 = [x for x in subband_1[snr1 > 10]]
            subband_2_10 = [x for x in subband_2[snr2 > 10]]
            subband_3_10 = [x for x in subband_3[snr3 > 10]]
            subband_4_10 = [x for x in subband_4[snr4 > 10]]
            subband_5_10 = [x for x in subband_5[snr5 > 10]]
            subband_6_10 = [x for x in subband_6[snr6 > 10]]
            subband_7_10 = [x for x in subband_7[snr7 > 10]]
            subband_8_10 = [x for x in subband_8[snr8 > 10]]

            #Full set medians
            med_1, med_2, med_3, med_4, med_5, med_6, med_7, med_8 = \
                np.median(subband_1), np.median(subband_2), np.median(subband_3), np.median(subband_4), \
                    np.median(subband_5), np.median(subband_6), np.median(subband_7), np.median(subband_8)
            
            #>5 snr medians
            med_1_5, med_2_5, med_3_5, med_4_5, med_5_5, med_6_5, med_7_5, med_8_5 = \
                np.median(subband_1_5), np.median(subband_2_5), np.median(subband_3_5), np.median(subband_4_5), \
                    np.median(subband_5_5), np.median(subband_6_5), np.median(subband_7_5), np.median(subband_8_5)
            
            #>10 snr medians
            med_1_10, med_2_10, med_3_10, med_4_10, med_5_10, med_6_10, med_7_10, med_8_10 = \
                np.median(subband_1_10), np.median(subband_2_10), np.median(subband_3_10), np.median(subband_4_10), \
                    np.median(subband_5_10), np.median(subband_6_10), np.median(subband_7_10), np.median(subband_8_10)

            meds1.append(med_1)
            meds2.append(med_2)
            meds3.append(med_3)
            meds4.append(med_4)
            meds5.append(med_5)
            meds6.append(med_6)
            meds7.append(med_7)
            meds8.append(med_8)

            meds1_5.append(med_1_5)
            meds2_5.append(med_2_5)
            meds3_5.append(med_3_5)
            meds4_5.append(med_4_5)
            meds5_5.append(med_5_5)
            meds6_5.append(med_6_5)
            meds7_5.append(med_7_5)
            meds8_5.append(med_8_5)

            meds1_10.append(med_1_10)
            meds2_10.append(med_2_10)
            meds3_10.append(med_3_10)
            meds4_10.append(med_4_10)
            meds5_10.append(med_5_10)
            meds6_10.append(med_6_10)
            meds7_10.append(med_7_10)
            meds8_10.append(med_8_10)

            Tobs = len(activedata)
            sigma256_1 = med_1/np.sqrt(Tobs/256)
            sigma256_2 = med_2/np.sqrt(Tobs/256)
            sigma256_3 = med_3/np.sqrt(Tobs/256)
            sigma256_4 = med_4/np.sqrt(Tobs/256)
            sigma256_5 = med_5/np.sqrt(Tobs/256)
            sigma256_6 = med_6/np.sqrt(Tobs/256)
            sigma256_7 = med_7/np.sqrt(Tobs/256)
            sigma256_8 = med_8/np.sqrt(Tobs/256)

            sigma256_1_5 = med_1_5/np.sqrt(Tobs/256)
            sigma256_2_5 = med_2_5/np.sqrt(Tobs/256)
            sigma256_3_5 = med_3_5/np.sqrt(Tobs/256)
            sigma256_4_5 = med_4_5/np.sqrt(Tobs/256)
            sigma256_5_5 = med_5_5/np.sqrt(Tobs/256)
            sigma256_6_5 = med_6_5/np.sqrt(Tobs/256)
            sigma256_7_5 = med_7_5/np.sqrt(Tobs/256)
            sigma256_8_5 = med_8_5/np.sqrt(Tobs/256)

            sigma256_1_10 = med_1_10/np.sqrt(Tobs/256)
            sigma256_2_10 = med_2_10/np.sqrt(Tobs/256)
            sigma256_3_10 = med_3_10/np.sqrt(Tobs/256)
            sigma256_4_10 = med_4_10/np.sqrt(Tobs/256)
            sigma256_5_10 = med_5_10/np.sqrt(Tobs/256)
            sigma256_6_10 = med_6_10/np.sqrt(Tobs/256)
            sigma256_7_10 = med_7_10/np.sqrt(Tobs/256)
            sigma256_8_10 = med_8_10/np.sqrt(Tobs/256)

            sigmas1.append(sigma256_1)
            sigmas2.append(sigma256_2)
            sigmas3.append(sigma256_3)
            sigmas4.append(sigma256_4)
            sigmas5.append(sigma256_5)
            sigmas6.append(sigma256_6)
            sigmas7.append(sigma256_7)
            sigmas8.append(sigma256_8)

            sigmas1_5.append(sigma256_1_5)
            sigmas2_5.append(sigma256_2_5)
            sigmas3_5.append(sigma256_3_5)
            sigmas4_5.append(sigma256_4_5)
            sigmas5_5.append(sigma256_5_5)
            sigmas6_5.append(sigma256_6_5)
            sigmas7_5.append(sigma256_7_5)
            sigmas8_5.append(sigma256_8_5)

            sigmas1_10.append(sigma256_1_10)
            sigmas2_10.append(sigma256_2_10)
            sigmas3_10.append(sigma256_3_10)
            sigmas4_10.append(sigma256_4_10)
            sigmas5_10.append(sigma256_5_10)
            sigmas6_10.append(sigma256_6_10)
            sigmas7_10.append(sigma256_7_10)
            sigmas8_10.append(sigma256_8_10) 

            snrs1.append(snr1)
            snrs2.append(snr2)
            snrs3.append(snr3)
            snrs4.append(snr4)
            snrs5.append(snr5)
            snrs6.append(snr6)
            snrs7.append(snr7)
            snrs8.append(snr8)

            toadf.append([pulsar, sigma256_1, sigma256_1_5, sigma256_1_10, sigma256_2, sigma256_2_5, sigma256_2_10, sigma256_3, sigma256_3_5, sigma256_3_10, \
                sigma256_4, sigma256_4_5, sigma256_4_10, sigma256_5, sigma256_5_5, sigma256_5_10, sigma256_6, sigma256_6_5, sigma256_6_10, \
                    sigma256_7, sigma256_7_5, sigma256_7_10, sigma256_8, sigma256_8_5, sigma256_8_10])


os.chdir('/fred/oz002/users/mmiles/templates/2D_Templates')

toa_labels = ['Pulsar','subband1_256', 'subband1_256_5', 'subband1_256_10','subband2_256', 'subband2_256_5', 'subband2_256_10','subband3_256', 'subband3_256_5', 'subband3_256_10'\
    ,'subband4_256', 'subband4_256_5', 'subband4_256_10','subband5_256', 'subband5_256_5', 'subband5_256_10','subband6_256', 'subband6_256_5', 'subband6_256_10'\
        ,'subband7_256', 'subband7_256_5', 'subband7_256_10','subband8_256', 'subband8_256_5', 'subband8_256_10']

df_toa = pd.DataFrame(toadf, columns = toa_labels)

df_toa.to_pickle('256scaled_subbandtoas_2D.pkl')

#The first half of the broken array is where the tim files are empty, the second half is where the tim files are filled with 0's
broken.extend(df_toa[df_toa['subband1_256']==0]['Pulsar'].tolist())


portrait_data = pd.read_pickle('256scaled_subbandtoas_2D.pkl')
template_data = pd.read_pickle('256scaled_subbandtoas_1D.pkl')


t = [950.508000,1054.402000,1150.282000,1274.552000,1376.517000,1477.161000,1615.783000,1658.082000]
cmap = plt.get_cmap('viridis')
norm = mpl.colors.Normalize(vmin=800,vmax=1700)
sm=plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cmapt = (np.array(t)-800)/900

fig, ax = plt.subplots() 
ax.scatter(sigmas1, [t[0]]*len(sigmas1), color = cmap(cmapt[0]), s=0.5)
ax.scatter(sigmas2, [t[1]]*len(sigmas2), color = cmap(cmapt[1]), s=0.5)
ax.scatter(sigmas3, [t[2]]*len(sigmas3), color = cmap(cmapt[2]), s=0.5)
ax.scatter(sigmas4, [t[3]]*len(sigmas4), color = cmap(cmapt[3]), s=0.5)
ax.scatter(sigmas5, [t[4]]*len(sigmas5), color = cmap(cmapt[4]), s=0.5)
ax.scatter(sigmas6, [t[5]]*len(sigmas6), color = cmap(cmapt[5]), s=0.5)
ax.scatter(sigmas7, [t[6]]*len(sigmas7), color = cmap(cmapt[6]), s=0.5)
ax.scatter(sigmas8, [t[7]]*len(sigmas8), color = cmap(cmapt[7]), s=0.5)

ax.set(title= 'Subband Median Uncertainty (256s)', xlabel=r'$\mathrm{256s\/ scaled\/ median\/ uncertainty}\/ (\mu s)$', ylabel='Centre Frequency (MHz)', xscale = 'log')
cbar = plt.colorbar(sm,ticks=np.linspace(800,1700,10))
cbar.set_label('Frequency')
fig.tight_layout()

#t = [892.671000,1015.465000,1115.816000,1238.280000,1346.873000,1444.453000,1522.836000,1663.671000]
cmap = plt.get_cmap('viridis')
norm = mpl.colors.Normalize(vmin=800,vmax=1700)
sm=plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cmapt = (np.array(t)-800)/900

fig, ax = plt.subplots() 
ax.scatter(sigmas1_5, [t[0]]*len(sigmas1_5), color = cmap(cmapt[0]), s=0.5)
ax.scatter(sigmas2_5, [t[1]]*len(sigmas2_5), color = cmap(cmapt[1]), s=0.5)
ax.scatter(sigmas3_5, [t[2]]*len(sigmas3_5), color = cmap(cmapt[2]), s=0.5)
ax.scatter(sigmas4_5, [t[3]]*len(sigmas4_5), color = cmap(cmapt[3]), s=0.5)
ax.scatter(sigmas5_5, [t[4]]*len(sigmas5_5), color = cmap(cmapt[4]), s=0.5)
ax.scatter(sigmas6_5, [t[5]]*len(sigmas6_5), color = cmap(cmapt[5]), s=0.5)
ax.scatter(sigmas7_5, [t[6]]*len(sigmas7_5), color = cmap(cmapt[6]), s=0.5)
ax.scatter(sigmas8_5, [t[7]]*len(sigmas8_5), color = cmap(cmapt[7]), s=0.5)

ax.set(title= 'Subband Median Uncertainty (256s) snr>5', xlabel=r'$\mathrm{256s\/ scaled\/ median\/ uncertainty}\/ (\mu s)$', ylabel='Centre Frequency (MHz)', xscale = 'log')
cbar = plt.colorbar(sm,ticks=np.linspace(800,1700,10))
cbar.set_label('Frequency')
fig.tight_layout()

#t = [892.671000,1015.465000,1115.816000,1238.280000,1346.873000,1444.453000,1522.836000,1663.671000]
cmap = plt.get_cmap('viridis')
norm = mpl.colors.Normalize(vmin=800,vmax=1700)
sm=plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cmapt = (np.array(t)-800)/900

fig, ax = plt.subplots() 
ax.scatter(sigmas1_10, [t[0]]*len(sigmas1_10), color = cmap(cmapt[0]), s=0.5)
ax.scatter(sigmas2_10, [t[1]]*len(sigmas2_10), color = cmap(cmapt[1]), s=0.5)
ax.scatter(sigmas3_10, [t[2]]*len(sigmas3_10), color = cmap(cmapt[2]), s=0.5)
ax.scatter(sigmas4_10, [t[3]]*len(sigmas4_10), color = cmap(cmapt[3]), s=0.5)
ax.scatter(sigmas5_10, [t[4]]*len(sigmas5_10), color = cmap(cmapt[4]), s=0.5)
ax.scatter(sigmas6_10, [t[5]]*len(sigmas6_10), color = cmap(cmapt[5]), s=0.5)
ax.scatter(sigmas7_10, [t[6]]*len(sigmas7_10), color = cmap(cmapt[6]), s=0.5)
ax.scatter(sigmas8_10, [t[7]]*len(sigmas8_10), color = cmap(cmapt[7]), s=0.5)

ax.set(title= 'Subband Median Uncertainty (256s) snr>10', xlabel=r'$\mathrm{256s\/ scaled\/ median\/ uncertainty}\/ (\mu s)$', ylabel='Centre Frequency (MHz)', xscale = 'log')
cbar = plt.colorbar(sm,ticks=np.linspace(800,1700,10))
cbar.set_label('Frequency')
fig.tight_layout()
plt.show()


subband1_diff = (template_data['subband1_256']-portrait_data['subband1_256'])*100/template_data['subband1_256']
subband2_diff = (template_data['subband2_256']-portrait_data['subband2_256'])*100/template_data['subband2_256']
subband3_diff = (template_data['subband3_256']-portrait_data['subband3_256'])*100/template_data['subband3_256']
subband4_diff = (template_data['subband4_256']-portrait_data['subband4_256'])*100/template_data['subband4_256']
subband5_diff = (template_data['subband5_256']-portrait_data['subband5_256'])*100/template_data['subband5_256']
subband6_diff = (template_data['subband6_256']-portrait_data['subband6_256'])*100/template_data['subband6_256']
subband7_diff = (template_data['subband7_256']-portrait_data['subband7_256'])*100/template_data['subband7_256']
subband8_diff = (template_data['subband8_256']-portrait_data['subband8_256'])*100/template_data['subband8_256']

subband1_diff_5 = (template_data['subband1_256_5']-portrait_data['subband1_256_5'])*100/template_data['subband1_256_5']
subband2_diff_5 = (template_data['subband2_256_5']-portrait_data['subband2_256_5'])*100/template_data['subband1_256_5']
subband3_diff_5 = (template_data['subband3_256_5']-portrait_data['subband3_256_5'])*100/template_data['subband1_256_5']
subband4_diff_5 = (template_data['subband4_256_5']-portrait_data['subband4_256_5'])*100/template_data['subband1_256_5']
subband5_diff_5 = (template_data['subband5_256_5']-portrait_data['subband5_256_5'])*100/template_data['subband1_256_5']
subband6_diff_5 = (template_data['subband6_256_5']-portrait_data['subband6_256_5'])*100/template_data['subband1_256_5']
subband7_diff_5 = (template_data['subband7_256_5']-portrait_data['subband7_256_5'])*100/template_data['subband1_256_5']
subband8_diff_5 = (template_data['subband8_256_5']-portrait_data['subband8_256_5'])*100/template_data['subband1_256_5']

subband1_diff_10 = (template_data['subband1_256_10']-portrait_data['subband1_256_10'])*100/template_data['subband1_256_10']
subband2_diff_10 = (template_data['subband2_256_10']-portrait_data['subband2_256_10'])*100/template_data['subband1_256_10']
subband3_diff_10 = (template_data['subband3_256_10']-portrait_data['subband3_256_10'])*100/template_data['subband1_256_10']
subband4_diff_10 = (template_data['subband4_256_10']-portrait_data['subband4_256_10'])*100/template_data['subband1_256_10']
subband5_diff_10 = (template_data['subband5_256_10']-portrait_data['subband5_256_10'])*100/template_data['subband1_256_10']
subband6_diff_10 = (template_data['subband6_256_10']-portrait_data['subband6_256_10'])*100/template_data['subband1_256_10']
subband7_diff_10 = (template_data['subband7_256_10']-portrait_data['subband7_256_10'])*100/template_data['subband1_256_10']
subband8_diff_10 = (template_data['subband8_256_10']-portrait_data['subband8_256_10'])*100/template_data['subband1_256_10']


#Template / portrait subband difference plots

t = [950.508000,1054.402000,1150.282000,1274.552000,1376.517000,1477.161000,1615.783000,1658.082000]
t2 = [x-20 for x in t]
fig, ax = plt.subplots() 
ax.scatter(template_data['subband1_256'], [t[0]]*len(template_data['subband1_256']), color = 'tab:blue',label = 'Template', s=0.4)
ax.scatter(template_data['subband2_256'], [t[1]]*len(template_data['subband2_256']), color = 'tab:blue', s=0.4)
ax.scatter(template_data['subband3_256'], [t[2]]*len(template_data['subband3_256']), color = 'tab:blue', s=0.4)
ax.scatter(template_data['subband4_256'], [t[3]]*len(template_data['subband4_256']), color = 'tab:blue', s=0.4)
ax.scatter(template_data['subband5_256'], [t[4]]*len(template_data['subband5_256']), color = 'tab:blue', s=0.4)
ax.scatter(template_data['subband6_256'], [t[5]]*len(template_data['subband6_256']), color = 'tab:blue', s=0.4)
ax.scatter(template_data['subband7_256'], [t[6]]*len(template_data['subband7_256']), color = 'tab:blue', s=0.4)
ax.scatter(template_data['subband8_256'], [t[7]]*len(template_data['subband8_256']), color = 'tab:blue', s=0.4)

ax.scatter(portrait_data['subband1_256'], [t2[0]]*len(portrait_data['subband1_256']), color = 'tab:green', label = 'Portrait',s=0.4)
ax.scatter(portrait_data['subband2_256'], [t2[1]]*len(portrait_data['subband2_256']), color = 'tab:green',s=0.4)
ax.scatter(portrait_data['subband3_256'], [t2[2]]*len(portrait_data['subband3_256']), color = 'tab:green',s=0.4)
ax.scatter(portrait_data['subband4_256'], [t2[3]]*len(portrait_data['subband4_256']), color = 'tab:green',s=0.4)
ax.scatter(portrait_data['subband5_256'], [t2[4]]*len(portrait_data['subband5_256']), color = 'tab:green',s=0.4)
ax.scatter(portrait_data['subband6_256'], [t2[5]]*len(portrait_data['subband6_256']), color = 'tab:green',s=0.4)
ax.scatter(portrait_data['subband7_256'], [t2[6]]*len(portrait_data['subband7_256']), color = 'tab:green',s=0.4)
ax.scatter(portrait_data['subband8_256'], [t2[7]]*len(portrait_data['subband8_256']), color = 'tab:green',s=0.4)

#ax.set(title= 'Subband Median Uncertainty (256s)', xlabel=r'$\mathrm{256s\/ scaled\/ median\/ uncertainty}\/ (\mu s)$', ylabel='Centre Frequency (MHz)', xscale = 'log')
ax.set_title('Subband Median Uncertainty (256s)',fontsize=5)
ax.set_xlabel(r'$\mathrm{256s\/ scaled\/ median\/ uncertainty}\/ (\mu s)$', fontsize=5)
ax.set_ylabel('Centre Frequency (MHz)',fontsize=5)
ax.tick_params(axis='both',labelsize=5)
ax.set_xscale('log')
fig.legend(fontsize=5)
fig.tight_layout()

fig, ax = plt.subplots() 
ax.scatter(template_data['subband1_256_5'], [t[0]]*len(template_data['subband1_256_5']), color = 'tab:blue',label = 'Template', s=0.4)
ax.scatter(template_data['subband2_256_5'], [t[1]]*len(template_data['subband2_256_5']), color = 'tab:blue', s=0.4)
ax.scatter(template_data['subband3_256_5'], [t[2]]*len(template_data['subband3_256_5']), color = 'tab:blue', s=0.4)
ax.scatter(template_data['subband4_256_5'], [t[3]]*len(template_data['subband4_256_5']), color = 'tab:blue', s=0.4)
ax.scatter(template_data['subband5_256_5'], [t[4]]*len(template_data['subband5_256_5']), color = 'tab:blue', s=0.4)
ax.scatter(template_data['subband6_256_5'], [t[5]]*len(template_data['subband6_256_5']), color = 'tab:blue', s=0.4)
ax.scatter(template_data['subband7_256_5'], [t[6]]*len(template_data['subband7_256_5']), color = 'tab:blue', s=0.4)
ax.scatter(template_data['subband8_256_5'], [t[7]]*len(template_data['subband8_256_5']), color = 'tab:blue', s=0.4)

ax.scatter(portrait_data['subband1_256_5'], [t2[0]]*len(portrait_data['subband1_256_5']), color = 'tab:green', label = 'Portrait',s=0.4)
ax.scatter(portrait_data['subband2_256_5'], [t2[1]]*len(portrait_data['subband2_256_5']), color = 'tab:green',s=0.4)
ax.scatter(portrait_data['subband3_256_5'], [t2[2]]*len(portrait_data['subband3_256_5']), color = 'tab:green',s=0.4)
ax.scatter(portrait_data['subband4_256_5'], [t2[3]]*len(portrait_data['subband4_256_5']), color = 'tab:green',s=0.4)
ax.scatter(portrait_data['subband5_256_5'], [t2[4]]*len(portrait_data['subband5_256_5']), color = 'tab:green',s=0.4)
ax.scatter(portrait_data['subband6_256_5'], [t2[5]]*len(portrait_data['subband6_256_5']), color = 'tab:green',s=0.4)
ax.scatter(portrait_data['subband7_256_5'], [t2[6]]*len(portrait_data['subband7_256_5']), color = 'tab:green',s=0.4)
ax.scatter(portrait_data['subband8_256_5'], [t2[7]]*len(portrait_data['subband8_256_5']), color = 'tab:green',s=0.4)

#ax.set(title= 'Subband Median Uncertainty (256s)', xlabel=r'$\mathrm{256s\/ scaled\/ median\/ uncertainty}\/ (\mu s)$', ylabel='Centre Frequency (MHz)', xscale = 'log')
ax.set_title('Subband Median Uncertainty (256s) snr>5',fontsize=5)
ax.set_xlabel(r'$\mathrm{256s\/ scaled\/ median\/ uncertainty}\/ (\mu s)$', fontsize=5)
ax.set_ylabel('Centre Frequency (MHz)',fontsize=5)
ax.tick_params(axis='both',labelsize=5)
ax.set_xscale('log')
fig.legend(fontsize=5)
fig.tight_layout()

fig, ax = plt.subplots() 
ax.scatter(template_data['subband1_256_10'], [t[0]]*len(template_data['subband1_256_10']), color = 'tab:blue',label = 'Template', s=0.4)
ax.scatter(template_data['subband2_256_10'], [t[1]]*len(template_data['subband2_256_10']), color = 'tab:blue', s=0.4)
ax.scatter(template_data['subband3_256_10'], [t[2]]*len(template_data['subband3_256_10']), color = 'tab:blue', s=0.4)
ax.scatter(template_data['subband4_256_10'], [t[3]]*len(template_data['subband4_256_10']), color = 'tab:blue', s=0.4)
ax.scatter(template_data['subband5_256_10'], [t[4]]*len(template_data['subband5_256_10']), color = 'tab:blue', s=0.4)
ax.scatter(template_data['subband6_256_10'], [t[5]]*len(template_data['subband6_256_10']), color = 'tab:blue', s=0.4)
ax.scatter(template_data['subband7_256_10'], [t[6]]*len(template_data['subband7_256_10']), color = 'tab:blue', s=0.4)
ax.scatter(template_data['subband8_256_10'], [t[7]]*len(template_data['subband8_256_10']), color = 'tab:blue', s=0.4)

ax.scatter(portrait_data['subband1_256_10'], [t2[0]]*len(portrait_data['subband1_256_10']), color = 'tab:green', label = 'Portrait',s=0.4)
ax.scatter(portrait_data['subband2_256_10'], [t2[1]]*len(portrait_data['subband2_256_10']), color = 'tab:green',s=0.4)
ax.scatter(portrait_data['subband3_256_10'], [t2[2]]*len(portrait_data['subband3_256_10']), color = 'tab:green',s=0.4)
ax.scatter(portrait_data['subband4_256_10'], [t2[3]]*len(portrait_data['subband4_256_10']), color = 'tab:green',s=0.4)
ax.scatter(portrait_data['subband5_256_10'], [t2[4]]*len(portrait_data['subband5_256_10']), color = 'tab:green',s=0.4)
ax.scatter(portrait_data['subband6_256_10'], [t2[5]]*len(portrait_data['subband6_256_10']), color = 'tab:green',s=0.4)
ax.scatter(portrait_data['subband7_256_10'], [t2[6]]*len(portrait_data['subband7_256_10']), color = 'tab:green',s=0.4)
ax.scatter(portrait_data['subband8_256_10'], [t2[7]]*len(portrait_data['subband8_256_10']), color = 'tab:green',s=0.4)

#ax.set(title= 'Subband Median Uncertainty (256s)', xlabel=r'$\mathrm{256s\/ scaled\/ median\/ uncertainty}\/ (\mu s)$', ylabel='Centre Frequency (MHz)', xscale = 'log')
ax.set_title('Subband Median Uncertainty (256s) snr>10',fontsize=5)
ax.set_xlabel(r'$\mathrm{256s\/ scaled\/ median\/ uncertainty}\/ (\mu s)$', fontsize=5)
ax.set_ylabel('Centre Frequency (MHz)',fontsize=5)
ax.tick_params(axis='both',labelsize=5)
ax.set_xscale('log')
fig.legend(fontsize=5)
fig.tight_layout()

fig.show()


fig, axs = plt.subplots(2,2) 
(ax1, ax2), (ax3, ax4) =axs

ax1.set_ylim(bottom=-100,top=100)
ax2.set_ylim(bottom=-100,top=100)
ax3.set_ylim(bottom=-100,top=100)
ax4.set_ylim(bottom=-100,top=100)

ax1.tick_params(axis='both',labelsize=10)
ax2.tick_params(axis='both',labelsize=10)
ax3.tick_params(axis='both',labelsize=10)
ax4.tick_params(axis='both',labelsize=10)


ax1.scatter(template_data['subband1_256_10'], subband1_diff_10, color = 'tab:blue', s=1)
ax1.set_title('Subband 1 snr > 10 portrait % change',fontsize=10)
ax1.set_xlabel(r'$\mathrm{Template\/ 256s\/ scaled\/ median\/ uncertainty}\/ (\mu s)$',fontsize=10)
ax1.set_ylabel('Percentage Change: (Template-Portrait)/Template',fontsize=10)

ax2.scatter(template_data['subband2_256_10'], subband2_diff_10, color = 'tab:blue', s=1)
ax2.set_title('Subband 2 snr > 10 portrait % change',fontsize=10)
ax2.set_xlabel(r'$\mathrm{Template\/ 256s\/ scaled\/ median\/ uncertainty}\/ (\mu s)$',fontsize=10)
ax2.set_ylabel('Percentage Change: (Template-Portrait)/Template',fontsize=10)

ax3.scatter(template_data['subband3_256_10'], subband3_diff_10, color = 'tab:blue', s=1)
ax3.set_title('Subband 3 snr > 10 portrait % change',fontsize=10)
ax3.set_xlabel(r'$\mathrm{Template\/ 256s\/ scaled\/ median\/ uncertainty}\/ (\mu s)$',fontsize=10)
ax3.set_ylabel('Percentage Change: (Template-Portrait)/Template',fontsize=10)

ax4.scatter(template_data['subband4_256_10'], subband4_diff_10, color = 'tab:blue', s=1)
ax4.set_title('Subband 4 snr > 10 portrait % change',fontsize=10)
ax4.set_xlabel(r'$\mathrm{Template\/ 256s\/ scaled\/ median\/ uncertainty}\/ (\mu s)$',fontsize=10)
ax4.set_ylabel('Percentage Change: (Template-Portrait)/Template',fontsize=10)

fig.tight_layout()
fig.show()

fig, axs = plt.subplots(2,2) 
(ax5, ax6), (ax7, ax8) =axs

ax5.set_ylim(bottom=-100,top=100)
ax6.set_ylim(bottom=-100,top=100)
ax7.set_ylim(bottom=-100,top=100)
ax8.set_ylim(bottom=-100,top=100)

ax5.tick_params(axis='both',labelsize=10)
ax6.tick_params(axis='both',labelsize=10)
ax7.tick_params(axis='both',labelsize=10)
ax8.tick_params(axis='both',labelsize=10)

ax5.scatter(template_data['subband5_256_10'], subband5_diff_10, color = 'tab:blue', s=1)
ax5.set_title('Subband 5 snr > 10 portrait % change',fontsize=10)
ax5.set_xlabel(r'$\mathrm{Template\/ 256s\/ scaled\/ median\/ uncertainty}\/ (\mu s)$',fontsize=10)
ax5.set_ylabel('Percentage Change: (Template-Portrait)/Template',fontsize=10)

ax6.scatter(template_data['subband6_256_10'], subband6_diff_10, color = 'tab:blue', s=1)
ax6.set_title('Subband 6 snr > 10 portrait % change',fontsize=10)
ax6.set_xlabel(r'$\mathrm{Template\/ 256s\/ scaled\/ median\/ uncertainty}\/ (\mu s)$',fontsize=10)
ax6.set_ylabel('Percentage Change: (Template-Portrait)/Template',fontsize=10)

ax7.scatter(template_data['subband7_256_10'], subband7_diff_10, color = 'tab:blue', s=1)
ax7.set_title('Subband 7 snr > 10 portrait % change',fontsize=10)
ax7.set_xlabel(r'$\mathrm{Template\/ 256s\/ scaled\/ median\/ uncertainty}\/ (\mu s)$',fontsize=10)
ax7.set_ylabel('Percentage Change: (Template-Portrait)/Template',fontsize=10)

ax8.scatter(template_data['subband8_256_10'], subband8_diff_10, color = 'tab:blue', s=1)
ax8.set_title('Subband 8 snr > 10 portrait % change',fontsize=10)
ax8.set_xlabel(r'$\mathrm{Template\/ 256s\/ scaled\/ median\/ uncertainty}\/ (\mu s)$',fontsize=10)
ax8.set_ylabel('Percentage Change: (Template-Portrait)/Template',fontsize=10)

fig.tight_layout()

fig.show()
