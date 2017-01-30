##########################
from bottle import route, run, static_file,request,response
from subprocess import Popen,PIPE,check_output

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
import nf_conntrack 
import wireless 
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

def showWifi():
  pass  

def datei(pfad):
	banana="/root/SecyrIT/bottle/htdocs"
	return static_file(pfad,root=banana)

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

route('/<pfad:path>','GET',datei)

##################################################################################

print table.load("main.py")
run(host='10.254.239.1', port=8080, debug=True)
