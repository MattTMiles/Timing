import os
import sys

#This makes a 2D template of the file

MainDir = "/fred/oz002/users/mmiles/templates/"
os.chdir(MainDir)

pulsar = sys.argv[1]

#for pulsar in os.listdir(MainDir):
if pulsar.startswith("J"):
    pulsar_dir = os.path.join(MainDir, pulsar)
    os.chdir(pulsar_dir)

    for obs in os.listdir(pulsar_dir):
        if obs.startswith("2"):
            if not obs.endswith("mohsened"):
                print(obs)
                obs_dir = os.path.join(pulsar_dir,obs)
                os.chdir(obs_dir)
                beam = os.listdir(obs_dir)[0]
                beam_dir = os.path.join(obs_dir,beam)
                os.chdir(beam_dir)
                freq = os.listdir(beam_dir)[0]
                freq_dir = os.path.join(beam_dir,freq)
                os.chdir(freq_dir)
                
                #Now in the directory containing the .mohsen files
                #paz all of these and then put them together into a metafile for each obs
                os.system("paz -E 1 -e paz *mohsen")
                os.system("ls *paz > metafile")

                #Specify the file to use (ftu) just as the first .mohsen file
                ftu = os.popen("ls *mohsen | head -1").read().strip("\n")
                #From this, create a constant profile
                os.system("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_constant_portrait.py /fred/oz002/users/mmiles/templates/Wsmoothed/1D."+pulsar+"*.sm "+ftu+" constant_profile."+obs+".port")
                os.system("pam -Tp -e Tp.port constant_profile."+obs+".port")
                os.system("paz -E 1 -e paz.port constant_profile."+obs+".Tp.port") 

                #Creates constant profile
                ##have to put the pythonpath in here because for some reason it's defaulting to the skylake one##
                os.system("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppalign.py -M metafile -T -I constant_profile."+obs+".Tp.paz.port -o metafile_average."+obs+".Tp.port --niter 2")

                #Creates the average metadata model/2D model
                os.system("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/ppspline.py -d metafile_average."+obs+".Tp.port -o 2D.spline."+obs+".spl -N prof -n 3 -s --plots -a 2D.portrait."+obs+".Tp.paz.port")

                ### making difference plot:
                #os.system("~/.conda/envs/py2/bin/python /home/mmiles/soft/timing/make_residual_plots.py -m 2D.spline."+obs+".spl -d constant_profile."+obs+".Tp.paz.port --nowb -r 0.5")
                



