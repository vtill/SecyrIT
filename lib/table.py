import re
from subprocess import check_output

def load(file):
    ''' Read the table of tcp connections & remove header  '''
    with open(file,'r') as f:
        #content = f.readlines()
        #content.pop(0)
        content = f.read()
    return content

#def re():
#	arg=['conntrackd','-i']
#	output=check_output(arg)
#	return output

def getLines(str):
	list=str.split("\n")
	return list

def makeTable(rows,pattern):
	table=[]
	for r in rows:
		row=re.split(pattern,r)
		print len(row) #debug
		table.append(row)	
	return table
