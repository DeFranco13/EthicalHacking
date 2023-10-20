# Socket server

import socket

class serverSock:
    def run(data, ports):
        
        host = socket.gethostname() # Localhost / vervang met IP voor netwerk verkeer
        port = 1313

        sock_ = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM
        )
        sock_.bind(
            (host, port)
        ) 
        sock_.listen(1) 

        print("\nServer online...\nWaiting for Client...")
        

        conn, addr = sock_.accept()  

        print("Connected: ", str(addr))
        boodschap = "\nHere some data! " + str(addr)
        for i in data:
            boodschap = boodschap + f"\n {i}"
        
        for i in ports:
            boodschap = boodschap + f"\n {i}"

        conn.send(boodschap.encode("ascii"))
        conn.close()

    