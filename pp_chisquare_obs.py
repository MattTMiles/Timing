#Per frequency band code to check a new observation

import matplotlib.pyplot as plt 
from matplotlib.pyplot import text
import numpy as np
import pandas as pd
import sys
import os
import subprocess as sproc 
from scipy.stats import chisquare
import psrchive
import glob

parent_dir = '/fred/oz002/users/mmiles/templates/2D_Templates/'
pulsar = sys.argv[1]

pulsar_dir = os.path.join(parent_dir,pulsar)

stdfile = '/fred/oz002/users/mmiles/templates/msp_templates/'+pulsar+'.std'

os.chdir(pulsar_dir)

for files in glob.glob('J*ar'):

    if not os.path.isfile(files.split('.ar')[0]+'.paz'):
        p = sproc.Popen('paz -r '+files+' -e paz', shell=True)
        p.wait()

        p = sproc.Popen('pam -mp '+files.split('.ar')[0]+'.paz',shell=True)
        p.wait()

        p = sproc.Popen('pam -e 8chan --setnchn 8 '+files.split('.ar')[0]+'.paz',shell=True)
        p.wait()

        p = sproc.Popen('pam -mD '+files.split('.ar')[0]+'.8chan',shell=True)
        p.wait()


std = psrchive.Archive_load(stdfile)
sprof = std[0].get_Profile(0,0)

grandfile = psrchive.Archive_load('grand.8chan') 
ppfile = psrchive.Archive_load('2D.portrait.'+pulsar+'.Tp.paz.norm.8chan')

grandfile.remove_baseline()
grandfile.dedisperse()
ppfile.remove_baseline()
ppfile.dedisperse()

data = []

for obs in os.listdir(pulsar_dir):
    if obs.startswith('J') and obs.endswith('8chan') and not obs.endswith('0000.8chan'):
        if not os.path.isfile(obs.split('.8chan')[0]+'.0000_0000.8chan'):
    
            p=sproc.Popen('psrsplit '+obs+' -c 1',shell =True)
            p.wait()

            base = os.path.splitext(obs)[0]
            grandfile1 = psrchive.Archive_load(base+'.0000_0000.8chan')
            grandfile2 = psrchive.Archive_load(base+'.0001_0000.8chan')
            grandfile3 = psrchive.Archive_load(base+'.0002_0000.8chan')
            grandfile4 = psrchive.Archive_load(base+'.0003_0000.8chan')
            grandfile5 = psrchive.Archive_load(base+'.0004_0000.8chan')
            grandfile6 = psrchive.Archive_load(base+'.0005_0000.8chan')
            grandfile7 = psrchive.Archive_load(base+'.0006_0000.8chan')
            grandfile8 = psrchive.Archive_load(base+'.0007_0000.8chan')
            grandfile1.remove_baseline()
            grandfile2.remove_baseline()
            grandfile3.remove_baseline()
            grandfile4.remove_baseline()
            grandfile5.remove_baseline()
            grandfile6.remove_baseline()
            grandfile7.remove_baseline()
            grandfile8.remove_baseline()

            gf1_prof = grandfile1[0].get_Profile(0,0)
            gf2_prof = grandfile2[0].get_Profile(0,0)
            gf3_prof = grandfile3[0].get_Profile(0,0)
            gf4_prof = grandfile4[0].get_Profile(0,0)
            gf5_prof = grandfile5[0].get_Profile(0,0)
            gf6_prof = grandfile6[0].get_Profile(0,0)
            gf7_prof = grandfile7[0].get_Profile(0,0)
            gf8_prof = grandfile8[0].get_Profile(0,0)
            
            ppfile1 = psrchive.Archive_load('2D.portrait.'+pulsar+'.Tp.paz.norm.0000_0000.8chan')
            ppfile2 = psrchive.Archive_load('2D.portrait.'+pulsar+'.Tp.paz.norm.0001_0000.8chan')
            ppfile3 = psrchive.Archive_load('2D.portrait.'+pulsar+'.Tp.paz.norm.0002_0000.8chan')
            ppfile4 = psrchive.Archive_load('2D.portrait.'+pulsar+'.Tp.paz.norm.0003_0000.8chan')
            ppfile5 = psrchive.Archive_load('2D.portrait.'+pulsar+'.Tp.paz.norm.0004_0000.8chan')
            ppfile6 = psrchive.Archive_load('2D.portrait.'+pulsar+'.Tp.paz.norm.0005_0000.8chan')
            ppfile7 = psrchive.Archive_load('2D.portrait.'+pulsar+'.Tp.paz.norm.0006_0000.8chan')
            ppfile8 = psrchive.Archive_load('2D.portrait.'+pulsar+'.Tp.paz.norm.0007_0000.8chan')
            ppfile1.remove_baseline()
            ppfile2.remove_baseline()
            ppfile3.remove_baseline()
            ppfile4.remove_baseline()
            ppfile5.remove_baseline()
            ppfile6.remove_baseline()
            ppfile7.remove_baseline()
            ppfile8.remove_baseline()

            ppf1_prof = ppfile1[0].get_Profile(0,0)
            ppf2_prof = ppfile2[0].get_Profile(0,0)
            ppf3_prof = ppfile3[0].get_Profile(0,0)
            ppf4_prof = ppfile4[0].get_Profile(0,0)
            ppf5_prof = ppfile5[0].get_Profile(0,0)
            ppf6_prof = ppfile6[0].get_Profile(0,0)
            ppf7_prof = ppfile7[0].get_Profile(0,0)
            ppf8_prof = ppfile8[0].get_Profile(0,0)

            psf = psrchive.ProfileShiftFit()
            psf.set_standard(sprof)

            psf.apply_scale_and_shift(ppf1_prof)
            psf.apply_scale_and_shift(ppf2_prof)
            psf.apply_scale_and_shift(ppf3_prof)
            psf.apply_scale_and_shift(ppf4_prof)
            psf.apply_scale_and_shift(ppf5_prof)
            psf.apply_scale_and_shift(ppf6_prof)
            psf.apply_scale_and_shift(ppf7_prof)
            psf.apply_scale_and_shift(ppf8_prof)

            psf.apply_scale_and_shift(gf1_prof)
            psf.apply_scale_and_shift(gf2_prof)
            psf.apply_scale_and_shift(gf3_prof)
            psf.apply_scale_and_shift(gf4_prof)
            psf.apply_scale_and_shift(gf5_prof)
            psf.apply_scale_and_shift(gf6_prof)
            psf.apply_scale_and_shift(gf7_prof)
            psf.apply_scale_and_shift(gf8_prof)

            freqs = [944.238,1041.15,1138.148,1235.116,1332.065,1429.032,1525.986,1622.992]

            ppdata1 = ppf1_prof.get_amps()
            ppdata2 = ppf2_prof.get_amps()
            ppdata3 = ppf3_prof.get_amps()
            ppdata4 = ppf4_prof.get_amps()
            ppdata5 = ppf5_prof.get_amps()
            ppdata6 = ppf6_prof.get_amps()
            ppdata7 = ppf7_prof.get_amps()
            ppdata8 = ppf8_prof.get_amps()

            granddata1 = gf1_prof.get_amps()
            granddata2 = gf2_prof.get_amps()
            granddata3 = gf3_prof.get_amps()
            granddata4 = gf4_prof.get_amps()
            granddata5 = gf5_prof.get_amps()
            granddata6 = gf6_prof.get_amps()
            granddata7 = gf7_prof.get_amps()
            granddata8 = gf8_prof.get_amps()

            res1 = ppdata1-granddata1
            res2 = ppdata2-granddata2
            res3 = ppdata3-granddata3
            res4 = ppdata4-granddata4
            res5 = ppdata5-granddata5
            res6 = ppdata6-granddata6
            res7 = ppdata7-granddata7
            res8 = ppdata8-granddata8

            dof = 1023

            var1 = np.var(res1)
            chi1 = sum(((res1)**2)/var1)
            redchi1 = chi1/dof

            var2 = np.var(res2)
            chi2 = sum(((res2)**2)/var2)
            redchi2 = chi2/dof

            var3 = np.var(res3)
            chi3 = sum(((res3)**2)/var3)
            redchi3 = chi3/dof

            var4 = np.var(res4)
            chi4 = sum(((res4)**2)/var4)
            redchi4 = chi4/dof

            var5 = np.var(res5)
            chi5 = sum(((res5)**2)/var5)
            redchi5 = chi5/dof

            var6 = np.var(res6)
            chi6 = sum(((res6)**2)/var6)
            redchi6 = chi6/dof

            var7 = np.var(res7)
            chi7 = sum(((res7)**2)/var7)
            redchi7 = chi7/dof

            var8 = np.var(res8)
            chi8 = sum(((res8)**2)/var8)
            redchi8 = chi8/dof

            averedchi = np.mean([redchi1,redchi2,redchi3,redchi4,redchi5,redchi6,redchi7,redchi8])

            data.append([obs, redchi1, redchi2, redchi3, redchi4, redchi5, redchi6, redchi7, redchi8, averedchi])


            scalefactor = 100/ppdata1.max()
            res_scalefactor = 100/ppdata1.max()

            fig,(ax1,ax2) =plt.subplots(1,2,figsize=(9.60,5.40)) 

            ax1.plot((ppdata1*(100/ppdata1.max()))+freqs[0],linewidth=1,c='tab:blue',label='pulse portraiture')
            ax1.plot((granddata1*(100/granddata1.max()))+freqs[0],linewidth=0.5,c='tab:red',label='grand profile')

            ax1.plot((ppdata2*(100/ppdata2.max()))+freqs[1],linewidth=1,c='tab:blue')
            ax1.plot((granddata2*(100/granddata2.max()))+freqs[1],linewidth=0.5,c='tab:red')

            ax1.plot((ppdata3*(100/ppdata3.max()))+freqs[2],linewidth=1,c='tab:blue')
            ax1.plot((granddata3*(100/granddata3.max()))+freqs[2],linewidth=0.5,c='tab:red')

            ax1.plot((ppdata4*(100/ppdata4.max()))+freqs[3],linewidth=1,c='tab:blue')
            ax1.plot((granddata4*(100/granddata4.max()))+freqs[3],linewidth=0.5,c='tab:red')

            ax1.plot((ppdata5*(100/ppdata5.max()))+freqs[4],linewidth=1,c='tab:blue')
            ax1.plot((granddata5*(100/granddata5.max()))+freqs[4],linewidth=0.5,c='tab:red')

            ax1.plot((ppdata6*(100/ppdata6.max()))+freqs[5],linewidth=1,c='tab:blue')
            ax1.plot((granddata6*(100/granddata6.max()))+freqs[5],linewidth=0.5,c='tab:red')

            ax1.plot((ppdata7*(100/ppdata7.max()))+freqs[6],linewidth=1,c='tab:blue')
            ax1.plot((granddata7*(100/granddata7.max()))+freqs[6],linewidth=0.5,c='tab:red')

            ax1.plot((ppdata8*(100/ppdata8.max()))+freqs[7],linewidth=1,c='tab:blue')
            ax1.plot((granddata8*(100/granddata8.max()))+freqs[7],linewidth=0.5,c='tab:red')

            ax2.plot((res1*(res1.max()/np.var(res1)))+freqs[0],linewidth=0.5,c='black',label='residual')
            text(5,964.238, r'$\chi_{r}^{2}$ = %.3f' % redchi1)
            ax2.plot((res2*(res2.max()/np.var(res2)))+freqs[1],linewidth=0.5,c='black')
            text(5,1061.15, r'$\chi_{r}^{2}$ = %.3f' % redchi2)
            ax2.plot((res3*(res3.max()/np.var(res3)))+freqs[2],linewidth=0.5,c='black')
            text(5,1158.148, r'$\chi_{r}^{2}$ = %.3f' % redchi3)
            ax2.plot((res4*(res4.max()/np.var(res4)))+freqs[3],linewidth=0.5,c='black')
            text(5,1255.116, r'$\chi_{r}^{2}$ = %.3f' % redchi4)
            ax2.plot((res5*(res5.max()/np.var(res5)))+freqs[4],linewidth=0.5,c='black')
            text(5,1352.065, r'$\chi_{r}^{2}$ = %.3f' % redchi5)
            ax2.plot((res6*(res6.max()/np.var(res6)))+freqs[5],linewidth=0.5,c='black')
            text(5,1449.032, r'$\chi_{r}^{2}$ = %.3f' % redchi6)
            ax2.plot((res7*(res7.max()/np.var(res7)))+freqs[6],linewidth=0.5,c='black')
            text(5,1545.986, r'$\chi_{r}^{2}$ = %.3f' % redchi7)
            ax2.plot((res8*(res8.max()/np.var(res8)))+freqs[7],linewidth=0.5,c='black')
            text(5,1642.992, r'$\chi_{r}^{2}$ = %.3f' % redchi8)

            ax1.legend(bbox_to_anchor=(1,1))
            ax2.legend(bbox_to_anchor=(1,1))
            fig.tight_layout()
            
            #fig.show()
            fig.savefig(obs+'_pp_comp.pdf',format='pdf',dpi=1200)

plt.show()
labels = ['observation','red_chi1','red_chi2','red_chi3','red_chi4','red_chi5','red_chi6','red_chi7','red_chi8','ave_red_chi']

df = pd.DataFrame(data,columns=labels)

df.to_pickle(pulsar+'obs_chisquares.pkl')


