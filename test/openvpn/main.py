#!/usr/bin/python

import re
import time
import subprocess

out=subprocess.check_output(["cat","/sys/class/net/eth0/address"])
print out
print "hi"

