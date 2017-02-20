import wifi 
import subprocess
import time 
import json
import sys

sys.path.append("../../lib" )
import wireless 

def main():
	wireless.printWifiNames()
	wireless.createScheme('Gargoyle','sub')
	wireless.printSchemes()

print 'hi'
main()
