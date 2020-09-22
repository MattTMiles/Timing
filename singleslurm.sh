#!/bin/bash
#SBATCH --cpus-per-task=16
#SBATCH --time=48:00:00
#SBATCH --job-name=bilby 
#SBATCH --mem=15gb
#SBATCH --tmp=15gb

##In order to batch the pulse portraiture codes, this needs to be uncommented
#ource activate py2
#module load numpy/1.16.3-python-2.7.14
#module load scipy/1.0.0-python-2.7.14
#module load psrchive/1e36de3a8
#module load matplotlib/2.2.2-python-2.7.14

#touch ${1}".pptoa"
#bash ~/soft/timing/residuals.sh $1
#~/.conda/envs/py2/bin/python ~/soft/timing/2Dtoa.py $1
#python ~/soft/timing/TOA.py $1
#python ~/soft/timing/template_update.py $1
#rm -f ${1}".pptoa"

touch "bilby_triplemodel"
python ~/soft/SP/SP_bilby_true_parametized_real.py

rm -f "bilby_triplemodel"

echo done
