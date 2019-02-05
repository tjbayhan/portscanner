#!/usr/bin/env python
#simple port scanner for practicing python

import socket
import subprocess
import sys
from datetime import datetime

#interact to get target 
target = raw_input("Please enter target IP: ")
ip = socket.gethostbyname(target)

#banner
print "-"*60
print "Please wait, scanning target", ip
print"-"*60

#check what time the scan started 
t1=datetime.now()

#range function to specify ports + error handling 

try:
	for port in range (1,1025):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result - sock.connect_ex((ip,port))
		if result == 0:
			print "Port {}:   Open".format(port)
		sock.close()

except KeyboardInterrupt:
	print "You pressed Control+C"
	sys.exit()

except socket.error:
	print "Couldn't connect to server"
	sys.exit()

#time elapsed 
t2 = datetime.now()
total=t2-t1
print 'Scanning Completed in: ',total
