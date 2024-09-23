import ipaddress as ip


for i in range (33):
    net = ip.ip_network(f'224.120.249.18/{i}', strict=False)

    print(net, net.netmask)