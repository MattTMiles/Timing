import os
import glob
import sys
import errno

MainDir = "/fred/oz002/users/mmiles/templates/"
os.chdir(MainDir)
pulsar = sys.argv[1]

pulsar_dir = os.path.join(MainDir,pulsar)
os.chdir(pulsar_dir)

Tf32p_dir = os.path.join(pulsar_dir,"Tf32p")

os.chdir(Tf32p_dir)
os.system("rm high_snr")

high_snr = os.path.join(Tf32p_dir,"high_snr")

try:
    os.system("mkdir "+high_snr)
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    pass

for obs in os.listdir(pulsar_dir):
    if not obs.endswith(".mohsened"):
        if obs.startswith("2"):
            #Change to requested observation directory
            obs_dir = os.path.join(pulsar_dir, obs)
            os.chdir(obs_dir)

            #Move through beam number directory
            beamno = os.listdir(obs_dir)[0]
            beamno_dir = os.path.join(obs_dir, beamno)
            os.chdir(beamno_dir)

            #Move through frequency directory
            freq = os.listdir(beamno_dir)[0]
            freq_dir = os.path.join(beamno_dir, freq)
            os.chdir(freq_dir)

            os.system("pam -F -e TFp *.Tp")

            os.system("mv *.TFp "+pulsar_dir+"/Tf32p")

os.chdir(Tf32p_dir)

eph_dir = "/fred/oz002/users/mmiles/templates/msp_ephemerides"

os.system("pam -mE "+eph_dir+"/"+pulsar+".par --update_dm *TFp")

for data in os.listdir(Tf32p_dir):
    if data.endswith(".TFp"):
        if data.startswith("2"):
            snr = os.popen("psrstat -c snr=pdmp -j FTp -c snr -Q "+data+" | awk '{print $(NF)}'").read().split()
            if float(snr[0]) > 100:
                os.system("cp "+data+" "+high_snr)

os.chdir(high_snr)
os.system("psradd -TPF -o grand_snr.TFp 20*TFp -ip")
os.system("pam -mT grand_snr.TFp")
os.system("psrsmooth -W grand_snr.TFp")
os.system("mv grand_snr.TFp.sm "+pulsar+"_snr.std")
