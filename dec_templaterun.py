import os
import glob
import sys
import errno
import itertools
import subprocess as sproc 

MainDir = "/fred/oz002/users/mmiles/templates/"
os.chdir(MainDir)

pulsar = sys.argv[1]
pulsar_dir = os.path.join(MainDir,pulsar)
os.chdir(pulsar_dir)

#Want to use the TpF files in the timing directory to make the profiles
#Isolate the the TpF files in this, then select the files that have the first 10 characters
#Add these files together and move them to a directory created for this 

try:
    os.mkdir("Dec_run")
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    pass

Dec_dir = os.path.join(pulsar_dir,"Dec_run")
filedir = os.path.join(pulsar_dir,"timing")

os.chdir(filedir)

#Add the rm in so it doesn't double up the list
os.system("rm Tpf128.list")
#Create a list with all the TpF file sin it
os.system("find -name '*Tpf128' >> Tpf128.list")
Tplist = open("Tpf128.list","r")
archlist = Tplist.readlines()
archlist = [s.strip('\n') for s in archlist]
archlist = [s.strip('./') for s in archlist]

dictionary = {}
for x in archlist: 
    group = dictionary.get(x[:10],[]) 
    group.append(x) 
    dictionary[x[:10]] = group

for key in dictionary.keys(): 
    active = dictionary[key] 
    stractive = str(active) 
    stractvie = stractive.replace(',','') 
    stractive = stractive.replace("'","") 
    stractive = stractive[1:-1] 
    stractive = stractive.replace(",","") 
    os.system('psradd -TPF -o '+key+'.added '+stractive) 

os.system('mv *added '+Dec_dir)

os.chdir(Dec_dir)

#Now that all the data is in the correct directories we need to 
#implement the correct ephemeris

eph = "/fred/oz002/users/mmiles/templates/msp_ephemerides/"+pulsar+".par"

p = sproc.Popen("pam -mE "+eph+" --update_dm *added", shell=True)
p.wait()
'''
#Add them together and transition them into the standard profile
p = sproc.Popen('psradd -TPF -o grand.added 2*added', shell=True)
p.wait()

p = sproc.Popen('pam -mT grand.added', shell=True)
p.wait()

p = sproc.Popen('psrsmooth -W grand.added', shell=True)
p.wait()

p = sproc.Popen("mv *sm "+pulsar+".std_dec", shell=True)
p.wait()

p = sproc.Popen("psradd -TPF -o grand.added_50snr `psrstat -c snr=pdmp -c snr -Q 2*added | awk '$2>50' | awk '{print $(1)}'`",shell=True)
p.wait()

p = sproc.Popen("psradd -TPF -o grand.added_100snr `psrstat -c snr=pdmp -c snr -Q 2*added | awk '$2>100' | awk '{print $(1)}'`",shell=True)
p.wait()

p = sproc.Popen("psradd -TPF -o grand.added_150snr `psrstat -c snr=pdmp -c snr -Q 2*added | awk '$2>150' | awk '{print $(1)}'`",shell=True)
p.wait()

p = sproc.Popen('psrsmooth -W grand*snr', shell=True)
p.wait()

try:
    p = sproc.Popen('mv *50snr.sm '+pulsar+'.std_dec_50snr', shell=True)
    p.wait()
except:
    pass
try:
    p = sproc.Popen('mv *100snr.sm '+pulsar+'.std_dec_100snr', shell=True)
    p.wait()
except:
    pass

try:
    p = sproc.Popen('mv *150snr.sm '+pulsar+'.std_dec_150snr', shell=True)
    p.wait()
except:
    pass
'''