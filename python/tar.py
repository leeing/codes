#!/usr/bin/python

import tarfile
import glob
import commands
import os

if __name__ == "__main__":
     files = glob.glob("""/tmp/*.log""")
     archive_file = """/tmp/""" + commands.getoutput("date +%Y%m%d%H%M%S") + "_sample.tar"
     tar_file = tarfile.open(archive_file,"w|")
     for file in files:
	os.chdir(os.path.dirname(file))
	tar_file.add(os.path.basename(file))
     tar_file.close()


    
