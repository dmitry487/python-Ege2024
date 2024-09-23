import ipaddress as ip


for i in range (33):
    net = ip.ip_network(f'224.37.249.32/{i}', strict=False)
    print(net, net.netmask)



