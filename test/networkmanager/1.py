import wifi 
import subprocess
import time 
import re
import json

def getAccessPoints():
	""" gets all AccessPoints """
	#nmcli -f all device wifi
	#SSID,SSID-HEX,BSSID,MODE,CHAN,FREQ,RATE,SIGNAL,BARS,SECURITY,WPA-FLAGS,RSN-FLAGS,DEVICE,ACTIVE,*,DBUS-PATH
	arg=['nmcli'
			,'-t'
			,'-f'
			#,'	ssid,ssid-hex,bssid,mode,chan'
			,'SSID,SSID-HEX,BSSID,MODE,CHAN,FREQ,RATE,SIGNAL,BARS,SECURITY,WPA-FLAGS,RSN-FLAGS,DEVICE,ACTIVE,DBUS-PATH'
			,'device'
			,'wifi'
			]
	out=subprocess.check_output(arg)
	return out

def getConnectionInfos():
	""" get all Connection Infos """
	#nmcli -f all c show
	#NAME,UUID,TYPE,TIMESTAMP,TIMESTAMP-REAL,AUTOCONNECT,READONLY,DBUS-PATH,ACTIVE,DEVICE,STATE,ACTIVE-PATH          
	arg=['nmcli'
			,'-t'
			,'-f'
			,'NAME,UUID,TYPE,TIMESTAMP,TIMESTAMP-REAL,AUTOCONNECT,READONLY,DBUS-PATH,ACTIVE,DEVICE,STATE,ACTIVE-PATH'
			,'connection'
			,'show'
			]
	out=subprocess.check_output(arg)
	return out

def output2List(str):
	rows=[]
	pattern=r"(?<!\\):"
	splitrows=str.split('\n')
	for row in splitrows:
		cols=re.split(pattern,row)
		rows.append(cols)
	return rows

def output2Dict(str,keys):
	rows=[]
	pattern=r"(?<!\\):"
	splitrows=str.split('\n')
	for row in splitrows:
		cols=dict()
		splitCols=re.split(pattern,row)
		for i in range(len(splitCols)):
			cols[keys[i]]=splitCols[i]
			#print splitCols[i]
		rows.append(cols)
	return rows

def getAccessPointsDict():
	keys=['SSID','SSID-HEX','BSSID','MODE','CHAN','FREQ','RATE','SIGNAL','BARS','SECURITY','WPA-FLAGS','RSN-FLAGS','DEVICE','ACTIVE','DBUS-PATH' ]
	dict=output2Dict (getAccessPoints(), keys ) 
	return dict
	
def getConnectionInfosDict():
	keys=("NAME","UUID","TYPE","TIMESTAMP","TIMESTAMP-REAL","AUTOCONNECT","READONLY","DBUS-PATH","ACTIVE","DEVICE","STATE","ACTIVE-PATH")
	dict=output2Dict (getConnectionInfos(), keys ) 
	return dict

def getApandConInfoDict():
	aps=getAccessPointsDict()	
	cons=getConnectionInfosDict()
	table=[]
	for ap in aps:
		row=dict()
		row.update(ap)
		for con in cons:
			if con['NAME']==ap['SSID']:
				row["CONNECTION"]=dict()
				row["CONNECTION"].update(con)
		table.append(row)
	return table

#/////////////////////////////////////////////////////////////
def connect(ssid,password):
	""" Verbindet und erzeugt eine Connection
		arguments:
		ssid -- String
		password -- String

		return: konsolenausgabe
	"""
	arg=[
		'nmcli'
		,'device'
		,'wifi'
		,'connect'
		,ssid
		,'password'
		,password
	]
	out=subprocess.check_output(arg)
	return out

def regTest():
	txt=r"abc:def\:g:hij"
	pattern=r"(?<!\\):"
	res=re.split(pattern,txt)
	print res

#printAccessPoints()
#print(getConnectionInfo())
#regTest()
#print(output2List(getAccessPoints()))
#print getAccessPointsDict()
#print getConnectionInfosDict()
print getApandConInfoDict()
