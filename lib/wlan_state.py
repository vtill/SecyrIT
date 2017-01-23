from subprocess import Popen,PIPE,check_output
import re

def check_wlan0_state():
	def get_output():
		arg=['ip'
				,'link'
				,'show'
				,'wlan0'
				]
		p_output=check_output(arg)
		return p_output
	def get_state(str):
		re_match=re.search('state (\w*)',str)
		state=re_match.group(1)
		return state
	def get_bool_of_state(str):
		if str=='UP':
			state=True
		else:
			state=False
		return state 
	
	out=get_output()
	state=get_state(out)
	bool=get_bool_of_state(state)
	return bool

print check_wlan0_state()
