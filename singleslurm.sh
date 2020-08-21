#!/bin/bash
#SBATCH --cpus-per-task=1
#SBATCH --time=00:30:00
#SBATCH --job-name=residual_creation
#SBATCH --mem=1g
#SBATCH --tmp=1g 


#cd /fred/oz002/users/mmiles/timing/
#touch ${1}".DMupdate"
#csh combiner.csh $1 $2 $3
#if $1 == J*
#then
#python 1Dtemplate.py $1
#fi

#rm -f ${1}".DMupdate"


source activate py2
module load numpy/1.16.3-python-2.7.14
module load scipy/1.0.0-python-2.7.14
module load psrchive/1e36de3a8


touch ${1}".2DTOA"
bash residuals.sh $1
#~/.conda/envs/py2/bin/python ~/soft/timing/2Dtemplate.py $1
rm -f ${1}".2DTOA"

#touch "bilby_another"
#python ~/soft/SP/SP_bilby_true_parametized_real.py

#rm -f "bilby_another"

echo done
