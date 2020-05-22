import os
import sys

pulsars = sys.argv[1]
template_dir = "/fred/oz002/users/mmiles/templates"
os.chdir(template_dir)
#for pulsars in template_dir:
if pulsars.startswith("J"):
        pulsar_dir = os.path.join(template_dir,pulsars)
        os.chdir(pulsar_dir)
        wd = os.path.join(pulsar_dir,"Tf32p")
        os.chdir(wd)

        #Actually makes the standard
        os.system("psradd -TPF -o grand2.TFp 20*TFp -ip ; pam -mT grand2.TFp ; psrsmooth -W grand2.TFp")
        #Renames the standard
        os.system("mv grand2.TFp.sm "+pulsars+"_2.std")
        os.system("cp "+pulsars+"_2.std ../../best/standards_2/")