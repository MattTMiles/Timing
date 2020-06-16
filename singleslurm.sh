#!/bin/bash
#SBATCH --cpus-per-task=1
#SBATCH --time=04:00:00
#SBATCH --job-name=SinglePulses
#SBATCH --mem=20g
#SBATCH --tmp=20g 


#cd /fred/oz002/users/mmiles/timing/
#touch ${1}".DMupdate"
#csh combiner.csh $1 $2 $3
#if $1 == J*
#then
#python 1Dtemplate.py $1
#fi

#rm -f ${1}".DMupdate"

touch "singlepulse.collector"
~/.conda/envs/py37/bin/python3.7 ~/soft/SP/SP_timephase.py
rm -f "singlepulse.collector"
echo done
