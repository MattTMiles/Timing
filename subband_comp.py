#This script creates subband-timing comparison plots

import numpy as np
import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import subprocess as sproc 

activedir = "/fred/oz002/users/mmiles/templates/2D_Templates"
os.chdir(activedir)
dir_1d = "/fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/1Dtims"
dir_2d = "/fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/2DFscrunched_tims"

dir_1df = "/fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/1Dtims_F"
dir_2df = "/fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/2DFscrunched_tims_F"

pp_toas = "/fred/oz002/users/mmiles/templates/2D_Templates/pp_timing/pp_2dtoas/"
pp_toas_noDM = "/fred/oz002/users/mmiles/templates/2D_Templates/pp_timing/pp_2dtoas_noDMfit/"

pat_portrait = "/fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/2Dportrait_tims/"
pat_portrait_F = "/fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/2Dportrait_tims_F/"

dir_1d_64 = "/fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/1Dtims_64"
dir_1d_256 = "/fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/1Dtims_256"

portrait_64 = "/fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/2Dportrait_tims_64"
portrait_256 = "/fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/2Dportrait_tims_new"

badportrait_timing = '/fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/bad_portraits'

subband_timing = []

d1=[]
d2=[]
d3=[]
d4=[]
d5=[]
d6=[]
d7=[]
d8=[]

d1_2=[]
d2_2=[]
d3_2=[]
d4_2=[]
d5_2=[]
d6_2=[]
d7_2=[]
d8_2=[]

d1_64=[]
d2_64=[]
d3_64=[]
d4_64=[]
d5_64=[]
d6_64=[]
d7_64=[]
d8_64=[]

d1_2_64=[]
d2_2_64=[]
d3_2_64=[]
d4_2_64=[]
d5_2_64=[]
d6_2_64=[]
d7_2_64=[]
d8_2_64=[]

d1_256=[]
d2_256=[]
d3_256=[]
d4_256=[]
d5_256=[]
d6_256=[]
d7_256=[]
d8_256=[]

d1_2_256=[]
d2_2_256=[]
d3_2_256=[]
d4_2_256=[]
d5_2_256=[]
d6_2_256=[]
d7_2_256=[]
d8_2_256=[]

meds1 = []
meds2 = []
meds3 = []
meds4 = []
meds5 = []
meds6 = []
meds7 = []
meds8 = []

medp1 = []
medp2 = []
medp3 = []
medp4 = []
medp5 = []
medp6 = []
medp7 = []
medp8 = []

badp1 = []
badp2 = []
badp3 = []
badp4 = []
badp5 = []
badp6 = []
badp7 = []
badp8 = []

c1 = []
c2 = []
c3 = []
c4 = []
c5 = []
c6 = []
c7 = []
c8 = []

ctotal1 = []
ctotal2 = []
ctotal3 = []
ctotal4 = []
ctotal5 = []
ctotal6 = []
ctotal7 = []
ctotal8 = []

DM2 = []
toadf = []

DM_bin = []
#Collect the DM's
#for pulsar in sorted(os.listdir(dir_1d)):
for pulsar in sorted(["J1713+0747"]):
    os.chdir('/fred/oz002/users/mmiles/templates/msp_ephemerides')
    pulsar = os.path.splitext(pulsar)[0]
    with open(pulsar+".par") as f: 
        for line in f: 
            if line.startswith('DM '): 
                 line = line.strip('\n')
                 line = line.replace('\t',' ')
                 DM=line.split(' ') 
                 DM = list(filter(None,DM))
                 #DM = list(filter('\t',DM))
                 #print(DM)
                 DM = DM[1:2]
                 DM_bin.append([pulsar.strip('.par'),DM])

labels = ['Pulsar','DM']
df = pd.DataFrame(DM_bin,columns=labels)
df['DM'] = df['DM'].str[0]

for timfile in sorted(os.listdir(dir_1d)):
    if timfile.startswith("J1713+0747"):
        pulsar = os.path.splitext(timfile)[0]
        print(pulsar)
        
        #load and prepare the data
        file_1d = os.path.join(dir_1d,pulsar+".tim1D")
        file_2d = os.path.join(dir_2d,pulsar+".tim2D")

        file_1df = os.path.join(dir_1df,pulsar+"_F.tim1D")
        file_2df = os.path.join(dir_2df,pulsar+"_F.tim2D")

        file_pptoa = os.path.join(pp_toas,"2D."+pulsar+".tim")
        file_pptoa_nodm = os.path.join(pp_toas_noDM,"2D_noDM."+pulsar+".tim")

        file_pat_portrait = os.path.join(pat_portrait,pulsar+".portrait_tim")
        file_pat_portrait_F = os.path.join(pat_portrait_F,pulsar+".portrait_tim_F")

        file_641d = os.path.join(dir_1d_64,pulsar+".tim1D_64")
        file_64portrait = os.path.join(portrait_64,pulsar+".portrait_tim_64")

        file_2561d = os.path.join(dir_1d_256,pulsar+".tim1D_256")
        file_256portrait = os.path.join(portrait_256,pulsar+".newportrait_tim")

        file_badportrait = os.path.join(badportrait_timing, pulsar+'.bad_portrait_tim')

        active1D = []
        timdata_2d = []
        active1Df = []
        timdata_2df = []
        timdata_pp = []
        timdata_ppnodm = []
        active2D = []
        active2Df = []
        timdata64_1d = []
        timdata64_portrait = []
        timdata256_1d = []
        timdata256_portrait = []
        badtimdata = []

        try:
            active1D = np.loadtxt(file_1d, usecols=3, skiprows=1)
            pass
        except:
            continue
        try:
            timdata_2d = np.loadtxt(file_2d, usecols=3, skiprows=1)
        except:
            pass
        try:
            active1Df = np.loadtxt(file_1df, usecols=3, skiprows=1)
        except:
            pass
        try:
            timdata_2df = np.loadtxt(file_2df, usecols=3, skiprows=1)
        except:
            pass
        try:
            timdata_pp = np.loadtxt(file_pptoa, usecols=3)
        except:
            pass
        try:
            timdata_ppnodm = np.loadtxt(file_pptoa_nodm, usecols=3)
        except:
            pass
        try:
            active2D = np.loadtxt(file_pat_portrait, usecols=3, skiprows=1)
            pass
        except:
            continue
        try:
            active2Df = np.loadtxt(file_pat_portrait_F, usecols=3, skiprows=1)
        except:
            pass
        try:
            timdata64_1d = np.loadtxt(file_641d, usecols=3, skiprows=1)
        except:
            pass
        try:
            timdata64_portrait = np.loadtxt(file_64portrait, usecols=3, skiprows=1)
        except:
            pass
        try:
            timdata256_1d = np.loadtxt(file_2561d, usecols=3, skiprows=1)
        except:
            pass
        try:
            timdata256_portrait = np.loadtxt(file_256portrait, usecols=3, skiprows=1)
        except:
            pass
        try:
            badtimdata = np.loadtxt(file_badportrait, usecols=3, skiprows=1)
        except:
            pass

        #These change depending on what we want to plot the subband data of
        active1D = timdata256_1d
        active2D = timdata256_portrait

        #separate the 8s data into the subbands
        stdsubband_1 = active1D[::8]
        stdsubband_2 = active1D[1::8]
        stdsubband_3 = active1D[2::8]
        stdsubband_4 = active1D[3::8]
        stdsubband_5 = active1D[4::8]
        stdsubband_6 = active1D[5::8]
        stdsubband_7 = active1D[6::8]
        stdsubband_8 = active1D[7::8]

        portsubband_1 = active2D[::8]
        portsubband_2 = active2D[1::8]
        portsubband_3 = active2D[2::8]
        portsubband_4 = active2D[3::8]
        portsubband_5 = active2D[4::8]
        portsubband_6 = active2D[5::8]
        portsubband_7 = active2D[6::8]
        portsubband_8 = active2D[7::8]

        #Collect the medians of the subband timing
        med_std1, med_std2, med_std3, med_std4, med_std5, med_std6, med_std7, med_std8 = \
            np.median(stdsubband_1), np.median(stdsubband_2), np.median(stdsubband_3), np.median(stdsubband_4), \
                np.median(stdsubband_5), np.median(stdsubband_6), np.median(stdsubband_7), np.median(stdsubband_8)

        med_port1, med_port2, med_port3, med_port4, med_port5, med_port6, med_port7, med_port8 = \
            np.median(portsubband_1), np.median(portsubband_2), np.median(portsubband_3), np.median(portsubband_4), \
                 np.median(portsubband_5), np.median(portsubband_6), np.median(portsubband_7), np.median(portsubband_8)

        #Collect the percentage change from using the 2D templates
        change1, change2, change3, change4, change5, change6, change7, change8 = \
            ((med_std1-med_port1)/med_std1)*100, ((med_std2-med_port2)/med_std2)*100, ((med_std3-med_port3)/med_std3)*100, ((med_std4-med_port4)/med_std4)*100, \
                ((med_std5-med_port5)/med_std5)*100, ((med_std6-med_port6)/med_std6)*100, ((med_std7-med_port7)/med_std7)*100, ((med_std8-med_port8)/med_std8)*100


        changetotal1, changetotal2, changetotal3, changetotal4, changetotal5, changetotal6, changetotal7, changetotal8 = \
            ((stdsubband_1-portsubband_1)/stdsubband_1)*100,((stdsubband_2-portsubband_2)/stdsubband_2)*100,((stdsubband_3-portsubband_3)/stdsubband_3)*100,((stdsubband_4-portsubband_4)/stdsubband_4)*100, \
                ((stdsubband_5-portsubband_5)/stdsubband_5)*100,((stdsubband_6-portsubband_6)/stdsubband_6)*100,((stdsubband_7-portsubband_7)/stdsubband_7)*100,((stdsubband_8-portsubband_8)/stdsubband_8)*100


        #Put it all together into the required arrays
        meds1.append(med_std1)
        meds2.append(med_std2)
        meds3.append(med_std3)
        meds4.append(med_std4)
        meds5.append(med_std5)
        meds6.append(med_std6)
        meds7.append(med_std7)
        meds8.append(med_std8)

        medp1.append(med_port1)
        medp2.append(med_port2)
        medp3.append(med_port3)
        medp4.append(med_port4)
        medp5.append(med_port5)
        medp6.append(med_port6)
        medp7.append(med_port7)
        medp8.append(med_port8)

        c1.append(change1)
        c2.append(change2)
        c3.append(change3)
        c4.append(change4)
        c5.append(change5)
        c6.append(change6)
        c7.append(change7)
        c8.append(change8)

        ctotal1.append(changetotal1)
        ctotal2.append(changetotal2)
        ctotal3.append(changetotal3)
        ctotal4.append(changetotal4)
        ctotal5.append(changetotal5)
        ctotal6.append(changetotal6)
        ctotal7.append(changetotal7)
        ctotal8.append(changetotal8)
        
        #dm fitter
        try:
            dm = df['DM'][df['Pulsar']==pulsar].values[0]
        except IndexError:
            print(pulsar+' stuffed up')
            dm = 0

        DM2.append(float(dm))


        #64s data, same process as above
        stdsubband_1_64 = timdata64_1d[::8]
        stdsubband_2_64 = timdata64_1d[1::8]
        stdsubband_3_64 = timdata64_1d[2::8]
        stdsubband_4_64 = timdata64_1d[3::8]
        stdsubband_5_64 = timdata64_1d[4::8]
        stdsubband_6_64 = timdata64_1d[5::8]
        stdsubband_7_64 = timdata64_1d[6::8]
        stdsubband_8_64 = timdata64_1d[7::8]

        portsubband_1_64 = timdata64_portrait[::8]
        portsubband_2_64 = timdata64_portrait[1::8]
        portsubband_3_64 = timdata64_portrait[2::8]
        portsubband_4_64 = timdata64_portrait[3::8]
        portsubband_5_64 = timdata64_portrait[4::8]
        portsubband_6_64 = timdata64_portrait[5::8]
        portsubband_7_64 = timdata64_portrait[6::8]
        portsubband_8_64 = timdata64_portrait[7::8]

        stdsubband_1_256 = timdata256_1d[::8]
        stdsubband_2_256 = timdata256_1d[1::8]
        stdsubband_3_256 = timdata256_1d[2::8]
        stdsubband_4_256 = timdata256_1d[3::8]
        stdsubband_5_256 = timdata256_1d[4::8]
        stdsubband_6_256 = timdata256_1d[5::8]
        stdsubband_7_256 = timdata256_1d[6::8]
        stdsubband_8_256 = timdata256_1d[7::8]

        portsubband_1_256 = timdata256_portrait[::8]
        portsubband_2_256 = timdata256_portrait[1::8]
        portsubband_3_256 = timdata256_portrait[2::8]
        portsubband_4_256 = timdata256_portrait[3::8]
        portsubband_5_256 = timdata256_portrait[4::8]
        portsubband_6_256 = timdata256_portrait[5::8]
        portsubband_7_256 = timdata256_portrait[6::8]
        portsubband_8_256 = timdata256_portrait[7::8]

        #Organise the data
        #8s subint data
        d1.extend(stdsubband_1)
        d2.extend(stdsubband_2)
        d3.extend(stdsubband_3)
        d4.extend(stdsubband_4)
        d5.extend(stdsubband_5)
        d6.extend(stdsubband_6)
        d7.extend(stdsubband_7)
        d8.extend(stdsubband_8)

        d1_2.extend(portsubband_1)
        d2_2.extend(portsubband_2)
        d3_2.extend(portsubband_3)
        d4_2.extend(portsubband_4)
        d5_2.extend(portsubband_5)
        d6_2.extend(portsubband_6)
        d7_2.extend(portsubband_7)
        d8_2.extend(portsubband_8)
        
        #64second subintegration data
        d1_64.extend(stdsubband_1_64)
        d2_64.extend(stdsubband_2_64)
        d3_64.extend(stdsubband_3_64)
        d4_64.extend(stdsubband_4_64)
        d5_64.extend(stdsubband_5_64)
        d6_64.extend(stdsubband_6_64)
        d7_64.extend(stdsubband_7_64)
        d8_64.extend(stdsubband_8_64)

        d1_2_64.extend(portsubband_1_64)
        d2_2_64.extend(portsubband_2_64)
        d3_2_64.extend(portsubband_3_64)
        d4_2_64.extend(portsubband_4_64)
        d5_2_64.extend(portsubband_5_64)
        d6_2_64.extend(portsubband_6_64)
        d7_2_64.extend(portsubband_7_64)
        d8_2_64.extend(portsubband_8_64)

        d1_256.extend(stdsubband_1_256)
        d2_256.extend(stdsubband_2_256)
        d3_256.extend(stdsubband_3_256)
        d4_256.extend(stdsubband_4_256)
        d5_256.extend(stdsubband_5_256)
        d6_256.extend(stdsubband_6_256)
        d7_256.extend(stdsubband_7_256)
        d8_256.extend(stdsubband_8_256)

        d1_2_256.extend(portsubband_1_256)
        d2_2_256.extend(portsubband_2_256)
        d3_2_256.extend(portsubband_3_256)
        d4_2_256.extend(portsubband_4_256)
        d5_2_256.extend(portsubband_5_256)
        d6_2_256.extend(portsubband_6_256)
        d7_2_256.extend(portsubband_7_256)
        d8_2_256.extend(portsubband_8_256)

        #Create a df to debug the huge TOAs
        #Needs to have [pulsar, <1d subbands>, <2d subbands>]
        toadf.append([pulsar, med_std1, med_std2, med_std3, med_std4, med_std5, med_std6, med_std7, med_std8,\
             med_port1, med_port2, med_port3, med_port4, med_port5, med_port6, med_port7, med_port8, \
                 change1, change2, change3, change4, change5, change6, change7, change8])

toa_labels = ['Pulsar','1D1','1D2','1D3','1D4','1D5','1D6','1D7','1D8',\
    '2D1','2D2','2D3','2D4','2D5','2D6','2D7','2D8','c1','c2','c3','c4','c5','c6','c7','c8']

df_toa = pd.DataFrame(toadf, columns = toa_labels)
df_toa.round(4)
df_toa.round(4).to_csv(r'/fred/oz002/users/mmiles/templates/2D_Templates/toadf.txt', header=toa_labels, sep=' ', mode='a')
DM_array = DM2

d1 = np.array(d1)
d2 = np.array(d2)
d3 = np.array(d3)
d4 = np.array(d4)
d5 = np.array(d5)
d6 = np.array(d6)
d7 = np.array(d7)
d8 = np.array(d8)
d1_2 = np.array(d1_2)
d2_2 = np.array(d2_2)
d3_2 = np.array(d3_2)
d4_2 = np.array(d4_2)
d5_2 = np.array(d5_2)
d6_2 = np.array(d6_2)
d7_2 = np.array(d7_2)
d8_2 = np.array(d8_2)

d1_64 = np.array(d1_64)
d2_64 = np.array(d2_64)
d3_64 = np.array(d3_64)
d4_64 = np.array(d4_64)
d5_64 = np.array(d5_64)
d6_64 = np.array(d6_64)
d7_64 = np.array(d7_64)
d8_64 = np.array(d8_64)
d1_2_64 = np.array(d1_2_64)
d2_2_64 = np.array(d2_2_64)
d3_2_64 = np.array(d3_2_64)
d4_2_64 = np.array(d4_2_64)
d5_2_64 = np.array(d5_2_64)
d6_2_64 = np.array(d6_2_64)
d7_2_64 = np.array(d7_2_64)
d8_2_64 = np.array(d8_2_64)

d1_256 = np.array(d1_256)
d2_256 = np.array(d2_256)
d3_256 = np.array(d3_256)
d4_256 = np.array(d4_256)
d5_256 = np.array(d5_256)
d6_256 = np.array(d6_256)
d7_256 = np.array(d7_256)
d8_256 = np.array(d8_256)
d1_2_256 = np.array(d1_2_256)
d2_2_256 = np.array(d2_2_256)
d3_2_256 = np.array(d3_2_256)
d4_2_256 = np.array(d4_2_256)
d5_2_256 = np.array(d5_2_256)
d6_2_256 = np.array(d6_2_256)
d7_2_256 = np.array(d7_2_256)
d8_2_256 = np.array(d8_2_256)

meds1 = np.array(meds1)
meds2 = np.array(meds2)
meds3 = np.array(meds3)
meds4 = np.array(meds4)
meds5 = np.array(meds5)
meds6 = np.array(meds6)
meds7 = np.array(meds7)
meds8 = np.array(meds8)

medp1 = np.array(medp1)
medp2 = np.array(medp2)
medp3 = np.array(medp3)
medp4 = np.array(medp4)
medp5 = np.array(medp5)
medp6 = np.array(medp6)
medp7 = np.array(medp7)
medp8 = np.array(medp8)

#Where the change is exactly 100% it means that the 2D portrait hasn't timed correctly, so get rid of these for the plot
c1 = np.array(c1)
c1[c1==100] = np.nan
c2 = np.array(c2)
c2[c2==100] = np.nan
c3 = np.array(c3)
c3[c3==100] = np.nan
c4 = np.array(c4)
c4[c4==100] = np.nan
c5 = np.array(c5)
c5[c5==100] = np.nan
c6 = np.array(c6)
c6[c6==100] = np.nan
c7 = np.array(c7)
c7[c7==100] = np.nan
c8 = np.array(c8)
c8[c8==100] = np.nan

os.chdir(activedir)

t = [892.671000,1015.465000,1115.816000,1238.280000,1346.873000,1444.453000,1522.836000,1663.671000]
cmap = plt.get_cmap('viridis')
norm = mpl.colors.Normalize(vmin=800,vmax=1700)
sm=plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cmapt = (np.array(t)-800)/900

fig, ax = plt.subplots()
plt.style.use('fivethirtyeight')

#ax.scatter(meds1,np.zeros(len(meds1)), c = cmap(cmapt[0]), s = 5)
#ax.scatter(meds2,np.zeros(len(meds2)), c = cmap(cmapt[1]), s = 5)
#ax.scatter(meds3,np.zeros(len(meds3)), c = cmap(cmapt[2]), s = 5)
#ax.scatter(meds4,np.zeros(len(meds4)), c = cmap(cmapt[3]), s = 5)
#ax.scatter(meds5,np.zeros(len(meds5)), c = cmap(cmapt[4]), s = 5)
#ax.scatter(meds6,np.zeros(len(meds6)), c = cmap(cmapt[5]), s = 5)
#ax.scatter(meds7,np.zeros(len(meds7)), c = cmap(cmapt[6]), s = 5)
#ax.scatter(meds8,np.zeros(len(meds8)), c = cmap(cmapt[7]), s = 5)

#ax.scatter(meds1,c1, c = cmap(cmapt[0]), s = 10)
#ax.scatter(meds2,c2, c = cmap(cmapt[1]), s = 10)
#ax.scatter(meds3,c3, c = cmap(cmapt[2]), s = 10)
#ax.scatter(meds4,c4, c = cmap(cmapt[3]), s = 10)
#ax.scatter(meds5,c5, c = cmap(cmapt[4]), s = 10)
#ax.scatter(meds6,c6, c = cmap(cmapt[5]), s = 10)
#ax.scatter(meds7,c7, c = cmap(cmapt[6]), s = 10)
#ax.scatter(meds8,c8, c = cmap(cmapt[7]), s = 10)

ax.scatter(d1_256,ctotal1, c = cmap(cmapt[0]), s = 10)
ax.scatter(d2_256,ctotal2, c = cmap(cmapt[1]), s = 10)
ax.scatter(d3_256,ctotal3, c = cmap(cmapt[2]), s = 10)
ax.scatter(d4_256,ctotal4, c = cmap(cmapt[3]), s = 10)
ax.scatter(d5_256,ctotal5, c = cmap(cmapt[4]), s = 10)
ax.scatter(d6_256,ctotal6, c = cmap(cmapt[5]), s = 10)
ax.scatter(d7_256,ctotal7, c = cmap(cmapt[6]), s = 10)
ax.scatter(d8_256,ctotal8, c = cmap(cmapt[7]), s = 10)

#ax.scatter(DM_array,c1, c = cmap(cmapt[0]), s = 5)
#ax.scatter(DM_array,c2, c = cmap(cmapt[1]), s = 5)
#ax.scatter(DM_array,c3, c = cmap(cmapt[2]), s = 5)
#ax.scatter(DM_array,c4, c = cmap(cmapt[3]), s = 5)
#ax.scatter(DM_array,c5, c = cmap(cmapt[4]), s = 5)
#ax.scatter(DM_array,c6, c = cmap(cmapt[5]), s = 5)
#ax.scatter(DM_array,c7, c = cmap(cmapt[6]), s = 5)
#ax.scatter(DM_array,c8, c = cmap(cmapt[7]), s = 5)
#ax.grid(color='k', linestyle='-', linewidth=0.2)
#ax.set_xlim(left=0)
ax.set_ylim(bottom=-100,top=100)
ax.set_xscale("log")
#plt.legend()
cbar = plt.colorbar(sm,ticks=np.linspace(800,1700,10))
cbar.set_label('Frequency')
ax.set(xlabel=r'$\mathrm{1D\/ sub-band\/ TOA}\/ (\mu s)$', ylabel=r'$\mathrm{\%\/ change\/ from\/ 2D}$')
#ax.set(xlabel='DM', ylabel=r'$\mathrm{\%\/ change\/ from\/ 2D}$')
plt.title('256s Subintegrations')
#plt.xticks(np.arange(min(DM_array), max(DM_array)+1, 10.0))
fig.tight_layout()
plt.show()


'''
#data_min = [d1.min(),d2.min(),d3.min(),d4.min(),d5.min(),d6.min(),d7.min(),d8.min(),d1_2.min(),d2_2.min(),d3_2.min(),d4_2.min(),d5_2.min(),d6_2.min(),d7_2.min(),d8_2.min()]
#data = np.array(data)
#subband_data = pd.DataFrame(data, columns = labels)
ratio = d1_2/d1
high = np.percentile(ratio, 95)
low = np.percentile(ratio, 15)
limit = np.logical_or(ratio > high, ratio < low)
ratio2, ratio3, ratio4, ratio5, ratio6, ratio7, ratio8 = d2_2/d2, d3_2/d3, d4_2/d4, d5_2/d5,d6_2/d6,d7_2/d7,d8_2/d8
limit2, limit3, limit4, limit5, limit6, limit7, limit8 = np.logical_or(ratio2 > high, ratio2 < low), np.logical_or(ratio3 > high, ratio3 < low), np.logical_or(ratio4 > high, ratio4 < low), np.logical_or(ratio5 > high, ratio5 < low), np.logical_or(ratio6 > high, ratio6 < low), np.logical_or(ratio7 > high, ratio7 < low), np.logical_or(ratio8 > high, ratio8 < low)

ratio_64 = d1_2_64/d1_64
high_64 = np.percentile(ratio_64, 95)
low_64 = np.percentile(ratio_64, 15)
limit_64 = np.logical_or(ratio_64 > high_64, ratio_64 < low_64)
ratio2_64, ratio3_64, ratio4_64, ratio5_64, ratio6_64, ratio7_64, ratio8_64 = d2_2_64/d2_64, d3_2_64/d3_64, d4_2_64/d4_64, d5_2_64/d5_64,d6_2_64/d6_64,d7_2_64/d7_64,d8_2_64/d8_64
limit2_64, limit3_64, limit4_64, limit5_64, limit6_64, limit7_64, limit8_64 = np.logical_or(ratio2_64 > high_64, ratio2_64 < low_64), np.logical_or(ratio3_64 > high_64, ratio3_64 < low_64), np.logical_or(ratio4_64 > high_64, ratio4_64 < low_64), np.logical_or(ratio5_64 > high_64, ratio5_64 < low_64), np.logical_or(ratio6_64 > high_64, ratio6_64 < low_64), np.logical_or(ratio7_64 > high_64, ratio7_64 < low_64), np.logical_or(ratio8_64 > high_64, ratio8_64 < low_64)


ratio_256 = d1_2_256/d1_256
high_256 = np.percentile(ratio_256, 95)
low_256 = np.percentile(ratio_256, 15)
limit_256 = np.logical_or(ratio_256 > high_256, ratio_256 < low_256)
ratio2_256, ratio3_256, ratio4_256, ratio5_256, ratio6_256, ratio7_256, ratio8_256 = d2_2_256/d2_256, d3_2_256/d3_256, d4_2_256/d4_256, d5_2_256/d5_256,d6_2_256/d6_256,d7_2_256/d7_256,d8_2_256/d8_256
limit2_256, limit3_256, limit4_256, limit5_256, limit6_256, limit7_256, limit8_256 = np.logical_or(ratio2_256 > high_256, ratio2_256 < low_256), np.logical_or(ratio3_256 > high_256, ratio3_256 < low_64), np.logical_or(ratio4_256 > high_256, ratio4_256 < low_256), np.logical_or(ratio5_256 > high_256, ratio5_256 < low_256), np.logical_or(ratio6_256 > high_256, ratio6_256 < low_256), np.logical_or(ratio7_256 > high_256, ratio7_256 < low_256), np.logical_or(ratio8_256 > high_256, ratio8_256 < low_256)

fig, axs = plt.subplots(2,2)
axs[0, 0].scatter(d1,d1_2,color='tab:blue',s=0.2,zorder=1)
#axs[0, 1].scatter(d2,d2_2,color='tab:blue',s=0.2,zorder=1)
axs[0, 1].scatter(d3,d3_2,color='tab:blue',s=0.2,zorder=1)
#axs[1, 0].scatter(d4,d4_2,color='tab:blue',s=0.2,zorder=1)
#axs[1, 1].plot()
#axs[1, 2].scatter(d5,d5_2,color='tab:blue',s=0.2,zorder=1)
axs[1, 0].scatter(d6,d6_2,color='tab:blue',s=0.2,zorder=1)
#axs[2, 1].scatter(d7,d7_2,color='tab:blue',s=0.2,zorder=1)
axs[1, 1].scatter(d8,d8_2,color='tab:blue',s=0.2,zorder=1)

#scale_left = subband_data.min()
fig.suptitle("All pulsars: 8s subints",y=0.98)

for ax in axs.flat:
    ax.set(xlabel=r'$\mathrm{1D}\/ (\mu s)$', ylabel=r'$\mathrm{portrait}\/ (\mu s)$')
    ax.label_outer()
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(left=1e-2,right=10)
    ax.set_ylim(bottom=1e-2,top=10)
    lims = [np.min([ax.get_xlim(), ax.get_ylim()]),np.max([ax.get_xlim(),ax.get_ylim()])]
    ax.plot(lims, lims, 'k-', alpha=5, zorder=2)

fig.subplots_adjust(top=5)

fig.tight_layout()

#plt.figure()
plt.show()
#plt.savefig("/fred/oz002/users/mmiles/templates/2D_Templates/plots/subband_timing/8s_allpulsars_4bands.png")

fig2, axs2 = plt.subplots(2,2)
axs2[0, 0].scatter(d1_64,d1_2_64,color='tab:blue',s=0.2,zorder=1)
#axs2[0, 1].scatter(d2_64,d2_2_64,color='tab:blue',s=0.2,zorder=1)
axs2[0, 1].scatter(d3_64,d3_2_64,color='tab:blue',s=0.2,zorder=1)
#axs2[1, 0].scatter(d4_64,d4_2_64,color='tab:blue',s=0.2,zorder=1)
#axs2[1, 1].plot()
#axs2[1, 2].scatter(d5_64,d5_2_64,color='tab:blue',s=0.2,zorder=1)
axs2[1, 0].scatter(d6_64,d6_2_64,color='tab:blue',s=0.2,zorder=1)
#axs2[2, 1].scatter(d7_64,d7_2_64,color='tab:blue',s=0.2,zorder=1)
axs2[1, 1].scatter(d8_64,d8_2_64,color='tab:blue',s=0.2,zorder=1)

#scale_left = subband_data.min()
fig2.suptitle("All pulsars: 64s subints",y=0.98)

for ax in axs2.flat:
    ax.set(xlabel=r'$\mathrm{1D}\/ (\mu s)$', ylabel=r'$\mathrm{portrait}\/ (\mu s)$')
    ax.label_outer()
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(left=1e-2,right=10)
    ax.set_ylim(bottom=1e-2,top=10)
    lims = [np.min([ax.get_xlim(), ax.get_ylim()]),np.max([ax.get_xlim(),ax.get_ylim()])]
    ax.plot(lims, lims, 'k-', alpha=5, zorder=2)

fig2.subplots_adjust(top=5)
fig2.tight_layout()
plt.savefig("/fred/oz002/users/mmiles/templates/2D_Templates/plots/subband_timing/64s_allpulsars_4bands.png")

fig3, axs3 = plt.subplots(2,2)
axs3[0, 0].scatter(d1_256,d1_2_256,color='tab:blue',s=0.2,zorder=1)
#axs3[0, 1].scatter(d2_256,d2_2_256,color='tab:blue',s=0.2,zorder=1)
axs3[0, 1].scatter(d3_256,d3_2_256,color='tab:blue',s=0.2,zorder=1)
#axs3[1, 0].scatter(d4_256,d4_2_256,color='tab:blue',s=0.2,zorder=1)
#axs3[1, 1].plot()
#axs3[1, 2].scatter(d5_256,d5_2_256,color='tab:blue',s=0.2,zorder=1)
axs3[1, 0].scatter(d6_256,d6_2_256,color='tab:blue',s=0.2,zorder=1)
#axs3[2, 1].scatter(d7_256,d7_2_256,color='tab:blue',s=0.2,zorder=1)
axs3[1, 1].scatter(d8_256,d8_2_256,color='tab:blue',s=0.2,zorder=1)


#scale_left = subband_data.min()
fig3.suptitle("All pulsars: 256s subints",y=0.98)

for ax in axs3.flat:
    ax.set(xlabel=r'$\mathrm{1D}\/ (\mu s)$', ylabel=r'$\mathrm{portrait}\/ (\mu s)$')
    ax.label_outer()
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(left=1e-2,right=10)
    ax.set_ylim(bottom=1e-2,top=10)
    lims = [np.min([ax.get_xlim(), ax.get_ylim()]),np.max([ax.get_xlim(),ax.get_ylim()])]
    ax.plot(lims, lims, 'k-', alpha=5, zorder=2)

fig3.subplots_adjust(top=5)
fig3.tight_layout()
plt.savefig("/fred/oz002/users/mmiles/templates/2D_Templates/plots/subband_timing/256s_allpulsars_4bands.png")

#Put in colourbar values (800 to 1800)
t = [892.671000,1015.465000,1115.816000,1238.280000,1346.873000,1444.453000,1522.836000,1663.671000]
cmap = plt.get_cmap('viridis')
norm = mpl.colors.Normalize(vmin=800,vmax=1700)
sm=plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cmapt = (np.array(t)-800)/900

#Lowest band cutoff method
fig, ax = plt.subplots()
ax.scatter(d1[limit],d1_2[limit], c = cmap(cmapt[0]),s=0.2, zorder=1, label='sub-band 1')
ax.scatter(d2[limit2],d2_2[limit2], c = cmap(cmapt[1]),s=0.2,zorder=1,label = 'sub-band 2')
ax.scatter(d3[limit3],d3_2[limit3], c = cmap(cmapt[2]),s=0.2,zorder=1,label = 'sub-band 3')
ax.scatter(d4[limit4],d4_2[limit4], c = cmap(cmapt[3]),s=0.2,zorder=1,label = 'sub-band 4')
ax.scatter(d5[limit5],d5_2[limit5], c = cmap(cmapt[4]),s=0.2,zorder=1,label = 'sub-band 5')
ax.scatter(d6[limit6],d6_2[limit6], c = cmap(cmapt[5]),s=0.2,zorder=1,label = 'sub-band 6')
ax.scatter(d7[limit7],d7_2[limit7], c = cmap(cmapt[6]),s=0.2,zorder=1,label = 'sub-band 7')
ax.scatter(d8[limit8],d8_2[limit8], c = cmap(cmapt[7]),s=0.2,zorder=1,label = 'sub-band 8')

plt.title('8s subintegrations')
plt.yscale('log'), plt.xscale('log')
plt.xlabel(r'$\mathrm{1D}\/ (\mu s)$')
plt.ylabel(r'$\mathrm{portrait}\/ (\mu s)$')
lims = [np.min([ax.get_xlim(), ax.get_ylim()]),np.max([ax.get_xlim(),ax.get_ylim()])]
ax.plot(lims, lims, 'k-', alpha=5, zorder=2)
ax.set_xlim(left=1e-2,right=10)
ax.set_ylim(bottom=1e-2,top=10)
#plt.legend()
cbar = plt.colorbar(sm,ticks=np.linspace(800,1700,10))
cbar.set_label('Frequency')
fig.tight_layout()
plt.savefig("/fred/oz002/users/mmiles/templates/2D_Templates/plots/8s_freq_dependent.png")
#plt.figure()



fig, ax = plt.subplots()
ax.scatter(d1_64[limit_64],d1_2_64[limit_64], c = cmap(cmapt[0]), s=0.2,zorder=1, label = 'sub-band 1')
ax.scatter(d2_64[limit2_64],d2_2_64[limit2_64], c = cmap(cmapt[1]), s=0.2,zorder=1,label = 'sub-band 2')
ax.scatter(d3_64[limit3_64],d3_2_64[limit3_64], c = cmap(cmapt[2]), s=0.2,zorder=1,label = 'sub-band 3')
ax.scatter(d4_64[limit4_64],d4_2_64[limit4_64], c = cmap(cmapt[3]), s=0.2,zorder=1,label = 'sub-band 4')
ax.scatter(d5_64[limit5_64],d5_2_64[limit5_64], c = cmap(cmapt[4]), s=0.2,zorder=1,label = 'sub-band 5')
ax.scatter(d6_64[limit6_64],d6_2_64[limit6_64], c = cmap(cmapt[5]), s=0.2,zorder=1,label = 'sub-band 6')
ax.scatter(d7_64[limit7_64],d7_2_64[limit7_64], c = cmap(cmapt[6]), s=0.2,zorder=1,label = 'sub-band 7')
ax.scatter(d8_64[limit8_64],d8_2_64[limit8_64], c = cmap(cmapt[7]), s=0.2,zorder=1,label = 'sub-band 8')

plt.title('64s subintegrations')
plt.yscale('log'), plt.xscale('log')
plt.xlabel(r'$\mathrm{1D}\/ (\mu s)$')
plt.ylabel(r'$\mathrm{portrait}\/ (\mu s)$')
lims = [np.min([ax.get_xlim(), ax.get_ylim()]),np.max([ax.get_xlim(),ax.get_ylim()])]
ax.plot(lims, lims, 'k-', alpha=5, zorder=2)
ax.set_xlim(left=1e-2,right=10)
ax.set_ylim(bottom=1e-2,top=10)
cbar = plt.colorbar(sm,ticks=np.linspace(800,1700,10))
cbar.set_label('Frequency')
#plt.legend()
fig.tight_layout()
plt.savefig("/fred/oz002/users/mmiles/templates/2D_Templates/plots/64s_freq_dependent.png")
#plt.figure()
'''
'''
fig, ax = plt.subplots()
plt.title('256s subintegrations')
t = [892.671000,1015.465000,1115.816000,1238.280000,1346.873000,1444.453000,1522.836000,1663.671000]
cmap = plt.get_cmap('viridis')
norm = mpl.colors.Normalize(vmin=800,vmax=1700)
sm=plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cmapt = (np.array(t)-800)/900

ax.scatter(d1_256, d1_2_256, c = cmap(cmapt[0]), s=2,zorder=1,label = 'sub-band 1')
ax.scatter(d2_256, d2_2_256, c = cmap(cmapt[1]), s=2,zorder=1,label = 'sub-band 2')
ax.scatter(d3_256,d3_2_256, c = cmap(cmapt[2]), s=2,zorder=1,label = 'sub-band 3')
ax.scatter(d4_256,d4_2_256, c = cmap(cmapt[3]), s=2,zorder=1,label = 'sub-band 4')
ax.scatter(d5_256,d5_2_256, c = cmap(cmapt[4]), s=2,zorder=1,label = 'sub-band 5')
ax.scatter(d6_256,d6_2_256, c = cmap(cmapt[5]), s=2,zorder=1,label = 'sub-band 6')
ax.scatter(d7_256,d7_2_256, c = cmap(cmapt[6]), s=2,zorder=1,label = 'sub-band 7')
ax.scatter(d8_256,d8_2_256, c = cmap(cmapt[7]), s=2,zorder=1,label = 'sub-band 8')

plt.yscale('log'), plt.xscale('log')
plt.xlabel(r'$\mathrm{1D}\/ (\mu s)$')
plt.ylabel(r'$\mathrm{portrait}\/ (\mu s)$')

ax.set_xlim(left=1e-2,right=10)
ax.set_ylim(bottom=1e-2,top=10)
cbar = plt.colorbar(sm,ticks=np.linspace(800,1700,10))
cbar.set_label('Frequency')
#plt.legend()
lims = [np.min([ax.get_xlim(), ax.get_ylim()]),np.max([ax.get_xlim(),ax.get_ylim()])]
ax.plot(lims, lims, 'k-', zorder=2, lw=1)
fig.tight_layout()
#plt.savefig("/fred/oz002/users/mmiles/templates/2D_Templates/plots/256s_freq_dependent.png")
plt.show()
'''

'''
ax.scatter(d1_256[limit_256],d1_2_256[limit_256], c = cmap(cmapt[0]), s=0.2,zorder=1,label = 'sub-band 1')
ax.scatter(d2_256[limit2_256],d2_2_256[limit2_256], c = cmap(cmapt[1]), s=0.2,zorder=1,label = 'sub-band 2')
ax.scatter(d3_256[limit3_256],d3_2_256[limit3_256], c = cmap(cmapt[2]), s=0.2,zorder=1,label = 'sub-band 3')
ax.scatter(d4_256[limit4_256],d4_2_256[limit4_256], c = cmap(cmapt[3]), s=0.2,zorder=1,label = 'sub-band 4')
ax.scatter(d5_256[limit5_256],d5_2_256[limit5_256], c = cmap(cmapt[4]), s=0.2,zorder=1,label = 'sub-band 5')
ax.scatter(d6_256[limit6_256],d6_2_256[limit6_256], c = cmap(cmapt[5]), s=0.2,zorder=1,label = 'sub-band 6')
ax.scatter(d7_256[limit7_256],d7_2_256[limit7_256], c = cmap(cmapt[6]), s=0.2,zorder=1,label = 'sub-band 7')
ax.scatter(d8_256[limit8_256],d8_2_256[limit8_256], c = cmap(cmapt[7]), s=0.2,zorder=1,label = 'sub-band 8')
'''
