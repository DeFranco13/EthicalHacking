# voorbeeld van een socket client

import socket

sock_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # we maken socket object aan
sock_.connect((socket.gethostname(), 9336))  # verbinden met de server
msg = sock_.recv(1024)
sock_.close()
print(msg.decode("ascii"))
