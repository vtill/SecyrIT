import wifi 
#cell = wifi.Cell.all('wlan0')[0]
#scheme = wifi.Scheme.for_cell('wlan0', 'home', cell, passkey)
#scheme.save()
#scheme.activate()

def getWifiNames():
  res= wifi.Cell.all('wlan0')
  return res

def printWifiNames():
  res= wifi.Cell.all('wlan0')
  for r in res:
    print r

printWifiNames()
#from wifi import Cell
#res= Cell.all('wlan0')
