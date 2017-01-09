from subprocess import Popen,PIPE,check_output
import json

import sys
import table

def _ip_conntrack():
	file = "/proc/net/nf_conntrack"
	file="conn1.txt"
	stdout=table.load(file)
	return stdout

def ip_conntrack_json():
	str=_ip_conntrack()
	rows=table.getLines(str)
	tbl=table.makeTable(rows,r"\s*")
	tbl_new=[]

	for row in tbl:	
		tmp=ip_conntrack_parse0(row)
		#print "####################################################"
		#print_arr (row )
		#print tmp
		#print "####################################################"
		tbl_new.append(tmp)

	js=json.JSONEncoder().encode(tbl_new)
	return js

def print_arr(arr):
	for idx in range(len(arr)):
		print "arr[" +str(idx)+ "]:"+arr[idx]
	
def ip_conntrack_parse0(row):
	tmp=dict()
	cons=[]
	con1=dict()
	con2=dict()
	status1=0	
	status2=0	
	status3=0	

	case={
		0:"ip_name"
		,1:"ip_num"
		,2:"proto_name"
		,3:"proto_num"
		,4:"TTL"
		,5:"connectionStatus"
		,6:"src1"
		,7:"dst1"
		,8:"sport1"
		,9:"dport1"
		,10:"packets1"
		,11:"bytes1"
		,12:"status1"
		,13:"src2"
		,14:"dst2"
		,15:"sport2"
		,16:"dport2"
		,17:"packets2"
		,18:"bytes2"
		,19:"status2"
		,20:"mark"
		,21:"zone"
		,22:"delta-time"
		,23:"use"
	}

	if(len(row)<5):
		return None	
	if(row[5].find("=")==-1): #found
		status1=1
		tmp["status"]=row[5]
	if(row[11+status1].find("=")==-1): #found
		status2=1
		con1["status"]=row[11+status1]
	if(row[17+status1+status2].find("=")==-1): #found
		con2["status"]=row[17+status1+status2]
		status3=1

	
	#rng=list(list())

	w, h = 5, 5
	rng = [[0 for x in range(w)] for y in range(h)] 


	rng[0][0]=0
	rng[0][1]=5

	#for idx in range(5+status1,11+status1+status2):
	rng[1][0]=5+status1
	rng[1][1]=11+status1+status2
	#for idx in range(11+status1+status2,16+status1+status2+status3):
	#for idx in range(12+status1+status2,18+status1+status2+status3):
	rng[2][0]=11+status1+status2
	rng[2][1]=17+status1+status2+status3
	#for idx in range(17+status1+status2+status3,len(row)):
	#for idx in range(19+status1+status2,+status3,len(row)):
	rng[3][0]=17+status1+status2+status3
	rng[3][1]=len(row)

	#print "status1:"+str(status1)
	#print "status2:"+str(status2)
	#print "status3:"+str(status3)
	#print "rng[0][0]: " +str(rng[0][0])+ " rng[0][1]: " +str(rng[0][1]) 
	#print "rng[1][0]: " +str(rng[1][0])+ " rng[1][1]: " +str(rng[1][1]) 
	#print "rng[2][0]: " +str(rng[2][0])+ " rng[2][1]: " +str(rng[2][1]) 
	#print "rng[3][0]: " +str(rng[3][0])+ " rng[3][1]: " +str(rng[3][1]) 

	for idx in range(rng[0][0],rng[0][1]):
		print "row[" +str(idx)+ "]:"+row[idx]
		tmp[case[idx]]=row[idx]
		if(row[idx].find("=")!=-1): #found
			a=row[idx].split("=")
			tmp[a[0]]=a[1]

	for idx in range(rng[1][0],rng[1][1]):
		print "row[" +str(idx)+ "]:"+row[idx]
		if(row[idx].find("=")!=-1): #found
			a=row[idx].split("=")
			con1[a[0]]=a[1]

	for idx in range(rng[2][0], rng[2][1]):
		print "row[" +str(idx)+ "]:"+row[idx]
		if(row[idx].find("=")!=-1): #found
			a=row[idx].split("=")
			con2[a[0]]=a[1]

	for idx in range(rng[3][0], rng[3][1]):
		print "row[" +str(idx)+ "]:"+row[idx]
		if(row[idx].find("=")!=-1): #found
			a=row[idx].split("=")
			a[0]=a[0].replace("-","_")
			tmp[a[0]]=a[1]


	parsed=dict()
				
	cons.append(con1)
	cons.append(con2)
	tmp["cons"]=cons
	return tmp
	
	
##############################################	
ip_conntrack_json()
