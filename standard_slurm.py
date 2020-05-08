import os
import sys
#Specify parent directory
MainDir = "/fred/oz002/users/mmiles/templates/"
os.chdir(MainDir)

#Move through pulsar directories
#for pulsar in os.listdir(MainDir):
#    if pulsar.startswith("J"):
pulsar = sys.argv[1]
pulsar_dir = os.path.join(MainDir,pulsar)
os.chdir(pulsar_dir)

Tp_dir = os.path.join(pulsar_dir,"Tp_templates")
#Specify the directories for the different possible bandwidths
dir_856 = os.path.join(Tp_dir,"856")
dir_775 = os.path.join(Tp_dir,"775")
dir_642 = os.path.join(Tp_dir,"642")

#Search and change into the relevant bandwidth directories
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
