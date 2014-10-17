import socket, traceback
from udt import *

host = 'localhost'                               # Bind to all interfaces
port = 50008

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

messg = raw_input("Enter message: ")
pkt = make_pkt(messg, 0, host, port)
udt_send(pkt)


while True:
    try:
        #pkt, address = s.recvfrom(8192)
        pkt,address = udt_recv(s)
        print(pkt)
        if pkt and pkt.mess == "ACK":
            print("YAY")
        
        if pkt and pkt.is_corrupt == False:
            print("YES")
            print("Got data from", address, pkt.mess)
            messg = raw_input("Enter next message: ")
            pkt.ip = address[0]
            pkt.port = address[1]
            udt_send(pkt)
            
        elif pkt:
            print("NO")
            pkt.ip = address[0]
            pkt.port = address[1]  
            udt_send(pkt)
    except (KeyboardInterrupt, SystemExit):
        break
    except:
        traceback.print_exc()
