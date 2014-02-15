#!/usr/bin/python

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", help="write report to FILE", metavar="LEE_FILE")
parser.add_option("-q", "--quiet", action="store_false", dest="verbose", default=True,help="don't print status messages to stdout")
parser.add_option("-m", "--hmc_list", action="append", dest="hmc_list", help="specify the HMC(s) to check",default=[])

(options,args) = parser.parse_args()

print(type(options))
print(type(args))
print(len(args))


print(options.hmc_list)
