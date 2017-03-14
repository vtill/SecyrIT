import datetime
import subprocess

folder="/root/SecyrIT/pcap/"
scriptPath="/root/SecyrIT/bash_scripts/pcap.sh"

def fileName():
	date=datetime.datetime.now()
	filename="{}_{}_{}__{}_{}_{}".format(date.year,date.month,date.day,date.hour,date.minute,date.second)
	return filename

	
def run():
	fName=fileName()
	filePath='{}{}.pcap'.format(folder,fName)	
	args=[scriptPath,filePath]
	try:
		out=subprocess.call(args)
	except subprocess.CalledProcessError, e:
		print "error"
		pass
