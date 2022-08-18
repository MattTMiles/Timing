#!/usr/bin/env bash

#This will make portraits en mass

# sh 2Dtemplate.sh pulsar directory

#cd $2

cd $1

paz -r -e paz J*dly ;

paz -E 2 -e J*paz ;

ftu = $(ls*paz | head -1) ; 

std = $(/fred/oz002/users/mmiles/MSP_DR/github_templates/$1.std) ;

rm metafile ;

ls J*paz > metafile ;

~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_constant_portrait.py $std $ftu constant_profile.$1.port ;

pam -Tp -e Tp.port constant_profile.$1.port ;

paz -E 2 -e paz.port constant_profile.$1.Tp.port ;

paz -mr J*paz ;

psradd -T J*paz -o grand.paz ;

~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppalign.py -M metafile -T -I constant_profile.$1.Tp.paz.port -o metafile_average.$1.Tp.port --niter 2 ;

paz -mr metafile_average.$1.Tp.port ;

~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppspline.py -d metafile_average.$1.Tp.port -o 2D.spline.$1.spl -N None -n 10 -s --plots -a 2D.portrait.$1.Tp.paz.port ;

~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppspline.py -d metafile_average.$1.Tp.port -o 2D.spline.$1.spl -N prof -n 10 -s --plots -a 2D.portrait.$1.Tp.paz.norm.port ;

~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_residual_plots.py -m 2D.spline.$1.spl -d metafile_average.$1.Tp.port --nowb -r 0.5 ;

pam -D -e ddisp *norm.port ;

#template_repo = $(/fred/oz002/users/mmiles/MSP_DR/MSP_data/portraits_metafile_trial/) ;

cp 2D*port /fred/oz002/users/mmiles/MSP_DR/MSP_data/portraits_metafile_trial ;

cp 2D*ddisp /fred/oz002/users/mmiles/MSP_DR/MSP_data/portraits_metafile_trial ;

