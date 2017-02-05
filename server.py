###########################################################
#File Name-server.py                                      #
#Use - Runs a server to count number of clients under ssh #
#Written By-Ravi Gupta                                    #
#Date-4/2/2017                                            #
###########################################################
import socket               

s = socket.socket()         
host = socket.gethostname() 
port = 12345                
s.bind((host, port))        

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