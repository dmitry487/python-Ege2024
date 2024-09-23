import ipaddress as ip 

for i in range (0, 33):
    net = ip.ip_network(f'140.37.235.224/{i}', strict=False)
    print(net, net.netmask)