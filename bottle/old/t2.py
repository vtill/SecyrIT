from bottle import route, run, static_file,request
import wifi 
import mimetypes,os

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
	
def derp():
  #return html(listwifi())
  return html(form_wifi())

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
    filename = 'index.html'
    mt = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
    return static_file(filename, root=folder_root, mimetype=mt)

def send_image(filename):
    mt = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
    return static_file(filename, root=folder_files, mimetype=mt)
      
def get_status():
    fname = '%s/statusfile' % os.getcwd()
    return  '{"status": "%s"}' % str(os.path.exists(fname)) 

def hello():
    return html("hallo")

def index():
   #return "index Hello World!"
    return html("hallo")

def submit():
	#print request.forms.keys()
	print request.POST.keys()
	print request.forms.get('firstname')
	print request.forms.get('access_points')
	#print request
	return "hey"

def showWifi():
  pass  

###################################################################################
#@route('/')
#@route('/files/<filename:re:.*\.*>')
#@route('/status')
#route('/',callback=blubb)
#route('/','GET',index)

route('/','GET',index_html)
route('/derp','GET',derp)
route('/submit_site','POST',submit)
route('/a','GET',index)
route('/files/<filename:re:.*\.*>','GET',send_image)
route('/status','GET',get_status)
route('/scan','GET',get_status)
##################################################################################
printWifiNames()
run(host='10.254.239.1', port=8080, debug=True)
