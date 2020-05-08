#!/bin/bash
#SBATCH --cpus-per-task=1
#SBATCH --time=12:00:00
#SBATCH --job-name=single.pulses
#SBATCH --mem=20g
#SBATCH --tmp=20g

#This should run observations for J0437 as batch files
#cd /fred/oz002/users/mmiles/timing/
touch ${1}".job"
#csh combiner.csh $1 $2 $3
#if $1 == J*
#then
python batchobs.py $1
#fi

rm -f ${1}".job"
echo done
