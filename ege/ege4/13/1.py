import ipaddress as ip


for i in range (33):
    net = ip.ip_network(f'20.24.110.42/{i}', strict=False)
    print(net, net.netmask)


