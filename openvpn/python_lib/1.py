#!/usr/bin/python

import subprocess,os
import requests


def create_pkey(pkey):
	args=["openssl"
		,"genpkey"
		,"-algorithm"
		,"RSA"
		,"-out"
		,pkey
		,"-pkeyopt"
		,"rsa_keygen_bits:2048"
		,"-pkeyopt"
		,"rsa_keygen_pubexp:3"
	]
	out=subprocess.check_output(args)
	print out

def create_csr(pkey,csr,subj):
	args=["openssl"
		,"req"
		,"-new"
		,"-key"
		,pkey
		,"-out"
		,csr
		,"-subj"
		,subj
		,"-batch"
	]
	out=subprocess.check_output(args)
	print out 

def getMac_eth0():
	args=["cat"
		,"/sys/class/net/eth0/address"
	]
	out=subprocess.check_output(args)
	#print out 
	return out

def verify_csr(csr):
	args=["openssl"
		,"req"
		,"-text"
		,"-noout"
		,"-verify"
		,"-in"
		,csr
	]
	out=subprocess.check_output(args)
	print out
	return out

def t2():
	pkey="pkey.key"
	csr="pkey.csr"
	mac=getMac_eth0()
	email="test@abc.net"
	subj="/CN={}/emailAddress={}".format(mac,email)
	create_pkey(pkey)
	create_csr(pkey,csr,subj)
	verify_csr(csr)

def requestCertificate(client_csr,download_tar):
	method="post"
	filename="client.csr"
	url="http://vpn.tillnet.de:8080/upload"
	file={"upload":(filename,open(client_csr,"rb"))}
	res=requests.request(method,url,files=file)
	print(res.headers)
	fp=open(download_tar,"w")
	fp.write(res.content)
	fp.close()
	return res.content

def extract_tar(download_tar,keyFolder):
	args=["tar"
		,"-xf"
		,download_tar
		,"-C"
		,keyFolder
	]
	out=subprocess.check_output(args)
	return out
	
def clientKeyProcessing():
	keyFolder="/root/SecyrIT/openvpn/keys"
	downloadFolder="/root/SecyrIT/openvpn/keys/download"
	pkey="{}/client.key".format(keyFolder)
	csr="{}/client.csr".format(keyFolder)
	crt="{}/client.crt".format(keyFolder)
	ca="{}/ca.crt".format(keyFolder)
	tar="{}/certs.tar".format(downloadFolder)
	
	mac=getMac_eth0()
	email="test@abc.net"
	subj="/CN={}/emailAddress={}".format(mac,email)
 	if not os.path.isfile(pkey) :   
		create_pkey(pkey)
		create_csr(pkey,csr,subj)
		requestCertificate(csr,tar)
		extract_tar(tar,keyFolder)
	else:
		print("file: {} exists".format(pkey))	
 	if not os.path.isfile(csr):   
		create_csr(pkey,csr,subj)
		requestCertificate(csr,tar)
		extract_tar(tar,keyFolder)
	else:
		print("file: {} exists".format(csr))	
 	if not os.path.isfile(crt) or not os.path.isfile(ca):   
		requestCertificate(csr,tar)
		extract_tar(tar,keyFolder)
	else:
		print("file: {} exists".format(crt))	
		print("file: {} exists".format(ca))	

clientKeyProcessing()
