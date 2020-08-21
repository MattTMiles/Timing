#!/usr/bin/env bash

cd  /fred/oz002/users/mmiles/templates/2D_Templates/$1/pol_profs/


~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_residual_plots.py -m 2D.spline.$1.spl -d metafile_average.$1.Tp.port.mohsen --nowb -r 0.5 ;
cp metafile*resids.png ../../residuals/ ;