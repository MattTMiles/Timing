#!/bin/csh

# megaslurm2.csh slurmname.csh directory start end gulpsize

set slurm = $1
set dirname = $2
#set pulsar = $3
#set theend = $4
#set ngulp = $5
set base = $PWD

#foreach pulsar (`ls $2 | grep J`)
foreach pulsar (`cat toa.list`)
	sbatch $slurm $pulsar
end

#foreach pulsar (J0955-6150 J1757-1854)
#	sbatch $slurm $pulsar
#end

#foreach pulsar (J1754+0032)
#	sbatch $slurm $pulsar
#end

#Megaslurm has been altered to work for each observation in J0437 in the code below, originial code is in lines above
#foreach obs (2019-10-13-05:37:42 2019-12-26-16:04:49 2019-12-26-20:05:04 2019-12-27-00:05:16 2019-12-27-00:05:16 2019-12-27-00:05:16 2019-12-27-23:56:16 2019-12-28-14:52:22 2019-12-28-18:52:37 2019-12-28-22:52:51 2019-12-29-15:39:36 2019-12-29-19:39:50 2019-12-29-23:40:03 2019-12-30-15:25:03 2019-12-30-19:25:16 2019-12-30-23:25:30 2019-12-31-15:02:05 2019-12-31-19:02:19 2019-12-31-23:02:33) 
#    sbatch $slurm $obs
#end

