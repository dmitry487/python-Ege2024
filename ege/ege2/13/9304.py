import ipaddress as ip


for i in range (33):
    net = ip.ip_network(f'227.138.127.144/{i}', strict=False)
    print(net, net.netmask)