#!/usr/bin/python

import re
import time


def load(file):
    ''' Read the table of tcp connections & remove header  '''
    with open(file,'r') as f:
        #content = f.readlines()
        #content.pop(0)
        content = f.read()
    return content

def getLines(str):
	list=str.split("\n")
	return list

def makeTable(rows,pattern):
	table=[]
	for r in rows:
		row=re.split(pattern,r)
		table.append(row)	
	return table

def run():
	file = "/proc/net/nf_conntrack"
	stdout=load(file)
	rows=getLines(stdout)
	table=makeTable(rows,r"\s*")
	print table
	print time.ctime()

run()
