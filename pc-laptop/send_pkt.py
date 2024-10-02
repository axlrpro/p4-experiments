from scapy.all import *
import sys

args = sys.argv[1:]
if(len(args)!=5):
    print("usage: send_pkt.py <src_ip> <dst_ip> <msg> <interface> <repetitions>")
    exit(1)
    
src_ip = args[0]
dst_ip = args[1]
msg = args[2]
iface = args[3]
repetitions = int(args[4])

for i in range(repetitions):
    p = Ether()/IP(dst=dst_ip, src=src_ip)/UDP()/msg
    sendp(p, iface=iface)
    