#!/bin/bash
#SBATCH --cpus-per-task=1
#SBATCH --time=01:00:00
#SBATCH --job-name=highsnr_portraits
#SBATCH --mem=20gb
#SBATCH --tmp=20gb


##In order to batch the pulse portraiture codes, this needs to be uncommented

#source activate py2
#module load numpy/1.16.3-python-2.7.14
#module load scipy/1.0.0-python-2.7.14
#module load psrchive/1e36de3a8
#module load tempo2/0759584
#module load matplotlib/2.2.2-python-2.7.14

#This is for letting python 3 do its job
#module load psrchive/2fac8db35-python-3.6.4
#source activate py37

#cd /fred/oz002/users/mmiles/SinglePulse
#cd /fred/oz002/users/mmiles/MSP_DR/subband_comps/highsnr_psradd_check
touch ${1}".highsnr_portraits"
#touch "comp"
#bash ~/soft/timing/residuals.sh $1
#srun python /home/mmiles/soft/SP/alldata_unsmoothed_weakStrongTemplatePython_TMtoa_Uniform.py $1
#srun python /home/mmiles/soft/SP/SP_t2sim.py -par /fred/oz002/users/mmiles/SinglePulse/Jitter_check/bilby_runs/J1909-3744.par -tim $1 -avgpar /fred/oz002/users/mmiles/SinglePulse/Jitter_check/bilby_runs/J1909-3744_avg.par -output .
#python ~/soft/timing/256s_subbands.py
#python ~/soft/timing/template_update.py $1
#python ~/soft/timing/tim_maker.py $1
python ~/soft/timing/2Dtemplate.py $1
#python ~/soft/timing/pp_temp_comparison.py $1
#srun python ~/soft/SP/SP_Positive_Pulses.py
#sh ~/soft/timing/2Dtemplate.sh $1
#cd $1
#pam -p -e p J*.ar
#/fred/oz005/users/mkeith/dlyfix/dlyfix -e dly J*.p
#pam -mE /fred/oz002/users/mmiles/MSP_DR/github_ephs/$1.par --update_dm J*dly
#cd archs
#srun python ~/soft/timing/subband_check.py -portrait *ddisp_16ch -archive grand.dly -ephemeris *par -subbands 8 -save
#rm -f "rerunpol"
#cd /fred/oz002/users/mmiles/MSP_DR/subband_comps/metafile_check/
#cd /fred/oz002/users/mmiles/MSP_DR/subband_comps
#cd ..
rm -f ${1}".highsnr_portraits"

#cd /fred/oz002/users/mmiles/SinglePulse/1070
#dspsr /fred/oz002/baseband/meerkat/J1909-3744/2020-02-13-03:05:04/1070/*dada -s -K -cuda 0 -E /fred/oz002/users/mmiles/SinglePulse/J1909_old.par -b 2048 -no_dyn -d 4 -x 1024
#mv pulse_128763500835.ar pulse_128763500836.ar pulse_128763500837.ar pulse_128763500838.ar ../bad1070

#cd /fred/oz002/users/mmiles/SinglePulse/1498
#dspsr /fred/oz002/baseband/meerkat/J1909-3744/2020-02-13-03:05:04/1498/*dada -s -K -cuda 0 -E /fred/oz002/users/mmiles/SinglePulse/J1909_old.par -b 2048 -no_dyn -d 4 -x 1024
#mv pulse_128763500835.ar pulse_128763500836.ar pulse_128763500837.ar pulse_128763500838.ar ../bad1498

#cd /fred/oz002/users/mmiles/SinglePulse/
#for f in `ls 1498`; do pam -e dd --DD 1070/$f; done

#for f in `ls 1498`; do pam -e dd --DD 1498/$f; done

#for f in `find 1498/*dd -type f -printf "%f\n"`; do psradd -R -o 1284/${f%%.*}.dd 1070/${f%%.*}.dd 1498/${f%%.*}.dd; done

#for f in `find 1284/*dd -type f -printf "%f\n"`; do
#    if [ ! -f ${f%%.*}.hand ]; then
#        psredit -c rcvr:hand=-1 -e hand 1284/${f%%.*}.dd
#    fi
#done
#for f in `find 1284/*hand -type f -printf "%f\n"`; do
#    if [ ! -f ${f%%.*}.jonesP ]; then
#        pac -Q /fred/oz002/users/mmiles/SinglePulse/*jones 1284/${f%%.*}.hand -e jones;
#    fi
#done

#for f in `find 1284/*jonesP -type f -printf "%f\n"`; do paz -r 1284/${f%%.*}.jonesP -e zz; done

#for f in `find 1284/*zz -type f -printf "%f\n"`; do psredit -c dm=10.3917340199024 1284/${f%%.*}.zz -e dm; done

#for f in `find 1284/*dm -type f -printf "%f\n"`; do
#    if [ ! -f ${f%%.*}.f32 ]; then
#        pam -f 32 1284/${f%%.*}.dm -e f32;
#    fi
#done

#for f in `find 1284/*f32 -type f -printf "%f\n"`; do pam -p 1284/${f%%.*}.f32 -e f32p; done

#for f in `find 1284/*f32 -type f -printf "%f\n"`; do pam -S 1284/${f%%.*}.f32 -e stokes; done

#for f in `find 1284/*stokes -type f -printf "%f\n"`; do ln -s /fred/oz002/users/mmiles/SinglePulse/1284/${f%%.*}.stokes /fred/oz002/users/mmiles/SinglePulse/1284_f32_stokes/${f%%.*}.stokes ; done

#touch "quickmove"
#python ~/soft/SP/SP_strongstate.py

#rm -f "quickmove"

echo done
