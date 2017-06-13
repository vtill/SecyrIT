#!/usr/bin/python
import thread
import subprocess

print("hi")
#subprocess.check_output(["gvim"])
blah=subprocess.call(["gvimmuell"])

#for x in range(1000000):
#	print x	
print blah
