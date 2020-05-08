#!/usr/bin/env bash

# template_maker #
##################

#template_maker is for making 1D & 2D templates for a pulsar

#Written by Mohsen Shamohammadi (msh.ph.ir@gmail.com).

#Example: bash template_maker.sh <file.ar>
#You need to do RFI excision before making any template



### choose the best filed as inputs:
#RF_1=${1?Error: no file is given}
#RF_2=${2?Error: no file is given}
#RF_3=${3?Error: no file is given}

#Naming the output files
C_FREQ=$(psrstat -c freq -Qq $1 | awk '{print $1}') ;
NAME=$(psrstat -c name -Qq $1 | awk '{print $1}') ;

#Self-standardising method: use the files to make the pulse profile (using .ar), better to clean this first.

## making 1D template(pulse profile):
#pam=pulse archive modifier
pam -FTp -e FTp *.mohsen

psradd *.FTp -o 1D.$NAME.$C_FREQ ;
echo "psradd is done" ;
pam -T -m 1D.$NAME.$C_FREQ ;
psrsmooth -W -e std 1D.$NAME.$C_FREQ ;
echo "1D template is made"
rm *FTp


### making 1D temp using autotoa:
#paz -r -E 5 -e dzT.paz *.dzT
#ls *paz > metafile.autotoa ;
#/home/mshamoha/codes/psrtools/./autotoa -M metafile.autotoa -g 0.1 -S 1D.$NAME.$C_FREQ ;
#pam -m -p 1D.$NAME.$C_FREQ
#psrsmooth -W -e std 1D.$NAME.$C_FREQ ;


### making 2D template:
paz -E 1 -e paz *mohsen
ls *paz > metafile

#Uses the first .ar file to create the structure of the constant profile (defines bounds)
~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_constant_portrait.py 1D.$NAME.$C_FREQ.std $1 constant_profile.$NAME.$C_FREQ.port ;
pam -Tp -e Tp.port constant_profile.$NAME.$C_FREQ.port ;
paz -E 1 -e paz.port constant_profile.$NAME.$C_FREQ.Tp.port ;
#Creates constant profile
~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppalign.py -M metafile -T -I constant_profile.$NAME.$C_FREQ.Tp.paz.port -o metafile_average.$NAME.$C_FREQ.Tp.port --niter 2 ;
#Creates the average metadata model
~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppspline.py -d metafile_average.$NAME.$C_FREQ.Tp.port -o 2D.spline.$NAME.$C_FREQ.spl -N prof -n 3 -s --plots -a 2D.portrait.$NAME.$C_FREQ.Tp.paz.port ;

### making difference plot:
~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_residual_plots.py -m 2D.spline.$NAME.$C_FREQ.spl -d constant_profile.$NAME.$C_FREQ.Tp.paz.port --nowb -r 0.5 --showplot ;

