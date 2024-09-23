import ipaddress as ip


for i in range (33):
    net = ip.ip_network(f'224.32.255.131/{i}', strict=False)
    print(net, net.netmask)


    