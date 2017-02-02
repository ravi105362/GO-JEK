import time
import socket               

f=open("auth.log","r")
line=f.read()

while True :
	s = socket.socket()        
	host = socket.gethostname() 
	port = 12345 

	if "sshd" in line  :
		print "found"
		s.connect((host, port))
		print s.recv(1024)
		s.send(host)
		s.shutdown(1)
		s.close
	time.sleep(1)