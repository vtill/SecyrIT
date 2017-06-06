import requests

def t1():
	res=requests.request("get","http://www.google.de")
	print res.url
	print res.content
	#print res.text

def t2():
	method="post"
	filename="pkey.csr"
	filepath="csr/{}".format(filename)
	url="http://vpn.tillnet.de:8080/upload"
	file={"upload":(filename,open(filepath,"rb"))}
	res=requests.request(method,url,files=file)

	print res.content

def t3():
	method="post"
	url="http://vpn.tillnet.de:8080/upload2"
	file={"upload":("pkey.csr",open("pkey.csr","rb"))}
	res=requests.request(method,url,files=file)
	print res.content


def requestCertificate():
	method="post"
	filename="pkey.csr"
	filepath="csr/{}".format(filename)
	url="http://vpn.tillnet.de:8080/upload"
	file={"upload":(filename,open(filepath,"rb"))}
	res=requests.request(method,url,files=file)
	print(res.headers)
	fp=open("tar/whoopwhoop.tar","w")
	fp.write(res.content)
	print res.content

requestCertificate()
