import os
import glob
import sys
import errno

#Let a user input a pulsar and observation to do this script indivdually


MainDir = "/fred/oz002/users/mmiles/templates/"
os.chdir(MainDir)

#    pulsar = input("Input the pulsar to be investigated:")
#    obs = input("Input the observation to be investigated:")
pulsar = sys.argv[1]

#for pulsar in os.listdir(MainDir):
#    if pulsar.startswith("J"):
        
#Change to requested pulsar directory
pulsar_dir = os.path.join(MainDir,pulsar)
os.chdir(pulsar_dir)

#Entrance gate so the the terminal will check if one is already running/has run on this pulsar
#if not os.path.isfile("started"):
#Creating reference file to keep track of what's been done, kept in the main directory
#os.system("echo "+pulsar+" >> "+MainDir+"/1D_donefile")

#Create file warning other terminals that pulsar has been started
#os.system("echo started > started")
for obs in os.listdir(pulsar_dir):
    if not obs.endswith(".mohsened"):
        #if not os.path.isfile(obs+".mohsened"):
        if obs.startswith("2"):
            #Change to requested observation directory
            obs_dir = os.path.join(pulsar_dir, obs)

            #Move through beam number directory
            beamno = os.listdir(obs_dir)[0]
            beamno_dir = os.path.join(obs_dir, beamno)
            os.chdir(beamno_dir)

            #Move through frequency directory
            freq = os.listdir(beamno_dir)[0]
            freq_dir = os.path.join(beamno_dir, freq)
            os.chdir(freq_dir)

            #This p,F, and T scrunches the data
            os.system("pam -Tp -e mohsenTp *.mohsen")
            
            #This adds it into a single archive.
            os.system("psradd *.mohsenTp -o 1D_"+obs+".Tp")

            #T scrunches the data again
            #os.system("pam -T -m *.Tp")
            #This moves the added file up to the pulsar directory
            os.system("mv 1D_"+obs+".Tp "+pulsar_dir)
            os.chdir(pulsar_dir)

#separate.py script - for separating the observations into their bandwidths   
Tp_dir = os.path.join(pulsar_dir,"Tp_templates")
try:
    os.mkdir(Tp_dir)
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    pass
os.chdir(Tp_dir)
try:
    os.mkdir(os.path.join(Tp_dir,"775"))
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    pass
dir_775 = os.path.join(Tp_dir,"775")

try:
    os.mkdir(os.path.join(Tp_dir,"856"))
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    pass
dir_856 = os.path.join(Tp_dir,"856")
dir_642 = os.path.join(Tp_dir,"642") 

os.chdir(pulsar_dir)
for template in os.listdir(pulsar_dir):
    if template.startswith("1D_"):
        bw = os.popen("psrstat -c bw "+template+" | awk '{print $(NF)}'").read().strip("bw=").strip("\n")
        if bw == "856":
            os.system("mv "+template+" "+dir_856)
        elif bw == "775.75":
            os.system("mv "+template+" "+dir_775)
        else:
            print("weird obs:", os.getcwd())
            print("different bandwidth:", bw)
            try:
                os.mkdir(os.path.join(Tp_dir, bw))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
                pass
            os.system("mv "+template+" "+os.path.join(Tp_dir, bw))

#snr_mover.py script - for identifying high signal to noise cases   
if os.path.isdir(dir_856):
    os.chdir(dir_856)
    try:
        os.mkdir(os.path.join(dir_856,"high_snr"))
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass
    #os.system("rm 1D*")
    os.chdir(dir_856)
    for ints in os.listdir(dir_856):
        if ints.startswith("1D"):
            snr = os.popen("psrstat -c snr=pdmp -j FTp -c snr -Q "+ints+" | awk '{print $(NF)}'").read().split()
            if float(snr[0]) > 40:
                os.system("cp ./"+ints+" ./high_snr/")

if os.path.isdir(dir_775):
    os.chdir(dir_775)
    try:
        os.mkdir(os.path.join(dir_775,"high_snr"))
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass
    #os.system("rm 1D*")
    os.chdir(dir_775)
    for ints in os.listdir(dir_775):
        if ints.startswith("1D"):
            snr = os.popen("psrstat -c snr=pdmp -j FTp -c snr -Q "+ints+" | awk '{print $(NF)}'").read().split()
            if float(snr[0]) > 40:
                os.system("cp ./"+ints+" ./high_snr/")

if os.path.isdir(dir_642):
    os.chdir(dir_642)
    try:
        os.mkdir(os.path.join(dir_642,"high_snr"))
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass
    #os.system("rm 1D*")
    os.chdir(dir_642)
    for ints in os.listdir(dir_642):
        if ints.startswith("1D"):
            snr = os.popen("psrstat -c snr=pdmp -j FTp -c snr -Q "+ints+" | awk '{print $(NF)}'").read().split()
            if float(snr[0]) > 40:
                os.system("cp ./"+ints+" ./high_snr/")

#Standard_slurm script - for creating the standard profiles
if os.path.isdir(dir_856):
    os.chdir(dir_856)
    os.system("pam -E /fred/oz005/users/aparthas/reprocessing_MK/PTA/pta_ephemerides/"+pulsar+".par -m 1D*")
    os.system("pam -T -m 1D*")
    os.system("psradd -P 1D* -o "+pulsar+".856.Tp")
    os.system("pam -T -m "+pulsar+".856.Tp")
    os.system("mv "+pulsar+".856.Tp "+pulsar_dir)
    os.chdir(os.path.join(dir_856, "high_snr"))
    os.system("pam -E /fred/oz005/users/aparthas/reprocessing_MK/PTA/pta_ephemerides/"+pulsar+".par -m 1D*")
    os.system("pam -T -m 1D*")
    os.system("psradd -P 1D* -o "+pulsar+".856_highsnr.Tp")
    os.system("pam -T -m "+pulsar+".856_highsnr.Tp")
    os.system("mv "+pulsar+".856_highsnr.Tp "+pulsar_dir)
    os.chdir(pulsar_dir)
    os.system("psrsmooth -W "+pulsar+".856_highsnr.Tp")
    os.system("psrsmooth -W "+pulsar+".856.Tp")

if os.path.isdir(dir_775):
    os.chdir(dir_775)
    os.system("pam -E /fred/oz005/users/aparthas/reprocessing_MK/PTA/pta_ephemerides/"+pulsar+".par -m 1D*")
    os.system("pam -T -m 1D*")
    os.system("psradd -P 1D* -o "+pulsar+".775.Tp")
    os.system("pam -T -m "+pulsar+".775.Tp")
    os.system("mv "+pulsar+".775.Tp "+pulsar_dir)
    os.chdir(os.path.join(dir_775, "high_snr"))
    os.system("pam -E /fred/oz005/users/aparthas/reprocessing_MK/PTA/pta_ephemerides/"+pulsar+".par -m 1D*")
    os.system("pam -T -m 1D*")
    os.system("psradd -P 1D* -o "+pulsar+".775_highsnr.Tp")
    os.system("pam -T -m "+pulsar+".775_highsnr.Tp")
    os.system("mv "+pulsar+".775_highsnr.Tp "+pulsar_dir)
    os.chdir(pulsar_dir)
    os.system("psrsmooth -W "+pulsar+".775_highsnr.Tp")
    os.system("psrsmooth -W "+pulsar+".775.Tp")

if os.path.isdir(dir_642):
    os.chdir(dir_642)
    os.system("pam -E /fred/oz005/users/aparthas/reprocessing_MK/PTA/pta_ephemerides/"+pulsar+".par -m 1D*")
    os.system("pam -T -m 1D*")
    os.system("psradd -P 1D* -o "+pulsar+".642.Tp")
    os.system("pam -T -m "+pulsar+".642.Tp")
    os.system("mv "+pulsar+".642.Tp "+pulsar_dir)
    os.chdir(os.path.join(dir_642, "high_snr"))
    os.system("pam -E /fred/oz005/users/aparthas/reprocessing_MK/PTA/pta_ephemerides/"+pulsar+".par -m 1D*")
    os.system("pam -T -m 1D*")
    os.system("psradd -P 1D* -o "+pulsar+".642_highsnr.Tp")
    os.system("pam -T -m "+pulsar+".642_highsnr.Tp")
    os.system("mv "+pulsar+".642_highsnr.Tp "+pulsar_dir)
    os.chdir(pulsar_dir)
    os.system("psrsmooth -W "+pulsar+".642_highsnr.Tp")
    os.system("psrsmooth -W "+pulsar+".642.Tp")


"""
#This creates an overall pulsar profile from the obs that are moved to the pulsar_dir
os.chdir(pulsar_dir)
#os.system("pam -T -m 1D*")
print("Mark 1: Got here")
os.system("psradd 1D* -o 1D."+pulsar)
os.system("pam -T -m 1D."+pulsar)

#This creates a comparison file to see the improvement from previous standard profiles
#Sets up a standard test file for comparison between the new and old standards
testfile = os.popen("ls /fred/oz002/users/mmiles/timing/"+pulsar+"/*.T | head -1").read()
testfile = testfile.strip("\n")
os.system("pam -F -e TF "+str(testfile))
testfile = str(testfile)+"F"
#Retrieve the goodness-of-fit from the old standard
old_gof = os.popen("pat -A FDM -f 'tempo2 IPTA' -C 'gof' -s /fred/oz005/timing_processed/meertime_templates/"+pulsar+".std "+str(testfile)+" | awk '{print $(NF)}'").read()
old_gof = old_gof.strip("1\n")

#Retrieve the goodness-of-fit from the new standard
new_gof = os.popen("pat -A FDM -f 'tempo2 IPTA' -C 'gof' -s /fred/oz002/users/mmiles/templates/"+pulsar+"/1D."+pulsar+" "+str(testfile)+" | awk '{print $(NF)}'").read()
new_gof = new_gof.strip("1\n")
#Writes the output to the comparison file
os.system("echo "+pulsar+" "+str(old_gof)+" "+str(new_gof)+" >> "+MainDir+"/compfile")
"""