#!/usr/bin/python

import subprocess

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

t2()
