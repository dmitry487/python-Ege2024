import ipaddress as ip
from ipaddress import *
for i in range(0, 33):
    net = ip.ip_network(f'145.92.137.88/255.255.240.0', strict=False)
    print(net.network_address, net.netmask)

#BHEA - otvet