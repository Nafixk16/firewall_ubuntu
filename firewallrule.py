import os
from netfilterqueue import NetfilterQueue
from scapy.all import *
import subprocess
from threading import Thread

class firewall():

    allowPackets = {
        "source":[],
        "dest":""
    }
    ipBlockList ={
        "ip":[]
    }


    def __init__(self):
        t1= Thread(target= self.packetTracing)
        t1.start()


    def blockIP(self,ip):
        self.ipBlockList["ip"].append(ip)
       

    def packetTracing(self):

        nfqueue = NetfilterQueue()
        nfqueue.bind(1, self.print_and_accept)
        try:
            nfqueue.run()
        except KeyboardInterrupt:
            print('interup')
        print("binding")
        nfqueue.unbind()

        
    def print_and_accept(self,pkt):
        
        # print(pkt)
        data =  pkt.get_payload()
        p =  IP(data)
        
        if p.src in self.ipBlockList["ip"]:
            print("packet reject")
        else:
            pkt.accept()
            # print("in ippppppppppppp")
            # print("source IP: ",p.src, "   destination: ",p.dst)    
            # pkt.accept()

        



if __name__== "__main__":
    obj =  firewall()
   



    # obj.blockIP("68.183.70.100")
    

   # pyuic4 -x name.ui -o name.py