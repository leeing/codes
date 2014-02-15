#!/usr/bin/python

import time

if __name__ == "__main__":
    dateformat = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))  
    print("dateformat is " + dateformat)
