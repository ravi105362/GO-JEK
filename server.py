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
   c.send('Thank you for connecting')
   key=c.recv(1024)
   number+=1
   print "*"+ key+" had " +str(number)+ " attempt"
   c.close()               