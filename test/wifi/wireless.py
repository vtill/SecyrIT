import wifi 
import subprocess
import time 

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

def createScheme():
		cell= wifi.Cell.all('wlan0')[2]
		scheme=wifi.Scheme.for_cell('wlan0','town',cell,'falscherMANN')
		print type(scheme)
		#scheme.save()
		scheme.find('wlan0','home')
		scheme.activate()

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


main()
