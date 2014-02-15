#!/usr/bin/python

import threading
import random
import os
import math
from time import sleep,ctime
import timeit

PACK=8.0

class RoshScript(threading.Thread):
    def __init__(self,sa_name,script):
	threading.Thread.__init__(self,name="["+sa_name+"]["+script+"]")
	self.sa_name= sa_name
	self.script = script

    def run(self):
	wait_time = random.randrange(1,5)
	print("## [ogfs] rosh -l root -n " + self.sa_name + " -s ./" + self.script + ", runnning :" + str(wait_time))
	print("## [ogfs] rosh -l root -n " + self.sa_name + " -s ./" + self.script + ", runnning :" + str(wait_time))
	os.system("sleep " + str(wait_time)
	print(self.getName() + " is finished in " + str(wait_time) + "s")

def dispatch_script(sa_list,script):
    sa_count = len(sa_list)
    turns = int(math.ceil(sa_count/PACK))
    print("turns is :" + str(turns))

    for turn in range(0,turns):
	start = timeit.default_timer()
	threads = []
	for count in range(int(turn*PACK),int((turn+1)*PACK)):
	    if count < sa_count:
		print("count is :" + str(count))
		thread = RoshScript(sa_list[count],script)
		thread.start()
		threads.append(thread)

	for thread in threads:
	    thread.join(5)
	end = timeit.default_timer()
	print("##[INFO] Turn :"+ str(turn+1) + " finished in " + str(end - start) + " s")


def main():
    print("start run rosh scripts")
    threads = []
    sa_list = ['tdauto1','tdauto2','dsapp1','dsapp2','dssapp1','dssapp2','sh.dxdb01','sh.dxdb02','tduat','tdst']
    shanghai_sa_list = [sa for sa in sa_list if sa.startswith("sh.")]

    print("shanghai sa list are :" + str(shanghai_sa_list))
    start = timeit.default_timer()
    dispatch_script(sa_list,"chkaix.py")
    end = timeit.default_timer()
    print("main thread is finished in " + str(end-start) + " s")


if __name__ == "__main__":

    main()
    assert 1==2

	
