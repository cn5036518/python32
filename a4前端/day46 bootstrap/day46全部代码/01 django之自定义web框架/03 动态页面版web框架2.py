import socket
import  time

server = socket.socket()
IP_PORT = ('127.0.0.1',8001)
server.bind(IP_PORT)
server.listen()

# urlpatterns = [
# 	('/',html),
# 	('/xx.css',css),
# 	('/1.jpg',jpg),
# 	('/xx.js',js),
# 	('/person',person,
# ]

while True:
	conn,addr = server.accept()
	from_client_msg = conn.recv(1024)
	from_browser_msg = from_client_msg.decode()
	print(from_browser_msg)
	path = from_browser_msg.split()[1]

	# for item in urlpatterns:

	conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
	# conn.send(data)
	conn.close()

# server.close()