import os
from netfilterqueue import NetfilterQueue
from scapy.all import *



class firewall():

    allowPackets = {
        "source":[],
        "dest":""
    }

    def packetTracing(self, sourceIP):

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
        # if p.src == "172.217.19.4":
            # print("in ippppppppppppp")
            # print("source IP: ",p.src, "   destination: ",p.dst)    
        pkt.accept()
        



if __name__== "__main__":
    obj =  firewall()
    obj.packetTracing("4")
    

   