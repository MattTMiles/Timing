import os
import glob
import sys
import errno

pulsar = sys.argv[1]

main_dir = '/fred/oz002/users/mmiles/templates/2D_Templates'
pulsar_dir = os.path.join(main_dir, pulsar)
pol_profs = os.path.join(pulsar_dir,'pol_profs')

meerpipe_1D = os.path.join(main_dir,'meerpipe_1D')

os.chdir(pol_profs)

#os.system('psrsmooth -W *tot.ar')
os.system('mv *Tf4_tot.ar.sm '+pulsar+'.meerpipe_std')
os.system('mv '+pulsar+'.meerpipe_std '+meerpipe_1D)