#!/bin/bash
#SBATCH --cpus-per-task=1
#SBATCH --time=02:00:00
#SBATCH --job-name=templates
#SBATCH --mem=20g
#SBATCH --tmp=20g 


#cd /fred/oz002/users/mmiles/timing/
touch ${1}".TheRest"
#csh combiner.csh $1 $2 $3
#if $1 == J*
#then
python 1Dtemplate.py $1
#fi

rm -f ${1}".TheRest"
echo done
