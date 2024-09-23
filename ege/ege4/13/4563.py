import ipaddress as ip


for i in range (33):
    net = ip.ip_network(f'217.19.128.131/{i}', strict=False)
    print(net, net.netmask)