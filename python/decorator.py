#!/usr/bin/python

import time

def timeit(func):
    def wrapper():
        start = time.clock()
        func()
        end = time.clock()
        print("used :" + str(end - start) + "seconds")
    return wrapper

@timeit
def foo():
    print "in foo()"

if __name__ == "__main__":
    foo()
    print("it's a sample file")
