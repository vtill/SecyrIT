#!/usr/bin/python
# -*- coding: utf-8 -*-
import GeoIP

def getCountryNameByAddr(ipv4):
	gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
	#ip
	name=gi.country_name_by_addr(ipv4)
	return name

#gi = GeoIP.new(GeoIP.GEOIP_STANDARD)
#gi = GeoIP.new(GeoIP.GEOIP_MMAP_CACHE)
#gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
#gi = GeoIP.open("/usr/local/share/GeoIP/GeoIP.dat",GeoIP.GEOIP_STANDARD)
#print(gi.country_code_by_name("yahoo.com"))
#print(gi.last_netmask())
#print(gi.country_name_by_name("www.bundestag.de"))
#print(gi.country_code_by_addr("24.24.24.24"))
#print(gi.country_name_by_addr("24.24.24.24"))
#print(gi.range_by_ip("68.180.206.184"))
