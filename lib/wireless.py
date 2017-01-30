import wifi 
import subprocess
import time 
import json

#bottle_json_funcs
def get_wifi_json():
	res= wifi.Cell.all('wlan0')
	cells=[]

	for cell in res:
		row=dict()
		row['ssid']=cell.ssid
		row['bitrates']=cell.bitrates
		row['address']=cell.address
		row['channel']=cell.channel
		row['encrypted']=cell.encrypted
		row['encryption_type']=cell.encryption_type
		row['frequency']=cell.frequency
		row['mode']=cell.mode
		row['quality']=cell.quality
		row['signal']=cell.signal
		row['noise']=cell.noise
		cells.append(row)
	#response.content_type = 'application/json'
	return json.dumps(cells)

def get_scheme_json():
	res=getSchemeList()
	schemes=[]
	for scheme in res:
		row=dict()
		row['interface']=scheme.interface
		row['name']=scheme.name
		row['psk']=scheme.options['wpa-psk']
		row['ssid']=scheme.options['wpa-ssid']
		row['channel']=scheme.options['wireless-channel']
		schemes.append(row)
	#response.content_type = 'application/json'
	return json.dumps(schemes)

#############################################################################################
def printWifiNames():
  res= wifi.Cell.all('wlan0')
  for r in res:
    print r

def getWifiList():
  res = wifi.Cell.all('wlan0')
  return res

def getSchemeList():
	schemeGen=list(wifi.Scheme.all())
	return schemeGen 

def getCompatibleSchemeList(wifiList,schemeList):
	ret=[]
	print ("wifilist length: {}".format(len(wifiList)))
	for wifi in wifiList:
		wifi_ssid=wifi.ssid
		print(wifi_ssid)
		for scheme in schemeList:
			scheme_ssid=scheme.options['wpa-ssid']	
			print ("compare wifi_ssid: {} scheme_ssid {}".format(wifi_ssid,scheme_ssid) )
			if(wifi_ssid==scheme_ssid):
				ret.append(scheme)
	return ret

def showCompatibleSchemeList():
	wifiList=getWifiList()
	schemeList=getSchemeList()
	compatible=getCompatibleSchemeList(wifiList,schemeList)
	print(compatible)	

def createScheme(cell_ssid,cell_pass):
	cells= wifi.Cell.all('wlan0')
	for cell in cells:
		if(cell.ssid == cell_ssid):
			scheme=wifi.Scheme.for_cell('wlan0',cell_ssid,cell,cell_pass)
			scheme.save()
			scheme.activate()
			return 0
		else:
			return -1

def activateScheme(scheme_name):
	scheme=wifi.Scheme.find('wlan0',scheme_name)
	if(scheme):
		scheme.activate()
		return 0
	else:
		return -1

def deleteScheme(scheme_name):
	scheme=wifi.Scheme.find('wlan0',scheme_name)
	if(scheme):
		scheme.delete()
		return 0
	else:
		return -1

def printSchemes():
	schemes=getSchemeList()
	for s in schemes:
		print "scheme_name: {} scheme_options: {}".format(s.name,s.options)


def main():
	try:
		print("Schemelist:")
		printSchemes()
		#getSchemeList()[0].activate()
		print("///////////////////////////////////")
		print("WifiNames:")
		printWifiNames()
		#showCompatibleSchemeList()
		createScheme()
	except wifi.exceptions.InterfaceError,e:
		print e
		arg=['ifup','wlan0']
		out=subprocess.check_output(arg)
		main()
	except wifi.exceptions.ConnectionError,e:
		print e
		time.sleep(1)
		arg=['ifup','wlan0']
		out=subprocess.check_output(arg)
		pass
