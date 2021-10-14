from socket import *

# UDP 접속
host = 'slogs.dev'
port = 30001

c = socket(AF_INET, SOCK_DGRAM)
msg = '이승용'
c.sendto(msg.encode(), (host, port))
c.close()