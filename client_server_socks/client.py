import socket

HOST = "127.0.0.1"
PORT = 3000

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))        
    while True:
        d = input("Enter data to send to server : ")
        if(d == 'exit'):
            break
        s.sendall(d.encode('utf-8'))
        

print(f"Conn closed")
