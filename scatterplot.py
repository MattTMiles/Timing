import csv
import os
import numpy as np 
import astropy
from astropy.table import Table
import matplotlib.pyplot as plt 

MainDir = "/fred/oz002/users/mmiles/templates/"
os.chdir(MainDir)

ActiveDir = "/fred/oz002/users/mmiles/templates/aligned_smoothed"
os.chdir(ActiveDir)

t = Table.read("aligned_compfile", format ='ascii')
old = plt.plot(t["col1"], t["col2"], 'b',label = "old")
new = plt.plot(t["col1"], t["col3"], 'g', label ="new")
plt.ylabel("gof")
plt.legend(handles = [old, new])
plt.show()