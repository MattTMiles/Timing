#This script creates a variety of plots for the different types of timing for the MSP project

import numpy as np
import pandas as pd 
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
portrait_256 = "/fred/oz002/users/mmiles/templates/2D_Templates/pat_timing/2Dportrait_tims_256"

df_timing = []

for timfile in sorted(os.listdir(dir_1d)):
    if not timfile.startswith("J0437"):
        pulsar = os.path.splitext(timfile)[0]
        print(pulsar)
        
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
        file_256portrait = os.path.join(portrait_256,pulsar+".portrait_tim_256")

        timdata_1d = []
        timdata_2d = []
        timdata_1df = []
        timdata_2df = []
        timdata_pp = []
        timdata_ppnodm = []
        timdata_patport = []
        timdata_patportf = []
        timdata64_1d = []
        timdata64_portrait = []
        timdata256_1d = []
        timdata256_portrait = []

        try:
            timdata_1d = np.loadtxt(file_1d, usecols=3, skiprows=1)
        except:
            pass
        try:
            timdata_2d = np.loadtxt(file_2d, usecols=3, skiprows=1)
        except:
            pass
        try:
            timdata_1df = np.loadtxt(file_1df, usecols=3, skiprows=1)
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
            timdata_patport = np.loadtxt(file_pat_portrait, usecols=3, skiprows=1)
        except:
            pass
        try:
            timdata_patportf = np.loadtxt(file_pat_portrait_F, usecols=3, skiprows=1)
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
        
        xdata = timdata_1d
        ydata = timdata_2d
        
        xdataf = timdata_1df
        ydataf = timdata_2df

        data_pptoa = timdata_pp
        data_pp_nodm = timdata_ppnodm
        '''
        #Here we are creating a 3x3 grid showing the 8 subbands for each timing file for the portraits and standards
        stdsubband_1 = timdata_1d[::8]
        stdsubband_2 = timdata_1d[1::8]
        stdsubband_3 = timdata_1d[2::8]
        stdsubband_4 = timdata_1d[3::8]
        stdsubband_5 = timdata_1d[4::8]
        stdsubband_6 = timdata_1d[5::8]
        stdsubband_7 = timdata_1d[6::8]
        stdsubband_8 = timdata_1d[7::8]

        portsubband_1 = timdata_patport[::8]
        portsubband_2 = timdata_patport[1::8]
        portsubband_3 = timdata_patport[2::8]
        portsubband_4 = timdata_patport[3::8]
        portsubband_5 = timdata_patport[4::8]
        portsubband_6 = timdata_patport[5::8]
        portsubband_7 = timdata_patport[6::8]
        portsubband_8 = timdata_patport[7::8]

        try:
            fig, axs = plt.subplots(3,3)
            axs[0, 0].scatter(stdsubband_1,portsubband_1,color='tab:blue',s=0.2,zorder=1)
            axs[0, 1].scatter(stdsubband_2,portsubband_2,color='tab:blue',s=0.2,zorder=1)
            axs[0, 2].scatter(stdsubband_3,portsubband_3,color='tab:blue',s=0.2,zorder=1)
            axs[1, 0].scatter(stdsubband_4,portsubband_4,color='tab:blue',s=0.2,zorder=1)
            axs[1, 1].plot()
            axs[1, 2].scatter(stdsubband_5,portsubband_5,color='tab:blue',s=0.2,zorder=1)
            axs[2, 0].scatter(stdsubband_6,portsubband_6,color='tab:blue',s=0.2,zorder=1)
            axs[2, 1].scatter(stdsubband_7,portsubband_7,color='tab:blue',s=0.2,zorder=1)
            axs[2, 2].scatter(stdsubband_8,portsubband_8,color='tab:blue',s=0.2,zorder=1)
            
            scale = np.array([timdata_patport.min(),timdata_1d.min()])
            fig.suptitle(pulsar)

            for ax in axs.flat:
                ax.set(xlabel=r'$\mathrm{1D}\/ (\mu s)$', ylabel=r'$\mathrm{portrait}\/ (\mu s)$')
                ax.label_outer()
                ax.set_xscale("log")
                ax.set_yscale("log")
                ax.set_xlim(left=scale.min(),right=10)
                ax.set_ylim(bottom=scale.min(),top=10)
                lims = [np.min([ax.get_xlim(), ax.get_ylim()]),np.max([ax.get_xlim(),ax.get_ylim()])]
                ax.plot(lims, lims, 'k-', alpha=0.5, zorder=2)

                fig.tight_layout()
                plt.savefig("/fred/oz002/users/mmiles/templates/2D_Templates/plots/subband_timing/"+pulsar+".png")
        except:
            pass
        '''
        '''
        #Below are the timing comparison graphs
        
        #Plots of the 2D Fscrunched portraits (pat) vs the 1D standards (pat), using the f128 data
        try:
            fig, ax = plt.subplots()
            ax.scatter(xdata,ydata,color='tab:blue',s=0.2, label = "Tf128 data")
            plt.xlabel(r'$\mathrm{1D \/timing}\/ (\mu s)$')
            plt.ylabel(r'$\mathrm{2D \/timing}\/ (\mu s)$')
            plt.legend()
            ax.set_title(pulsar)
            ax.set_yscale("log")
            ax.set_xscale("log")
            lims = [np.min([ax.get_xlim(), ax.get_ylim()]),np.max([ax.get_xlim(),ax.get_ylim()])]
            ax.plot(lims, lims, 'k-', alpha=0.75, zorder=0)
            fig.tight_layout()
            plt.savefig("/fred/oz002/users/mmiles/templates/2D_Templates/plots/2DFscrunched_v_1D_Tf128/"+pulsar+"_Tf4.png")
        except:
            pass
        
        #Plots of the 2D Fscrunched portraits (pat) vs the 1D standards (pat), using fully Fscrunched data
        try:
            fig, ax = plt.subplots()
            ax.scatter(xdataf,ydataf,color='tab:blue',s=0.5,label = "TF data")
            plt.xlabel(r'$\mathrm{1D \/timing}\/ (\mu s)$')
            plt.ylabel(r'$\mathrm{2D \/timing}\/ (\mu s)$')
            plt.legend()
            ax.set_title(pulsar)
            ax.set_yscale("log")
            ax.set_xscale("log")
            lims = [np.min([ax.get_xlim(), ax.get_ylim()]),np.max([ax.get_xlim(),ax.get_ylim()])]
            ax.plot(lims, lims, 'k-', alpha=0.75, zorder=0)
            fig.tight_layout()
            plt.savefig("/fred/oz002/users/mmiles/templates/2D_Templates/plots/2DFscrunched_v_1D_TF/"+pulsar+"_TF.png")
        except:
            pass
        
        #Plots of the 2D portrait timing (pptoas) vs the 1D standards (pat), using fully Fscrunched data
        try:
            fig, ax = plt.subplots()
            ax.scatter(xdataf,data_pptoa,color='tab:blue',s=0.2, label = "Pulse Portraiture timing vs 1D (TF data)")
            plt.xlabel(r'$\mathrm{1D \/timing}\/ (\mu s)$')
            plt.ylabel(r'$\mathrm{PP_2D \/timing}\/ (\mu s)$')
            plt.legend()
            ax.set_title(pulsar)
            ax.set_yscale("log")
            ax.set_xscale("log")
            lims = [np.min([ax.get_xlim(), ax.get_ylim()]),np.max([ax.get_xlim(),ax.get_ylim()])]
            ax.plot(lims, lims, 'k-', alpha=0.75, zorder=0)
            fig.tight_layout()
            plt.savefig("/fred/oz002/users/mmiles/templates/2D_Templates/plots/pptoa_v_1d_plots/"+pulsar+".png")
            #plt.figure()
        except:
            pass

        #Plots of the 2D portrait timing (pptoas, not fit for DM or bary) vs the 1D standards (pat), using fully Fscrunched data
        try:
            fig, ax = plt.subplots()
            ax.scatter(xdataf,data_pp_nodm,color='tab:blue',s=0.2, label = "Pulse Portraiture timing (no DM fit) vs 1D (TF data)")
            plt.xlabel(r'$\mathrm{1D \/timing}\/ (\mu s)$')
            plt.ylabel(r'$\mathrm{PP_2D \/timing}\/ (\mu s)$')
            plt.legend()
            ax.set_title(pulsar)
            ax.set_yscale("log")
            ax.set_xscale("log")
            lims = [np.min([ax.get_xlim(), ax.get_ylim()]),np.max([ax.get_xlim(),ax.get_ylim()])]
            ax.plot(lims, lims, 'k-', alpha=0.75, zorder=0)
            fig.tight_layout()
            plt.savefig("/fred/oz002/users/mmiles/templates/2D_Templates/plots/pptoa_noDM_v_1d_plots/"+pulsar+".png")
            #plt.figure()
        except:
            pass

        #Plots of the 2D portrait timing (pptoas) vs the 2D portrait timing (pptoas, not fit for DM or bary)
        try:
            fig, ax = plt.subplots()
            ax.scatter(data_pptoa,data_pp_nodm,color='tab:blue',s=0.2, label = "Pulse Portraiture timing with DM fit vs no DM fit")
            plt.xlabel(r'$\mathrm{PP_2D \/timing \/with \/fit}\/ (\mu s)$')
            plt.ylabel(r'$\mathrm{PP_2D \/timing \/no \/fit}\/ (\mu s)$')
            plt.legend()
            ax.set_title(pulsar)
            ax.set_yscale("log")
            ax.set_xscale("log")
            lims = [np.min([ax.get_xlim(), ax.get_ylim()]),np.max([ax.get_xlim(),ax.get_ylim()])]
            ax.plot(lims, lims, 'k-', alpha=0.75, zorder=0)
            fig.tight_layout()
            plt.savefig("/fred/oz002/users/mmiles/templates/2D_Templates/plots/pptoa_v_pptoa_nofit/"+pulsar+".png")
            #plt.figure()
        except:
            pass        

        #Plots of the pat portrait timing with the 1D Tf128 timing
        try:
            fig, ax = plt.subplots()
            ax.scatter(xdata, timdata_patport,color='tab:blue',s=0.2, label = "Pat portrait timing vs 1D timing (Tf128)")
            plt.xlabel(r'$\mathrm{1D \/Tf128 \/timing}\/ (\mu s)$')            
            plt.ylabel(r'$\mathrm{Pat \/portrait \/timing}\/ (\mu s)$')
            plt.legend()
            ax.set_title(pulsar)
            ax.set_yscale("log")
            ax.set_xscale("log")
            lims = [np.min([ax.get_xlim(), ax.get_ylim()]),np.max([ax.get_xlim(),ax.get_ylim()])]
            ax.plot(lims, lims, 'k-', alpha=0.75, zorder=0)
            fig.tight_layout()
            plt.savefig("/fred/oz002/users/mmiles/templates/2D_Templates/plots/patport2D_v_1D_Tf128/"+pulsar+".png")
            #plt.figure()
        except:
            pass 

        #Plots of pat portrait timing TF vs the pptoa timing
        try:
            fig, ax = plt.subplots()
            ax.scatter(data_pptoa,timdata_patportf,color='tab:blue',s=0.2, label = "Pat portrait timing vs pptoa timing (TF)")
            plt.xlabel(r'$\mathrm{PP_2D \/timing \/with \/fit}\/ (\mu s)$')
            plt.ylabel(r'$\mathrm{Pat \/portrait \/timing}\/ (\mu s)$')
            plt.legend()
            ax.set_title(pulsar)
            ax.set_yscale("log")
            ax.set_xscale("log")
            lims = [np.min([ax.get_xlim(), ax.get_ylim()]),np.max([ax.get_xlim(),ax.get_ylim()])]
            ax.plot(lims, lims, 'k-', alpha=0.75, zorder=0)
            fig.tight_layout()
            plt.savefig("/fred/oz002/users/mmiles/templates/2D_Templates/plots/patport2DTF_v_pptoa/"+pulsar+".png")
            #plt.figure()
        except:
            pass
        
        #64s and 256s data
        try:
            fig, ax = plt.subplots()
            ax.scatter(timdata64_1d,timdata64_portrait,color='tab:blue',s=0.2, label = "64s portrait vs 1D")
            plt.xlabel(r'$\mathrm{1D \/timing}\/ (\mu s)$')
            plt.ylabel(r'$\mathrm{Pat \/portrait \/timing}\/ (\mu s)$')
            plt.legend()
            ax.set_title(pulsar)
            ax.set_xlim(left=0.01,right=10)
            ax.set_ylim(bottom=0.01,top=10)
            ax.set_yscale("log")
            ax.set_xscale("log")
            lims = [np.min([ax.get_xlim(), ax.get_ylim()]),np.max([ax.get_xlim(),ax.get_ylim()])]
            ax.plot(lims, lims, 'k-', alpha=0.75, zorder=0)
            fig.tight_layout()
            plt.savefig("/fred/oz002/users/mmiles/templates/2D_Templates/plots/64_patport_v_1D/"+pulsar+".png")
            #plt.figure()
        except:
            pass
           
        try:
            fig, ax = plt.subplots()
            ax.scatter(timdata256_1d,timdata256_portrait,color='tab:blue',s=0.2, label = "256s portrait vs 1D")
            plt.xlabel(r'$\mathrm{1D \/timing}\/ (\mu s)$')
            plt.ylabel(r'$\mathrm{Pat \/portrait \/timing}\/ (\mu s)$')
            plt.legend()
            ax.set_title(pulsar)
            ax.set_xlim(left=0.01,right=10)
            ax.set_ylim(bottom=0.01,top=10)
            ax.set_yscale("log")
            ax.set_xscale("log")
            lims = [np.min([ax.get_xlim(), ax.get_ylim()]),np.max([ax.get_xlim(),ax.get_ylim()])]
            ax.plot(lims, lims, 'k-', alpha=0.75, zorder=0)
            fig.tight_layout()
            plt.savefig("/fred/oz002/users/mmiles/templates/2D_Templates/plots/256_patport_v_1D/"+pulsar+".png")
            #plt.figure()
        except:
            pass
        '''

        median_1d = np.median(timdata_1d)
        median_1d_fscrunched = np.median(timdata_1df)
        median_2d = np.median(timdata_2d)
        median_pptoa = np.median(timdata_pp)
        median_pptoa_nofit = np.median(timdata_ppnodm)
        median_patport = np.median(timdata_patport)
        median_patport_fscrunched = np.median(timdata_patportf)

        logdist_1d = np.log10(timdata_1d)
        logdist_2d = np.log10(timdata_2d)
        logdist_pptoa = np.log10(timdata_pp)
        logdist_pptoa_nofit = np.log10(timdata_ppnodm)
        logdist_patport = np.log10(timdata_patport)

        stdev_1d = np.std(logdist_1d)
        stdev_2d = np.std(logdist_2d)
        stdev_pp = np.std(logdist_pptoa)
        stdev_patport = np.log10(timdata_patport)

        error1 = 10**stdev_1d
        error2 = 10**stdev_2d
        error_pptoa = 10**stdev_pp
        error_patport = 10**stdev_patport
        
        if stdev_1d > stdev_2d:
            scaled_1d = 100
            scaled_2d = 100*(stdev_2d/stdev_1d)
        else:
            scaled_2d = 100
            scaled_1d = 100*(stdev_1d/stdev_2d)

        data = [pulsar, median_1d,median_1d_fscrunched, median_2d, median_pptoa, median_pptoa_nofit, median_patport,median_patport_fscrunched, error1, error2, error_pptoa, error_patport, scaled_1d, scaled_2d]

        df_timing.append(data)

labels = ['Pulsar', 'Median_1D','Median_1D_fscrunched', 'Median_2D', 'Median_pptoa','Median_pptoa_nofit', 'Median_patport','Median_patport_fscrunched', 'Error_1D', 'Error_2D', 'Error_pptoa', 'Error_patport','Scaled_Error_1D', 'Scaled_Error_2D']

timing_data = pd.DataFrame(df_timing, columns = labels)
#plt.show()
#Move the zero values into this array and drop them from the main series
zero_2D = []
zero_2D = timing_data.loc[timing_data['Median_2D'] == 0]
timing_data = timing_data[timing_data['Median_2D'] != 0]

zero_pp = []
zero_pp = timing_data.loc[timing_data['Median_pptoa'] == 0]
timing_data = timing_data[timing_data['Median_pptoa'] != 0]

xdata = timing_data["Median_1D"]
xdata_fscrunched = timing_data['Median_1D_fscrunched']
ydata = timing_data["Median_pptoa"]

med_patport = timing_data['Median_patport']
med_patport_fscrunched = timing_data['Median_patport_fscrunched']
med_nofit = timing_data['Median_pptoa_nofit']

xerr = timing_data["Error_1D"]

yerr = timing_data["Error_2D"]

#plt.show()
#Below are the median graphs

fig, ax1 = plt.subplots()

plt.style.use('seaborn-whitegrid')
ax1.scatter(xdata_fscrunched,med_patport_fscrunched, color='tab:blue', s=0.5, label='Median 1D timing vs portrait timing (fscrunched)')
#ax1.errorbar(xdata,ydata,xerr=xerr,yerr=yerr, fmt='o', color = 'tab:blue',ecolor='lightgray')
ax1.set_yscale('log')
ax1.set_xscale('log')
ax1.set_xlabel(r'$\mathrm{1D \/timing}\/ (\mu s)$')
ax1.set_ylabel(r'$\mathrm{Pat \/portrait \/timing}\/ (\mu s)$')
lims = [np.min([ax1.get_xlim(), ax1.get_ylim()]),np.max([ax1.get_xlim(),ax1.get_ylim()])]
ax1.plot(lims, lims, 'k-', alpha=0.75, zorder=0)
plt.legend()
fig.tight_layout()
#plt.savefig("/fred/oz002/users/mmiles/templates/2D_Templates/plots/medianplots/1D_v_pptoa")
plt.show()
'''
fig, ax1 = plt.subplots()
plt.style.use('seaborn-whitegrid')
ax1.scatter(xdata,med_patport, color='tab:blue', s=0.5, label='Median pat portrait timing vs median pat 1D timing')
#ax1.errorbar(xdata,ydata,xerr=xerr,yerr=yerr, fmt='o', color = 'tab:blue',ecolor='lightgray')
ax1.set_yscale('log')
ax1.set_xscale('log')
ax1.set_xlabel("1D Median")
ax1.set_ylabel("patport Median")
lims = [np.min([ax1.get_xlim(), ax1.get_ylim()]),np.max([ax1.get_xlim(),ax1.get_ylim()])]
ax1.plot(lims, lims, 'k-', alpha=0.75, zorder=0)
plt.legend()
fig.tight_layout()
plt.savefig("/fred/oz002/users/mmiles/templates/2D_Templates/plots/medianplots/1D_v_patport")

fig, ax1 = plt.subplots()
plt.style.use('seaborn-whitegrid')
ax1.scatter(med_patport, ydata, color='tab:blue', s=0.5, label='Median pptoa timing vs Median pat portrait timing')
#ax1.errorbar(xdata,ydata,xerr=xerr,yerr=yerr, fmt='o', color = 'tab:blue',ecolor='lightgray')
ax1.set_yscale('log')
ax1.set_xscale('log')
ax1.set_xlabel("patport Median")
ax1.set_ylabel("pptoa Median")
lims = [np.min([ax1.get_xlim(), ax1.get_ylim()]),np.max([ax1.get_xlim(),ax1.get_ylim()])]
ax1.plot(lims, lims, 'k-', alpha=0.75, zorder=0)
plt.legend()
fig.tight_layout()
plt.savefig("/fred/oz002/users/mmiles/templates/2D_Templates/plots/medianplots/patport_v_pptoa")

fig, ax1 = plt.subplots()
plt.style.use('seaborn-whitegrid')
ax1.scatter(ydata, med_nofit, color='tab:blue', s=0.5, label='Median pptoa timing vs Median pptoa timing no DM fit')
#ax1.errorbar(xdata,ydata,xerr=xerr,yerr=yerr, fmt='o', color = 'tab:blue',ecolor='lightgray')
ax1.set_yscale('log')
ax1.set_xscale('log')
ax1.set_xlabel("pptoa Median")
ax1.set_ylabel("pptoa Median no fit")
lims = [np.min([ax1.get_xlim(), ax1.get_ylim()]),np.max([ax1.get_xlim(),ax1.get_ylim()])]
ax1.plot(lims, lims, 'k-', alpha=0.75, zorder=0)
plt.legend()
fig.tight_layout()
plt.savefig("/fred/oz002/users/mmiles/templates/2D_Templates/plots/medianplots/pptoa_v_pptoa_noDM")
'''

#ax2 = ax1.twinx()
#ax2 = plt.errorbar(xdata,ydata,xerr=xerr,yerr=yerr, fmt='o', color = 'tab:blue',ecolor='lightgray')

'''
all_data1d = np.loadtxt("all_pulsars_1D.tim")
all_data2d = np.loadtxt("all_pulsars_2D.tim")

xdata = all_data1d
ydata = all_data2d
plt.scatter(xdata,ydata,color='tab:blue',s=0.2)
plt.xlabel(r'1D \/timing\/ \mu s")
plt.ylabel(r'2D \/timing\/ \mu s")
plt.yscale("log")
plt.xscale("log")
plt.figure()
'''

#plt.show()

    