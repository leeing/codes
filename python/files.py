#!/usr/bin/python

import tarfile
import os

def archive_files(file_list,dest_dir):
    for file in file_list:
	tarzipfile = tarfile.open(dest_dir + "/" + file + ".tar.gz","w:gz")
	tarzipfile.add(dest_dir + "/" + file)
	tarzipfile.close()

if __name__ == "__main__":
    files = os.listdir("/tmp/leeing")
    print("files are : " + str(files))
    archive_files(files,"/tmp/leeing")

