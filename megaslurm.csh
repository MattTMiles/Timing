#!/bin/csh

# megaslurm2.csh slurmname.csh directory start end gulpsize

set slurm = $1
set dirname = $2
set base = $PWD

#foreach pulsar (`ls $2 | grep J`)
foreach pulsar (`cat /fred/oz002/users/mmiles/MSP_DR/pulsar_list.txt`)
	sbatch $slurm $pulsar
end

