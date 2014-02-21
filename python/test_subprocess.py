#!/usr/bin/python

# in python 2.4.4, there is no check_call() method
# so I wrote a shell() to replace it.

import subprocess

def shell(cmd):
    command = cmd.split(" ")
    return subprocess.Popen(command,stdout=subprocess.PIPE).communicate()[0]


if __name__ == "__main__":
    result = shell("ls -l")
    print "result is " + result
	
    
