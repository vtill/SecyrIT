from pythonwifi.iwlibs import Wireless
wifi = Wireless('wlan0')
#print wifi.getEssid()
blubb= wifi.scan()
for b in blubb:
  print b.ssid
#print wifi.getMode()
