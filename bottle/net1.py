#!/usr/bin/python

import pwd
import os
import re
import glob
import time

PROC_TCP = "/proc/net/nf_conntrack"

def _load():
    ''' Read the table of tcp connections & remove header  '''
    with open(PROC_TCP,'r') as f:
        #content = f.readlines()
        #content.pop(0)
        content = f.read()
    return content

a=0
while a<1:
	print (time.ctime())
	print (_load())
	time.sleep(0.5)
	a+=1
