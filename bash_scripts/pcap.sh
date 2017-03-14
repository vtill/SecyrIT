#!/bin/bash
	process=`ps -e |grep tcpdump`
	echo $process
	folder=/root/SecyrIT/pcap/

	
	if [ -n "$process" ]
	then
		echo "tcpdump is running if you want to restart kill with ""pkill tcpdump"""
	else
		cd $folder
		tcpdump -G 86400 -w %y_%m_%d__%H_%M_%S.pcap & </dev/null &>/dev/null
	fi
