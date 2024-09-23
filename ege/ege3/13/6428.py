import ipaddress as ip


for i in range (33):
    net = ip.ip_network(f'32.64.208.224/{i}', strict=False)
    print(net, net.netmask)