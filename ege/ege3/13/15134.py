import ipaddress as ip


for i in range (33):
    net = ip.ip_network(f'93.138.161.49/{i}', strict=False)
    print(net, net.netmask)


