#!/bin/bash
#SBATCH --cpus-per-task=1
#SBATCH --time=0:10:00
#SBATCH --job-name=templates
#SBATCH --mem=20g
#SBATCH --tmp=20g 


#cd /fred/oz002/users/mmiles/timing/
touch ${1}".TFjob"
#csh combiner.csh $1 $2 $3
#if $1 == J*
#then
python TFprocess.py $1
#fi

rm -f ${1}".TFjob"
echo done
