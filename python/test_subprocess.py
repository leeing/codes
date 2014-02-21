#!/usr/bin/python

import subprocess

def shell(cmd):
    command = cmd.split(" ")
    return subprocess.Popen(command,stdout=subprocess.PIPE).communicate()[0]


if __name__ == "__main__":
    result = shell("ls -l")
    print "result is " + result
	
    
