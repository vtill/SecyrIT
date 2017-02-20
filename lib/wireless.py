import wifi 
import subprocess
import time 
import json

#bottle_json_funcs
def get_wifi_json():
	"""
	gets all wifi cells for interface wlan0 and returns the info as ssid
	"""
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
	"""
	gets all saved schemes and returns a json
	"""
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

def get_wifi_scheme_json():
	"""returns json file with wifi and scheme infos"""
	wifiList=getWifiList()
	schemeList=getSchemeList()
	wifi_scheme=getWifiAndScheme(wifiList,schemeList)
	return json.dumps(wifi_scheme)
#############################################################################################
def printWifiNames():
	"""print all cells from interface wlan0"""
	res= wifi.Cell.all('wlan0')
	for r in res:
		print r

def getWifiList():
	"""returns all cells from interface wlan0"""
	res = wifi.Cell.all('wlan0')
	return res

def getSchemeList():
	"""returns all saved schemes"""
	schemeGen=list(wifi.Scheme.all())
	return schemeGen 

def getCompatibleSchemeList(wifiList,schemeList):
	"""compares a list of Cells ssids with a list of safed schemes ssids
	and returns a list of schemes which have the same ssid as the cells from the wifilist

	arguments:
	wifiList -- type wifi.Cell
	SchemeList -- type wifi.Scheme
	"""
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

def getWifiAndScheme(wifiList,schemeList):
	"""compares a list of Cells ssids with a list of safed schemes ssids
	and returns Cells with possible extended infos of scheme options for that Cell

	arguments:
	wifiList -- type wifi.Cell
	SchemeList -- type wifi.Scheme
	"""
	ret=[]
	print ("wifilist length: {}".format(len(wifiList)))
	for cell in wifiList:
		row=dict()
		row['ssid']=						cell.ssid
		row['bitrates']=				cell.bitrates
		row['address']=					cell.address
		row['channel']=					cell.channel
		row['encrypted']=				cell.encrypted
		row['encryption_type']=	cell.encryption_type
		row['frequency']=				cell.frequency
		row['mode']=						cell.mode
		row['quality']=					cell.quality
		row['signal']=					cell.signal
		row['noise']=						cell.noise

		wifi_ssid=cell.ssid      #is used for comparing ssids in schemes

		for scheme in schemeList:
		#debug infos print
			scheme_ssid=scheme.options['wpa-ssid']	
			print ("compare wifi_ssid: {} scheme_ssid {}".format(wifi_ssid,scheme_ssid) )
			if(wifi_ssid==scheme_ssid):
				row['scheme']=							dict()
				row['scheme']['interface']=	scheme.interface
				row['scheme']['name']=			scheme.name
				row['scheme']['psk']=				scheme.options['wpa-psk']
				row['scheme']['ssid']=			scheme.options['wpa-ssid']
				row['scheme']['channel']=		scheme.options['wireless-channel']
			else:
				row['scheme']=None
		ret.append(row)
	return ret

def getSchemeBySsid(ssid):
	"""returns wifi.Scheme if there is a saved Scheme with a given ssid

	argument:
	ssid -- String
	"""
	schemeList=getSchemeList()
	for scheme in schemeList:
		scheme_ssid=scheme.options['wpa-ssid']	
		if(ssid == scheme_ssid):
			return scheme
	return None
		
def showCompatibleSchemeList():
	"""prints saved Schemes with ssids which are found in the Cells from interface wlan0"""
	wifiList=getWifiList()
	schemeList=getSchemeList()
	compatible=getCompatibleSchemeList(wifiList,schemeList)
	print(compatible)	


def createScheme(cell_ssid,cell_pass):
	"""creates Scheme and activates it

	arguments:
	cell_ssid -- string
	cell_pass -- string 
	"""
	cells= wifi.Cell.all('wlan0')
	for cell in cells:
		print "cell_ssid: {} cell.ssid: {}".format(cell_ssid,cell.ssid)
		if(cell.ssid == cell_ssid):
			scheme=wifi.Scheme.for_cell('wlan0',cell_ssid,cell,cell_pass)
			scheme.save()
			try:
				res=scheme.activate()
			except wifi.exceptions.ConnectionError,e:
				print e
				time.sleep(1)
				arg=['ifup','wlan0']
				out=subprocess.check_output(arg)
				print e
				return 'verbindung konnte nicht erzeugt werden, moeglicher weise ist das password falsch'
			print res
			return 'verbindung sollte klappen'
	return 'Fehler ssid nicht gefunden'

def activateScheme(scheme_name):
	"""activates saved Scheme

	arguments:
	scheme_name -- string
	returns 0 if it worked
	retruns -1 if something went wrong
	"""
	scheme=wifi.Scheme.find('wlan0',scheme_name)
	if(scheme):
		scheme.activate()
		return 0
	else:
		return -1

def deleteScheme(scheme_name):
	"""deletes saved Scheme

	arguments:
	scheme_name -- string
	returns 0 if scheme is found
	returns -1 if scheme is notfound
	"""
	scheme=wifi.Scheme.find('wlan0',scheme_name)
	if(scheme):
		scheme.delete()
		return 0
	else:
		return -1

def printSchemes():
	"""prints saved Schemes s.name s.options"""
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
