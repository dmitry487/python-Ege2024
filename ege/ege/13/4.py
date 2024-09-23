import ipaddress as ip

for i in range (0, 33):

    net = ip.ip_network(f'93.138.161.49/{i}', strict=False)
    print(net, net.netmask,(bin(int(net.netmask))[2:]),(bin(int(net.netmask))[2:].count('1')))

