import socket 
s = socket.socket() 
host = socket.gethostname() 
port = 40000 
s.connect((host, port)) 
s.send("Hello server!".encode()) 
with open('received_file', 'wb') as f:
    while True: 
        print('receiving data...') 
        data = s.recv(1024)  
        if not data:
            break
        print(data.decode())
        f.write(data) 
f.close() 
print('Successfully get the file') 
s.close() 
print('connection closed')