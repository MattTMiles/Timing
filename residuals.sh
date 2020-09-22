#!/usr/bin/env bash

cd  /fred/oz002/users/mmiles/templates/2D_Templates/$1/pol_profs/

~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppalign.py -M metafile -T -I constant_profile.$1.Tp.paz.port -o metafile_average.$1.Tp.port --niter 2
~/.conda/envs/py2/bin/python /fred/oz005/users/mshamoha/federico/rfihunter_nogate.py 0 metafile_average.$1.Tp.port
#~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_residual_plots.py -m 2D.spline.$1.spl -d metafile_average.$1.Tp.port.mohsen --nowb -r 0.5 ;
#cp metafile*resids.png ../../residuals/ ;