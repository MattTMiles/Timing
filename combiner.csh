#!/bin/csh

#combines single pulses from directory $1 from line $2 to line $3
#eg combiner.csh 2019-XXXX 0 1000
# or combiner.csh 2019-XXX 20000 30000

mkdir /tmp/mbtempo
setenv TMPDIR /tmp/mbtempo
cp -r $TEMPO2 $TMPDIR/tempo2
cp -r $TEMPO2_CLOCK_DIR $TMPDIR/tempo2_clock_dir
setenv TEMPO2 $TMPDIR/tempo2
setenv TEMPO2_CLOCK_DIR $TMPDIR/tempo2_clock_dir

set count=0
set directory=$1
set first=$2
set last=$3
set nfiles = `echo $last $first| awk '{ print $1-$2}'`

echo processing directory $directory from file $first to $last for a total of $nfiles files
cd /fred/oz002/users/mbailes/J0540-6919

#foreach dir ($directory)
  cd $directory
  mkdir -p combined
  set topband=`ls -1 | grep -v combined| head -1`
  set bottomband = `ls -1 | grep -v combined|tail -1`
  echo top band is $topband bottom band is $bottomband
  cd $topband
  foreach pulse (`lfs find . | grep pulse|sort -n| awk -F- '{print $2}'| head -$last| tail -$nfiles`)
#      echo psradd -R ../$bottomband"/pulse_-"$pulse "pulse_-"$pulse " -o ../combined/pulse_"$pulse
    psradd -R ../$bottomband"/pulse_-"$pulse "pulse_-"$pulse -o ../combined/pulse_$pulse
    set count = `echo $count | awk '{ print $1+1}'`
    echo completed $count files
  end
