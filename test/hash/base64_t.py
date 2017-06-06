import base64
import sys

def t1():
	text="hallo"
	hashed=base64.urlsafe_b64encode(text)
	return hashed

def t2():
	if (len(sys.argv)<3):
		out="usage: script <d|e> <txt>"
		return out
	if not (sys.argv[1]=="e" or sys.argv[1]=="d" ):
		out="usage: script <d|e> <txt>"
		return out
	if (sys.argv[1]=="e"):
		text=sys.argv[2]
		out=base64.urlsafe_b64encode(text)
		return out
	elif (sys.argv[1]=="d"):
		text=sys.argv[2]
		out=base64.urlsafe_b64decode(text)
		return out

print t2()
