print("Hello World!")

import socket

#서버 코드
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#127.0.0.1 = 로컬호스트, 내부에서는 접근 가능하나 외부에서는 접근 안됨
# -> 테스트 및 내부 서비스에 활용

# 0.0.0.0: : 30000 = 외부에서 접근 가능한 IP
# -> 방화벽 포트 개방 필요
s.bind(('0.0.0.0', 40000))
s.listen(0)

c, addr = s.accept()

print('{}, {}'.format(c, addr))

data = c.recv(1024)
print('수신한 데이터 : {}'.format(data.decode()))

c.close()
s.close()