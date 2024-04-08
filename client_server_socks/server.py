import socket

HOST = "127.0.0.1"
PORT = 3000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    print("Server is listening!")
    s.listen()

    conn, addr = s.accept()
    with conn:
        print(f"Connected by : {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                print("Conn closed")
                break
            decoded_str = data.decode('utf-8')
            print(f'I got this : {decoded_str}')

            