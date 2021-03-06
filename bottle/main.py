##########################
from bottle import route, run, static_file,request,response
from subprocess import Popen,PIPE,check_output,CalledProcessError,call
import multiprocessing

import requests
import re
import wifi 
import mimetypes,os
import pwd
import json

########
import sys
sys.path.append("../lib" )
import table
import netstat
import netmgr
import nf_conntrack 
import wireless 
import pcap
######
##########################

#global
folder_root  = os.getcwd()
folder_files = '%s/files' % folder_root
################################################

def getWifiNames():
  res= wifi.Cell.all('wlan0')
  return res

def printWifiNames():
  res= wifi.Cell.all('wlan0')
  for r in res:
    print r

def listwifi():
  cell=getWifiNames()
  list=[]
  list.append('<ul>')
  for c in cell:
    list.append('<li>%s</li>' % c.ssid)
  list.append('</ul>')
  return '\n'.join(list)

def optionwifi():
  cell=getWifiNames()
  list=[]
  for c in cell:
    list.append('<option value="{}">{}</option>'.format(c.ssid,c.ssid) )
  return '\n'.join(list)

def html(str):
  begin='<!DOCTYPE html>\n<html>\n<head>\n<title>Title of the document</title>\n</head>\n<body>'
  end='</body>\n</html>'
  html=[]
  html.append(begin)
  html.append(str)
  html.append(end)
  return '\n'.join(html)
	
def html_arr(str):
  begin='<!DOCTYPE html>\n<html>\n<head>\n<title>Title of the document</title>\n</head>\n<body>'
  end='</body>\n</html>'
  html=[]
  html.append(begin)
  html.extend(str)
  html.append(end)
  return '\n'.join(html)

def form_wifi():
	str=[]
	str.append('<form action="submit_site" method="POST">')
	str.append('<input type="text" name="firstname" value="Mickey"><br>')
	str.append('<select name="access_points">')
	str.append(optionwifi())
	str.append('</select>')
	str.append('<input type="submit" value="Submit">')
	str.append('</form>')
	return '\n'.join(str)

######################################################################################
#########
def hello():
	return html("hallo")

def index():
	#return "index Hello World!"
	return html("hallo")

def submit():
	#print request.forms.keys()
	print request.POST.keys()
	print request.POST.get('firstname')
	print request.forms.get('firstname')
	print request.forms.get('access_points')
	#print request
	return "request.POST.keys()"

#########

def index_html():
	folder_root='/root/SecyrIT/bottle/htdocs'
	filename = 'index.html'
	mt = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
	return static_file(filename, root=folder_root, mimetype=mt)

def send_image(filename):
	mt = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
	return static_file(filename, root=folder_files, mimetype=mt)
      
def get_status_bak():
	fname = '%s/statusfile' % os.getcwd()
	return  '{"status": "%s"}' % str(os.path.exists(fname)) 

def datei(pfad):
	banana="/root/SecyrIT/bottle/htdocs"
	return static_file(pfad,root=banana)

#########

def get_status_nf():
	ret=html(nf_conntrack.nf_conntrack())
	return ret

def get_status_ip():
	ret=html(netstat.ip_conntrack())
	return ret

def get_status_netstat():
	ret=html(netstat.netstat_nat())
	return ret


def get_status_nf_json():
	ret=nf_conntrack.nf_conntrack_json()
	response.content_type = 'application/json'
	return json.dumps(ret)

def get_status_ip_json():
	ret=netstat.ip_conntrack_json()
	response.content_type = 'application/json'
	return json.dumps(ret)

def get_status_netstat_json():
	ret=netstat.netstat_nat_json()
	response.content_type = 'application/json'
	return json.dumps(ret)

	
def choose_wifi():
  #return html(listwifi())
  return html(form_wifi())

#########
def create_scheme():
	print request.POST.keys()

	ssid=request.POST.get('ssid')
	passw=request.POST.get('pass')
	print ssid
	print passw
	res=wireless.createScheme(ssid,passw)
	print res
	return res

def activate_scheme():
	#ssid=request.POST.get('ssid')
	#scheme=getSchemeBySsid(ssid)
	scheme=request.POST.get('scheme')
	res=wireless.activateScheme(scheme)
	return res

def delete_scheme():
	#ssid=request.POST.get('ssid')
	#scheme=getSchemeBySsid(ssid)
	scheme=request.POST.get('scheme')
	res=wireless.deleteScheme(scheme)
	return res

#########
def getApandConInfoJson():
	tbl=netmgr.getApandConInfoDict()
	response.content_type = 'application/json'
	return json.dumps(tbl)

def create_netmgr():
	print request.POST.keys()

	ssid=request.POST.get('ssid')
	passw=request.POST.get('pass')
	res=netmgr.create(ssid,passw)
	print res

	response.content_type = 'application/json'
	js=json.dumps(res)
	return js

def activate_netmgr():
	print request.POST.keys()

	ssid=request.POST.get('ssid')
	res=netmgr.activate(ssid)
	print res

	response.content_type = 'application/json'
	js=json.dumps(res)
	return js

def delete_netmgr():
	print request.POST.keys()

	ssid=request.POST.get('ssid')
	res=netmgr.delete(ssid)
	print res

	response.content_type = 'application/json'
	js=json.dumps(res)
	return js
#########
def update_secyrIT():
	arg=[
		'/root/SecyrIT/bash_scripts/updateSecyrIT.sh'
	]

	try:
		update_out=check_output(arg)
	except CalledProcessError, e:
		pass

	response.content_type = 'application/json'
	js=json.dumps(update_out)
	return js

def restart_secyrIT():
	arg=[
		'/root/SecyrIT/init_d_scripts/bottle'
		,"restart"
	]
	try:
		restart_out=check_output(arg)
	except CalledProcessError, e:
		pass

	response.content_type = 'application/json'
	js=json.dumps(_out)
	return js

#########
def pcap_read():
	sPcapFileName="17_03_20__10_03_20.pcap"
	dstIP=request.POST.get("dstIP")
	srcPort=request.POST.get("srcPort")
	print("dstIP: {}  srcPort: {}").format(dstIP,srcPort)
	out=pcap.read(sPcapFileName, dstIP, srcPort)
	js=json.dumps(out)
	return js
#########
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
	

def login():
	p1=multiprocessing.Process(target=login_proc)
	p1.start()
	#p1.join() #darf nicht genutzt werden weil es die prozesse vereint  
	return "done"

def login_proc():
	args=["openvpn","--config","/root/SecyrIT/openvpn/conf/client.conf"]
	call(args,stdin=None,stdout=None,stderr=None,shell=False)		
	

###################################################################################
#@route('/')
#@route('/files/<filename:re:.*\.*>')
#@route('/status')
#route('/',callback=blubb)
#route('/','GET',index)

route('/files/<filename:re:.*\.*>','GET',send_image)
route('/','GET',index_html)

route('/wifi','GET',choose_wifi)
route('/submit_site','POST',submit)

route('/status','GET',get_status_nf)
route('/status_nf','GET',get_status_nf)
route('/status_ip','GET',get_status_ip)
route('/status_netstat','GET',get_status_netstat)

route('/status_nf_json','GET',get_status_nf_json)
route('/status_ip_json','GET',get_status_ip_json)
route('/status_netstat_json','GET',get_status_netstat_json)

route('/get_wifi_json','GET',wireless.get_wifi_json)
route('/get_scheme_json','GET',wireless.get_scheme_json)
route('/get_wifi_scheme_json','GET',wireless.get_wifi_scheme_json)
route('/create_scheme','POST',create_scheme)
route('/delete_scheme','POST',delete_scheme)
route('/activate_scheme','POST',activate_scheme)

route('/get_ap_con_info_json','GET',getApandConInfoJson)
route('/create_netmgr','POST',create_netmgr)
route('/delete_netmgr','POST',delete_netmgr)
route('/activate_netmgr','POST',activate_netmgr)

route('/update','GET',update_secyrIT)
route('/restart','GET',restart_secyrIT)

route('/pcap_read','POST',pcap_read)

route('/login','GET',login)

#######
route('/<pfad:path>','GET',datei)
##################################################################################

pcap.run()
run(host='10.254.239.1', port=8080, debug=True)
