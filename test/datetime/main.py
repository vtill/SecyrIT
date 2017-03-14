import datetime
import time

def main():
	date=datetime.datetime.now()
	print date.year
	print date.month
	print date.day
	print date.hour
	print date.minute
	print date.second
	print "{}_{}_{}__{}_{}_{}".format(date.year,date.month,date.day,date.hour,date.minute,date.second)
	
main()
