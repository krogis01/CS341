import socket, traceback
from udt import *

host = ''                               # Bind to all interfaces
port = 50008

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

while True:
    try:
        #pkt, address = s.recvfrom(1024)
        pkt,address = udt_recv(s)
        if pkt and pkt.is_corrupt == False:
            print("Got data from", address, pkt.mess)
            pkt.mess = "ACK"
            pkt.ip = address[0]
            pkt.port = address[1]
            print(pkt.mess)
            udt_send(pkt)
        elif pkt:
            pkt.mess = "NACK"
            pkt.ip = address[0]
            pkt.port = address[1]
            udt_send(pkt)
    except (KeyboardInterrupt, SystemExit):
        break
    except:
        traceback.print_exc()
