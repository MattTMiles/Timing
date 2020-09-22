import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import os

maindir = "/fred/oz002/users/mmiles/templates/2D_Templates"
os.chdir(maindir)


all_1d = np.loadtxt("all_pulsars_1D.tim")
all_2d = np.loadtxt("all_pulsars_2D.tim")
ave_1d = np.loadtxt("ave_pulsars_1D.tim")
ave_2d = np.loadtxt("ave_pulsars_2D.tim")

#all plots
plt.hist(all_1d, bins=500, label = "Standard timing")
plt.hist(all_2d, alpha=0.7, bins=500, label = "Portrait timing")
plt.legend()
plt.title("Comparison of all timing errors for 184 pulsars")
plt.xlabel("Timing error")
plt.ylabel("# of TOA's")
plt.figure()

#ave plots
plt.hist(ave_1d, bins = 500, label = "Standard timing")
plt.hist(ave_2d, alpha=0.7, bins=500, label = "Portrait timing")
plt.legend()
plt.title("Comparison of the average timing error for 184 pulsars")
plt.xlabel("Average timing error")
plt.xlim(0,1000)
plt.ylabel("# of pulsars")
plt.figure()


#all plots - log scale
plt.hist(all_1d, bins=500, log = True, label = "Standard timing")
plt.hist(all_2d, bins=500, alpha=0.7, log = True, label = "Portrait timing")
plt.legend()
plt.title("Comparison of all timing errors for 184 pulsars")
plt.xlabel("Timing error")
plt.ylabel("# of TOA's")
plt.figure()


#ave plots - log scale
plt.hist(ave_1d, bins = 500, log = True, label = "Standard timing")
plt.hist(ave_2d, bins=500, alpha=0.7, log = True, label = "Portrait timing")
plt.legend()
plt.title("Comparison of the average timing error for 184 pulsars")
plt.xlabel("Average timing error")
plt.ylabel("# of pulsars")
plt.xlim(0,1000)
plt.show()