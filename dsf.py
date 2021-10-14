import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('slogs.dev', 30000))

filename = 'output.jpg'
print("파일 수신 시작")
with open(filename, "wb") as f:
    try:
        data = sock.recv(8192)
        f.write(data)
        while data:
            data = c.recv(8192)
            f.write(data)
    except Exception as ex:
        print(ex)

    f.close()

#sock.send('LeeSeungYong'.encode())