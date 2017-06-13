import multiprocessing
import subprocess

def p1():
	args=["gvim"]
	subprocess.check_output(args)

def p2():
	for x in range(1000000):
		print x

if __name__ == '__main__':
	p1=multiprocessing.Process(target=p1)
	p1.start()
	p2=multiprocessing.Process(target=p2)
	p2.start()
