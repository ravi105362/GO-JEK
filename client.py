###############################################################
#File Name-client.py                                          #
#Use - Returns to server the number of times ssh done on host #
#Written By-Ravi Gupta                                        #
#Date-4/2/2017                                                #
###############################################################

import time
import socket               

filePath = 'auth.log'#set here for example actual path /var/log/auth.log

lastLine = None
with open(filePath,'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            lastLine = line
#print "lastline is "+lastLine
while True:
    with open(filePath,'r') as f:
        lines = f.readlines()
        if lines[-1] != lastLine:
			#print "Last line is not same and line is "+lines[-1]
			if "sshd" in lines[-1] and "Invalid user" in lines[-1] :
				#print "found"
				s = socket.socket()        
				host = socket.gethostname() 
				port = 12345 
				lastLine = lines[-1]
				print(lines[-1])
				s.connect((host, port))
				print s.recv(1024)
				s.send(host)
				s.shutdown(1)
				s.close
        time.sleep(1)