#!/usr/bin/env python

import sys
import psrchive as pr
#from pplib import *

#profile = DataPortrait(sys.argv[-3]).prof
arch = pr.Archive_load(sys.argv[-3])
arch.pscrunch()
profile = arch.get_data()[0,0,0]
arch = pr.Archive_load(sys.argv[-2])
outfile = sys.argv[-1]

arch.dededisperse()
arch.set_dispersion_measure(0.0)
for subint in arch:
    for ipol in xrange(arch.get_npol()):
        for ichan in xrange(arch.get_nchan()):
            subint.set_weight(ichan, 1.0)
            arch_prof = subint.get_Profile(ipol, ichan)
            arch_prof.get_amps()[:] = profile

arch.unload(outfile)
