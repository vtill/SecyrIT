#/usr/bin/python

from scapy.all import *
import sys
import http

try:
    interface = raw_input('[*] Enter Interface: ')
except KeyboardInterupt:
    print '[*] User requested shutdown ...'
    sys.exit(1)

f='port 53'

def spoof(pkt):
	if (pkt.haslayer(TCP)
	and (pkt.getlayer(TCP).dport == 80 or pkt.getlayer(TCP).dport == 443)
	and pkt.haslayer(Raw)):
		#print pkt.getlayer(Raw).load
		#ip_src = pkt[IP].src
		#ip_dst = pkt[IP].dst
		#print str(ip_src)+' -> '+str(ip_dst)+' : '+')'
		pkt[IP].dst='10.254.239.1'

#sniff(iface=interface, filter, prn=spoof, store=0)
sniff(iface=interface, prn=spoof, store=0)

