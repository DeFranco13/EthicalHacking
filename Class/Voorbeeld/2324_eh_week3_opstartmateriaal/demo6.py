# voorbeeld van een socket server

import socket

host = socket.gethostname()  # connecteert met de localhost
port = 9336  # random poortnummer

sock_ = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)  # aanmaak van een socket object
sock_.bind(
    (host, port)
)  # socket object verbinden met host en port => server definiëren
sock_.listen(1)  # luisteren naar inkomende oproepen / 1 connectie max

print("\nServer gestart...\n")

conn, addr = sock_.accept()  # we accepteren connectie van client

print("Verbinding gelegd met: ", str(addr))

boodschap = "\nBedankt om te verbinden! " + str(addr)
conn.send(boodschap.encode("ascii"))
conn.close()
