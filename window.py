""" This code will go into the files that have been cleaned and decimated and make 
relevant plots to them"""


import os

#Define a main directory for reference
mainDir = "/fred/oz002/users/mmiles/timing"

#Retrieve the pulsar name
#pulsar = input("Input the pulsar you want to make plots for:")
for pulsar in os.listdir(mainDir):
	#Change into the pulsar's directory
	if pulsar.startswith("J"):
		os.chdir(os.path.join(mainDir, pulsar))

		#Run through the observations and create png files where relevant
		for obs in os.listdir(os.path.join(mainDir, pulsar)):

			if obs.endswith(".F"):
				os.system("pav -Yd "+obs+" -g "+obs+".png/png")
  				
			#Run through the data that has been time-scrunched and create a flux plot (D) and a greyscale plot (G)
			if obs.endswith(".T"):
				os.system("pav -DF "+obs+" -g "+obs+".D.png/png")
        
				os.system("pav -Gd "+obs+" -g "+obs+".G.png/png")
