#!/bin/bash
#SBATCH --cpus-per-task=1
#SBATCH --time=20:00:00
#SBATCH --job-name=pol_data
#SBATCH --mem=5gb
#SBATCH --tmp=5gb

##In order to batch the pulse portraiture codes, this needs to be uncommented
#source activate py2
#module load numpy/1.16.3-python-2.7.14
#module load scipy/1.0.0-python-2.7.14
#module load psrchive/1e36de3a8
#module load matplotlib/2.2.2-python-2.7.14

source activate py37
touch ${1}".pol_data"
#bash ~/soft/timing/residuals.sh $1
python ~/soft/SP/pol_analysis.py
#python ~/soft/timing/template_update.py $1
#python ~/soft/SP/SP_bilby_true_parametized_real.py
rm -f ${1}".pol_data"

#touch "quickmove"
#python ~/soft/SP/SP_strongstate.py

#rm -f "quickmove"

echo done
