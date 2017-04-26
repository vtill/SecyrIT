import requests

def t1():
	res=requests.request("get","http://www.google.de")
	print res.url
	print res.content
	#print res.text

def t2():
	method="post"
	url="http://vpn.tillnet.de:8080/upload"
	file={"upload":("pkey.csr",open("pkey.csr","rb"))}
	res=requests.request(method,url,files=file)

	print res.content

def t3():
	method="post"
	url="http://vpn.tillnet.de:8080/upload2"
	file={"upload":("pkey.csr",open("pkey.csr","rb"))}
	res=requests.request(method,url,files=file)
	print res.content


t2()
