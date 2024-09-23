import ipaddress as ip

for i in range (0, 33):
    net = ip.ip_network(f'111.81.208.27/{i}', strict=False)
    print(net, net.netmask)