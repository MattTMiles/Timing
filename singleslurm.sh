#!/bin/bash
#SBATCH --cpus-per-task=1
#SBATCH --time=24:00:00
#SBATCH --job-name=bilby_wide_window
#SBATCH --mem=7gb
#SBATCH --tmp=7gb

##In order to batch the pulse portraiture codes, this needs to be uncommented
#source activate py2
#module load numpy/1.16.3-python-2.7.14
#module load scipy/1.0.0-python-2.7.14
#module load psrchive/1e36de3a8
#module load matplotlib/2.2.2-python-2.7.14

#This is for letting python 3 do its job
#module load psrchive/2fac8db35-python-3.6.4
#source activate py37
#touch ${1}".dataupdate"
touch "bilby_wide"
#bash ~/soft/timing/residuals.sh $1
#python ~/soft/SP/slurm_pol_analysis.py
#python ~/soft/timing/256s_subbands.py
#python ~/soft/timing/template_update.py $1
#python ~/soft/timing/tim_maker.py $1
#python ~/soft/timing/2Dtemplate.py $1
python ~/soft/SP/SP_bilby_wide.py
rm -f "bilby_wide"
#rm -f ${1}".dataupdate"

#touch "quickmove"
#python ~/soft/SP/SP_strongstate.py

#rm -f "quickmove"

echo done
