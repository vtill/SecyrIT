#/usr/bin/python

from scapy.all import *
import sys



def querysniff(pkt):
    if IP in pkt:
        ip_src = pkt[IP].src
        ip_dst = pkt[IP].dst
        if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
            print str(ip_src)+' -> '+str(ip_dst)+' : '+pkt.getlayer(DNS).qd.name+')'


try:
    interface = raw_input('[*] Enter Interface: ')
except KeyboardInterupt:
    print '[*] User requested shutdown ...'
    sys.exit(1)

sniff(iface=interface, filter='port 53', prn=querysniff, store=0)