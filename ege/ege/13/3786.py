import ipaddress as ip

for i in range (0, 33):
    net = ip.ip_network(f'232.126.150.18/{i}', strict=False)
    print(net, net.netmask)

