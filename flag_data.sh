#!/bin/sh

timhead=rms11

timname=${timhead}.tim



# 1K mode, PTM not applied by PTUSE [PTM value -24.629 us]
awk  '{if ($3 > 58526.21089) print $0, "-MJD_58526.21089_1K -1"; else print $0 }' $timname > tmp.tim

# 1K mode PTM applied by PTUSE [PTM value -24.630]
awk '{if ($3 > 58550.14921) print $0, "-MJD_58550.14921_1K -1"; else print $0 }' tmp.tim > tmp2.tim
mv tmp2.tim tmp.tim

# 1K mode, AJ added 1 sample [1.196 us] delay to PTUSE
awk  '{if ($3 > 58550.14921) print $0, "-MJD_58550.14921B_1K -1"; else print $0 }' tmp.tim > tmp2.tim 
mv tmp2.tim tmp.tim

# 1K mode, PTM sensor changed from -24 to -19 us [5.051 us]
awk '{if ($3> 58557.14847) print $0, "-MJD_58557.14847_1K -1"; else print $0 }' tmp.tim > tmp2.tim 
mv tmp2.tim tmp.tim

# 1K mode, AJ changed from 1 sample delay, to 0.5 sample delay in PTUSE
awk '{if ($3 > 58575.95951) print $0, "-MJD_58575.9591_1K -1"; else print $0}' tmp.tim > tmp2.tim
mv tmp2.tim tmp.tim


#  306 microsec offset in CBF
awk '{if (($3 > 58550) && ($3 < 58690)) print $0, "-MJD_58550_58690_1K -1"; else print $0}' tmp.tim > tmp2.tim
mv tmp2.tim tmp.tim

mv tmp.tim ${timhead}_flag.tim 	
