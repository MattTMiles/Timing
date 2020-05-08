#!/bin/bash
#
#SBATCH --cpus-per-task=1
#SBATCH --time=1:00:00
#SBATCH --job-name=templates
#SBATCH --mem=20g
#SBATCH --tmp=20g 

# The point of this is to create a quick slurm command that can send off
#a single file to the supercomputer on activation. 

# This is distinct from singleslurm.sh due to singleslurm.sh being tied
#into megaslurm.csh for convenience

#Below is an example of what to type into the command line to activate
# sbatch quickslurm.sh J0437-4715

#Creates artefact that only exists while job is running/remains if job 
#times out or crashes
touch ${1}".job"

#Put the script below, i.e: python standard_slurm.py $1 where $1 is
#the argument
python standard_slurm.py $1

rm -f ${1}".job"
echo done