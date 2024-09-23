import ipaddress as ip


for i in range (0, 33):
    net = ip.ip_network(f'216.23.243.133/{i}', strict=False)
    print(net, net.netmask)