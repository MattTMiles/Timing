import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import os 
import sys
import subprocess as sproc

chisquare_dir = '/fred/oz002/users/mmiles/templates/2D_Templates/pp_grand_comp'
os.chdir(chisquare_dir)

cs_data = pd.read_pickle('data_chisquare.pkl')

subband1 = cs_data['red_chi1'].to_numpy()
subband2 = cs_data['red_chi2'].to_numpy()
subband3 = cs_data['red_chi3'].to_numpy()
subband4 = cs_data['red_chi4'].to_numpy()
subband5 = cs_data['red_chi5'].to_numpy()
subband6 = cs_data['red_chi6'].to_numpy()
subband7 = cs_data['red_chi7'].to_numpy()
subband8 = cs_data['red_chi8'].to_numpy()

t = [950.508000,1054.402000,1150.282000,1274.552000,1376.517000,1477.161000,1615.783000,1658.082000]
cmap = plt.get_cmap('viridis')
norm = mpl.colors.Normalize(vmin=800,vmax=1700)
sm=plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cmapt = (np.array(t)-800)/900

fig, axs = plt.subplots(3,3)
axs[0,0].hist(subband1,bins=25,label='subband 1',color=cmap(cmapt[0]))
axs[0,0].set_title(r'$median \/ \chi_\nu^2$:{0:.03f}'.format(np.median(subband1)))

axs[0,1].hist(subband2,bins=25,label='subband 2',color=cmap(cmapt[1]))
axs[0,1].set_title(r'$median \/ \chi_\nu^2$:{0:.03f}'.format(np.median(subband2)))

axs[0,2].hist(subband3,bins=25,label='subband 3',color=cmap(cmapt[2]))
axs[0,2].set_title(r'$median \/ \chi_\nu^2$:{0:.03f}'.format(np.median(subband3)))

axs[1,0].hist(subband4,bins=25,label='subband 4',color=cmap(cmapt[3]))
axs[1,0].set_title(r'$median \/ \chi_\nu^2$:{0:.03f}'.format(np.median(subband4)))

axs[1,2].hist(subband5,bins=25,label='subband 5',color=cmap(cmapt[4]))
axs[1,2].set_title(r'$median \/ \chi_\nu^2$:{0:.03f}'.format(np.median(subband5)))

axs[2,0].hist(subband6,bins=25,label='subband 6',color=cmap(cmapt[5]))
axs[2,0].set_title(r'$median \/ \chi_\nu^2$:{0:.03f}'.format(np.median(subband6)))

axs[2,1].hist(subband7,bins=25,label='subband 7',color=cmap(cmapt[6]))
axs[2,1].set_title(r'$median \/ \chi_\nu^2$:{0:.03f}'.format(np.median(subband7)))

axs[2,2].hist(subband8,bins=25,label='subband 4',color=cmap(cmapt[7]))
axs[2,2].set_title(r'$median \/ \chi_\nu^2$:{0:.03f}'.format(np.median(subband8)))

axs[1,1].axis('off')
for ax in axs.flat:
    ax.set_xlim(0.9,2.5)
    ax.set_ylim(0,170)
    ax.set_xscale('log')
#ax.set_xscale('log')
#ax.set_yscale('log')
#fig.subplots_adjust(right=0.7)
#cbar_ax = fig.add_axes([0.95, 0.15, 0.05, 0.7])
cbar = fig.colorbar(sm,ticks=np.linspace(800,1700,10),ax=axs.ravel().tolist())
cbar.set_label('Frequency')
fig.suptitle('reduced chi-squared')
#fig.tight_layout()
fig.show()


