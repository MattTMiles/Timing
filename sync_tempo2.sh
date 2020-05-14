#This script makes tempo faster

export JOBFS=/tmp/mmiles
mkdir -p $JOBFS
rsync -a $TEMPO2/ $JOBFS/tempo2
rsync -a $TEMPO2_CLOCK_DIR/ $JOBFS/tempo2_clock_dir
export TEMPO2=$JOBFS/tempo2
export TEMPO2_CLOCK_DIR=$JOBFS/tempo2_clock_dir
#export TEMPO2_CLOCK_DIR="/fred/oz002/rshannon/tempo2/clock:$TEMPO2_CLOCK_DIR"

