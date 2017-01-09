from subprocess import Popen,PIPE,check_output

def t1():
	output=Popen(['ls'],stdout=PIPE)
	print output.communicate()
def t2():
	output=check_output(['ls'])
	print output

t1()
