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
while True:
   c, addr = s.accept()     
   c.send('Connected')
   key=c.recv(1024)
   number+=1
   print "*"+ key+" had " +str(number)+ " attempt"
   c.close()               