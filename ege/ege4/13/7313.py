import ipaddress as ip


for i in range (33):
    net = ip.ip_network(f'200.135.210.135/{i}', strict=False)
    print(net, net.netmask)