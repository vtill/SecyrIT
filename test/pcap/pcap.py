import datetime
import subprocess

folder="/root/SecyrIT/test/pcap/"

def fileName():
	date=datetime.datetime.now()
	filename="{}_{}_{}__{}_{}_{}".format(date.year,date.month,date.day,date.hour,date.minute,date.second)
	return filename

	
def run():
	fName=fileName()
	filePath='{}{}.pcap &'.format(folder,fName)	
	args=["/root/SecyrIT/test/pcap/test.sh",fName]
	#args=["tcpdump","-w",fName,"&"]
	try:
		out=subprocess.call(args)
	except subprocess.CalledProcessError, e:
		print "error"
		pass
	
run()
