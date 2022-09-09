# Per frequency band code to check how the template is performing as an average
# Input an archive and a portrait that you want to check against


import matplotlib.pyplot as plt 
from matplotlib.pyplot import text
import numpy as np
import pandas as pd
import sys
import os
import subprocess as sproc 
from scipy.stats import chisquare
from scipy.optimize import minimize, curve_fit
import psrchive
import filecmp
import glob
import argparse
from matplotlib import ticker

#Argument parsing
parser = argparse.ArgumentParser(description="Subband comparison")
parser.add_argument("-portrait", dest="portrait", help="Portrait to use", required = True)
parser.add_argument("-archive", dest="archive", help="Archive to compare portrait against. Specify 'all' to work through a directory of .ar files (not recommended).", required = True)
parser.add_argument("-ephemeris", dest="ephemeris", help="Ephemeris file to use", required = True)
parser.add_argument("-subbands", dest="subbands", help="Specify the number of subbands to compare", required = True)
parser.add_argument("-save", dest="save", action='store_true',default=False, help="(Optional) Adding this flag will save the plot")
parser.add_argument("-dir", dest="dir", action='store_true',default=False, help="(Optional) Adding this flag will specify a directory to save in")
parser.add_argument("-trim", dest="trim", action='store_true',default=False, help="(Optional) Adding this flag creates a plot with only 4 subbands shown")

#parser.add_argument("-chi2", dest="chi2", action='saves subbanded chi2', default=False, help="(Optional) Adding this flag will save subbanded reduced chi squared distributions.")
#parser.add_argument("--save")
args = parser.parse_args()

portrait = str(args.portrait)
archive = str(args.archive)
eph = str(args.ephemeris)

subbands = int(args.subbands)

directory = str(args.dir)

pulsar = eph.split('.')[0]
pulsar = pulsar.split('/')[-1]


#Load in the portrait
ppfile = psrchive.Archive_load(portrait)

#Define standard for shifting profiles later
std = ppfile
std.fscrunch()
std.pscrunch()
std.dedisperse()
std.remove_baseline()

#Dedisperse portrait file
p = sproc.Popen('pam -mD {0}'.format(portrait),shell=True)
p.wait()

#Scrunch to required number of subbands
p = sproc.Popen('pam -e {0}chan --setnchn {0} {1}'.format(subbands, portrait),shell=True)
p.wait()

port_trim = os.path.splitext(portrait)[0]
port_sub = os.path.splitext(portrait)[0]+'.'+str(subbands)+'chan'

if archive == 'all':
    for files in glob.glob("J*ar"):
        if not os.path.isfile(files.split('.ar')[0]+'.paz'):
            p = sproc.Popen('paz -r '+files+' -e paz', shell=True)
            p.wait()
    

    #Initialise all the J*paz so that they only update when they see a new file

    p = sproc.Popen('echo "`ls J*paz`" > to_add',shell=True)
    p.wait()

    if os.path.isfile('added'):
        if not filecmp.cmp('to_add','added'):
            p = sproc.Popen('pam -mE {0} J*paz'.format(eph),shell=True)
            p.wait()

            p = sproc.Popen('psradd -TP J*paz -o grand.paz',shell=True)
            p.wait()

            p = sproc.Popen('pam -mp grand.paz',shell=True)
            p.wait()

            p = sproc.Popen('pam -mD grand.paz',shell=True)
            p.wait()

            p = sproc.Popen('pam -e {0}chan --setnchn {0} grand.paz'.format(subbands),shell=True)
            p.wait()

            p = sproc.Popen('echo "`ls J*paz`" > added',shell=True)
            p.wait()

            if not os.path.isfile('grand.00{1:02d}_0000.{0}chan'.format(subbands,subbands-1)):
                p = sproc.Popen('psrsplit grand.{0}chan -c 1'.format(subbands),shell=True)
                p.wait()

    else:
        p = sproc.Popen('pam -mE {0} J*paz'.format(eph),shell=True)
        p.wait()

        p = sproc.Popen('psradd -TP J*paz -o grand.paz',shell=True)
        p.wait()

        p = sproc.Popen('pam -mp grand.paz',shell=True)
        p.wait()

        p = sproc.Popen('pam -mD grand.paz',shell=True)
        p.wait()

        p = sproc.Popen('pam -e {0}chan --setnchn {0} grand.paz'.format(subbands),shell=True)
        p.wait()

        p = sproc.Popen('echo "`ls J*paz`" > added',shell=True)
        p.wait()

        if not os.path.isfile('grand.00{1:02d}_0000.{0}chan'.format(subbands,subbands-1)):
            p = sproc.Popen('psrsplit grand.{0}chan -c 1'.format(subbands),shell=True)
            p.wait()

else:
    # rfi excise the archive file and organise into the subband splits
    p = sproc.Popen('paz -r {0} -e paz'.format(archive), shell=True)
    p.wait()
    pazarch = archive.split('.')[0]+'.paz'
    
    p = sproc.Popen('pam -mE {0} {1}'.format(eph,pazarch),shell=True)
    p.wait()

    p = sproc.Popen('pam -mTp {0}'.format(pazarch),shell=True)
    p.wait()

    p = sproc.Popen('pam -mD {0}'.format(pazarch),shell=True)
    p.wait()

    p = sproc.Popen('pam -e {0}chan --setnchn {0} {1}'.format(subbands,pazarch),shell=True)
    p.wait()

    charch = os.path.splitext(pazarch)[0]+'.'+str(subbands)+'chan'

    if not os.path.isfile('{0}.00{2:02d}_0000.{1}chan'.format(charch.split('.')[0],subbands,subbands-1)):
        p = sproc.Popen('psrsplit {0} -c 1'.format(charch),shell=True)
        p.wait()

    
def fft_rotate(data, bins):
    """Return data rotated by 'bins' places to the left. The
        rotation is done in the Fourier domain using the Shift Theorem.

        Inputs:
            data: A 1-D numpy array to rotate.
            bins: The (possibly fractional) number of bins to rotate by.

        Outputs:
            rotated: The rotated data.
    (inspired from CoastGuard)
    """
    freqs = np.arange(data.size/2+1, dtype=float)
    phasor = np.exp(complex(0.0, 2.0*np.pi) * freqs * bins / float(data.size))
    return np.fft.irfft(phasor*np.fft.rfft(data))


sprof = std.get_Profile(0,0,0)

grandname = archive.split(".")[0]
grandfile = psrchive.Archive_load(grandname+'.{}chan'.format(subbands)) 
grandfile.remove_baseline()
grandfile.dedisperse()

ppfile.remove_baseline()
ppfile.dedisperse()


#Split into the subbands to compare against
if not os.path.isfile('{0}.00{2:02d}_0000.{1}chan'.format(port_trim,subbands,subbands-1)):
    p = sproc.Popen('psrsplit {0} -c 1'.format(port_sub),shell=True)
    p.wait()

#Define the profile shift off of the standard 
ssf = psrchive.ProfileShiftFit()
ssf.set_standard(sprof)

granddata = grandfile.get_data()
ppdata = ppfile.get_data()

granddata = granddata[0,0,:,:]
ppdata = ppdata[0,0,:,:]

#The amount of fitting points as specified by pulse portraiture
dof = 1022

freqs = []

vars = []
redchis = []

for i in range(0,subbands):
    locals()['grandfile{0}'.format(i)] = psrchive.Archive_load('{0}.00{1:02d}_0000.{2}chan'.format(grandname,i,subbands))
    activefile = locals()['grandfile{0}'.format(i)]
    activefile.remove_baseline()

    freq = activefile.get_centre_frequency()
    freqs.append(freq)
    
    locals()['gf{0}_prof'.format(i)] = activefile[0].get_Profile(0,0)
    active_prof = locals()['gf{0}_prof'.format(i)]

    locals()['ppfile{0}'.format(i)] = psrchive.Archive_load('{0}.00{1:02d}_0000.{2}chan'.format(port_trim,i,subbands))
    ppfile = locals()['ppfile{0}'.format(i)]
    ppfile.remove_baseline()
    
    locals()['ppf{0}_prof'.format(i)] = ppfile[0].get_Profile(0,0)
    ppf_prof = locals()['ppf{0}_prof'.format(i)]

    ssf.apply_scale_and_shift(ppf_prof)
    psf = psrchive.ProfileShiftFit()

    psf.set_standard(ppf_prof)
    psf.set_Profile(active_prof)

    scale = psf.get_scale()[0]

    psf.apply_scale_and_shift(active_prof)


    locals()['ppdata{0}'.format(i)] = ppf_prof.get_amps()
    ppdata = locals()['ppdata{0}'.format(i)]
    locals()['granddata{0}'.format(i)] = active_prof.get_amps()
    granddata = locals()['granddata{0}'.format(i)]

    def func(temp_profile, amp, phs):
        return amp*fft_rotate(temp_profile, phs)

    amplitude = 1
    phase =  0

    locals()['ppdata_fitted{0}'.format(i)] = func(ppdata,amplitude,phase)
    ppdata_fitted = locals()['ppdata_fitted{0}'.format(i)]

    locals()['offpulse_{0}'.format(i)] = np.where(ppdata<0.01*ppdata.max())[0]
    offpulse_int = locals()['offpulse_{0}'.format(i)]

    locals()['offgrand_{0}'.format(i)] = granddata[offpulse_int]
    offgrand = locals()['offgrand_{0}'.format(i)]

    locals()['offport_{0}'.format(i)] = ppdata[offpulse_int]
    offport = locals()['offport_{0}'.format(i)]

    offres = offport-offgrand
    

    offres_sub = offres - np.mean(offres)

    locals()['res{0}'.format(i)] = ppdata_fitted-granddata
    res = locals()['res{0}'.format(i)]

    locals()['var{0}'.format(i)] = np.var(offres)
    var = locals()['var{0}'.format(i)]
    print("Off Pulse Variance: {}".format(var))

    varsub = np.var(offres_sub)

    ratio = var/varsub
    print('RFI: {}'.format(ratio))

    locals()['chi{0}'.format(i)] = sum(((res)**2)/var)
    chi = locals()['chi{0}'.format(i)]

    chi_sub = sum(((offres)**2)/varsub)
    locals()['redchisub{0}'.format(i)] = chi_sub/(len(offpulse_int)-2)
    redchisub = locals()['redchisub{0}'.format(i)]
    
    print('redchisub: {}'.format(redchisub))
    
    locals()['redchi{0}'.format(i)] = chi/dof
    redchi = locals()['redchi{0}'.format(i)]

    vars.append(var)
    redchis.append(redchi)

ave_var = np.mean(vars)
ave_redchi = np.mean(redchis)

np.save('redchi_{}'.format(pulsar),redchis)

if args.trim is not True:
    fig = plt.figure(figsize=(15,2*subbands))

    ax = fig.subplots(subbands,2,sharex=True)

    #if subbands == 8:
    j=0
    for ii,i in enumerate(reversed(range(0,subbands))):

        ppdata = locals()['ppdata{0}'.format(i)]
        ppdata_fitted = locals()['ppdata_fitted{0}'.format(i)]
        granddata = locals()['granddata{0}'.format(i)]
        res = locals()['res{0}'.format(i)]
        scalefactor = 800/(subbands+1)
        res_scalefactor = 400/(subbands+1)
        chi = locals()['chi{}'.format(i)]
        redchi = locals()['redchi{}'.format(i)]
        redchisub = locals()['redchisub{0}'.format(i)]

        ax[ii,j].plot((ppdata_fitted*(scalefactor/ppdata_fitted.max()))+freqs[i],linewidth=1,c='tab:blue',label='Pulse Portraiture')
        ax[ii,j].plot((granddata*(scalefactor/ppdata_fitted.max()))+freqs[i],linewidth=0.5,c='tab:red',label='Chosen Archive')
        ax[ii,j].get_yaxis().set_visible(False)
        ax[ii,j].set_title('Centre Frequency: {0}'.format(freqs[i]))

        ax[ii,j+1].plot(res,linewidth=0.5,c='black',label='residual')
        ax[ii,j+1].axhline(0,linestyle='--',linewidth=0.5,c='dimgray')

        ax[ii,j+1].set_title(r'total $\chi_{r}^{2}$ = %.3f; offpulse $\chi_{r}^{2}$ = %.3f' % (redchi, redchisub))




    ax[0,0].legend(['Pulse Portraiture','Chosen Archive'],bbox_to_anchor=(0.25,1.5))
    ax[0,1].legend(['Residual'],bbox_to_anchor=(1,1.5))

    fig.suptitle('{0}: mean total $\chi_r^2$ = {1:.3f}'.format(pulsar,ave_redchi))

    fig.tight_layout()
    #fig.show()
    #plt.show()
    '''if args.save is True:
        fig.savefig('{0}_{1}_comparison.pdf'.format(pulsar,subbands),format='pdf',dpi=600)'''
    try:
        archive_strip = archive.split('/')[-1]
    except:
        archive_strip = archive

    if args.save is True:
        if args.dir is True:
            fig.savefig(directory+'{0}_{1}_{2}_notebook_comparison.pdf'.format(pulsar,archive_strip,subbands),format='pdf',dpi=1000)
        else:
            fig.savefig('{0}_{1}_{2}_notebook_comparison.pdf'.format(pulsar,archive_strip,subbands),format='pdf',dpi=1000)

if args.trim is True:
    font=20
    fig = plt.figure(figsize=(20,12.5))

    ax = fig.subplots(4,2,sharex=True)
    j=0
    for ii,i in enumerate(reversed(range(0,subbands)[::4])):

        ppdata = locals()['ppdata{0}'.format(i)]
        ppdata_fitted = locals()['ppdata_fitted{0}'.format(i)]
        granddata = locals()['granddata{0}'.format(i)]
        res = locals()['res{0}'.format(i)]
        scalefactor = 800/(subbands+1)
        res_scalefactor = 400/(subbands+1)
        chi = locals()['chi{}'.format(i)]
        redchi = locals()['redchi{}'.format(i)]
        redchisub = locals()['redchisub{0}'.format(i)]

        ax[ii,j].plot((granddata*(scalefactor/ppdata_fitted.max()))+freqs[i],linewidth=0.5,c='tab:red',label='Chosen Archive')
        ax[ii,j].plot((ppdata_fitted*(scalefactor/ppdata_fitted.max()))+freqs[i],linewidth=2,linestyle="--",dashes=(5,5),c='tab:blue',label='Pulse Portraiture')
        ax[ii,j].get_yaxis().set_visible(False)
        ax[ii,j].set_title('Centre Frequency: {0}'.format(freqs[i]),fontsize=font)
        ax[ii,j].tick_params(labelsize=font)
        positions = [0,512,1024]
        labels = ['0','0.5','1']
        

        ax[ii,j+1].plot(res,linewidth=0.5,c='black',label='residual')
        ax[ii,j+1].axhline(0,linestyle='--',linewidth=0.5,c='dimgray')
        ax[ii,j+1].tick_params(labelsize=font)

        ax[ii,j+1].set_title(r'Total $\chi_{r}^{2}$ = %.3f; Offpulse $\chi_{r}^{2}$ = %.3f' % (redchi, redchisub),fontsize=font)
    
    ax[ii,j].xaxis.set_major_locator(ticker.FixedLocator(positions))
    ax[ii,j].xaxis.set_major_formatter(ticker.FixedFormatter(labels))
    

    ax[ii,j+1].xaxis.set_major_locator(ticker.FixedLocator(positions))
    ax[ii,j+1].xaxis.set_major_formatter(ticker.FixedFormatter(labels))
    

    ax[0,0].legend(['Chosen Archive','Pulse Portraiture'],bbox_to_anchor=(0.25,1.6),fontsize=font)
    ax[0,1].legend(['Residual'],bbox_to_anchor=(1,1.5),fontsize=font)

    fig.suptitle('{0}: Mean total $\chi_r^2$ = {1:.3f}'.format(pulsar,ave_redchi),fontsize=font)
    fig.supylabel("Normalised Flux (arb. units)",fontsize=font)
    fig.supxlabel("Pulse Phase",fontsize=font)

    fig.tight_layout()

    try:
        archive_strip = archive.split('/')[-1]
    except:
        archive_strip = archive

    if args.save is True:
        if args.dir is True:
            fig.savefig(directory+'{0}_{1}_{2}_notebook_comparison.pdf'.format(pulsar,archive_strip,4),format='pdf',dpi=1000)
        else:
            fig.savefig('/fred/oz002/users/mmiles/MSP_DR/paper_plots/trimmed/{0}_{1}_{2}_notebook_comparison.pdf'.format(pulsar,archive_strip,4),format='pdf',dpi=1000)





