import os
from netfilterqueue import NetfilterQueue
from scapy.all import *
import subprocess
from threading import Thread
import socket

class firewall():

    allowPackets = {
        "source":[],    
        "dest":""
    }
    ipBlockList ={
        "ip":[]
    }
    portBlockList = {
        "TCP": [],
        "UDP": [],
        "port":[]
    }


    def __init__(self):
        t1= Thread(target= self.packetTracing)
        t1.start()


    def block_TCP_port(self,portnum):
        self.portBlockList["TCP"].append(portnum)

    def block_UDP_port(self,portnum):
        self.portBlockList["UDP"].append(portnum)

    def block_both_port(self,portnum):
        self.portBlockList["port"].append(portnum)

        
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

        
    def findDomain(self,ips):
        print("find domain")
        res = subprocess.run(["host",ips],stdout=subprocess.PIPE)
        print(res)


        
    def print_and_accept(self,pkt):
        
        # print(pkt)
        rule1 = False
        rule2 = False
        rule3= False
        rule4= False

        payload =  pkt.get_payload()
        p =  IP(payload)

        source_port = p.sport

        if TCP in p:
            if source_port in self.portBlockList["TCP"]:
                print("yes port here ", p.sport)
                rule1 = True    
        
        if UDP in p:
            if source_port in self.portBlockList["UDP"]:
                print("yes port here ", p.sport)
                rule2 = True  


        if source_port in self.portBlockList["port"]:
            print("yes port here ", p.sport)
            rule3 = True  



        if p.src in self.ipBlockList["ip"]:
        
            rule4 = True
        
        if rule1==False and rule2==False and rule3==False and rule4==False:
            # print("source IP: ",p.src, "   destination: ",p.dst)
            print("accept")    
            pkt.accept()
        else:
            pkt.drop()
        



if __name__== "__main__":
    obj =  firewall()
    # obj.packetTracing()
   



    # obj.blockIP("68.183.70.100")
    
# iptables -I INPUT -d 10.0.2.15 -j NFQUEUE --queue-num 1
   # pyuic4 -x name.ui -o name.py