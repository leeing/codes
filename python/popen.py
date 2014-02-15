#!/usr/bin/python

import subprocess
import os

def external_cmd(cmd, msg_in=''):
    try:
        proc = subprocess.Popen(cmd,
                   shell=True,
                   stdin=subprocess.PIPE,
                   stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE,
                  )
        stdout_value, stderr_value = proc.communicate(msg_in)
        return stdout_value, stderr_value
    except ValueError as err:
        #log("ValueError: %s" % err)
        return None, None
    except IOError as err:
        #log("IOError: %s" % err)
        return None, None

if __name__ == '__main__':
    #stdout_val, stderr_val = external_cmd("./hello.sh")
    exit_status = os.system("./chkaix.ogpy")
    print("the exit_status is : " + str(exit_status))
    #print 'Standard Output: %s' % stdout_val
    #print 'Standard Error: %s' % stderr_val
