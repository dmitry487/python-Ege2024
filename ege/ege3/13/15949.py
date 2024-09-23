import ipaddress as ip



for i in range (33):
    net = ip.ip_network(f'98.162.77.94/{i}', strict=False)
    print(net, net.netmask)