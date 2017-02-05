###########################################################
#File Name-server.py                                      #
#Use - Runs a server to count number of clients under ssh #
#Written By-Ravi Gupta                                    #
#Date-4/2/2017
#Updated Date-5/2/2017                                    #
###########################################################

import socket               

TCP_IP = '127.0.0.1' # IP to be changed as required
TCP_PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))        

s.listen(5)
print "Matrix for Login SSH attempts"  
number=0
dict={}        
while True:
   c, addr = s.accept()     
   c.send('Connected')
   host=c.recv(1024)
   if dict.has_key(host) :
        val=dict[host]
        val+=1
        dict[host]=val
   else :
        dict[host]=1
   print "*"+ host+" had " + str(dict[host]) + " attempt"
   c.close()               