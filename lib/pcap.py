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

def read(sPcapFileName, dstIP, srcPort):
	sPcapFile='{}{}'.format(folder,sPcapFileName)

	args=[
	"tcpdump"
	,"-XX"
	,"-r"
	,"{}".format(sPcapFile)
	,"dst"
	,"net"
	,"{}".format(dstIP)
	,"and"
	,"src"
	,"port"
	,"{}".format(srcPort)
	]
	out=None
	try:
		out=subprocess.check_output(args)
	except subprocess.CalledProcessError, e:
		out=e.output
		print "error in pcap execution"
	return out
