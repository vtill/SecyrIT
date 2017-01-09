#!/usr/bin/python

#from __future__ import print_function

import GeoIP

#file="/usr/local/share/GeoIP/GeoIPCity.dat"
file="/usr/share/GeoIP/GeoIP.dat"
gi = GeoIP.open(file, GeoIP.GEOIP_STANDARD)

gir = gi.record_by_name("www.google.com")
#gir = gi.record_by_addr("")

if gir is not None:
    print(gir['country_code'])
    print(gir['country_code3'])
    print(gir['country_name'])
    print(gir['city'])
    print(gir['region'])
    print(gir['region_name'])
    print(gir['postal_code'])
    print(gir['latitude'])
    print(gir['longitude'])
    print(gir['area_code'])
    print(gir['time_zone'])
    print(gir['metro_code'])
    print(str(gir))

