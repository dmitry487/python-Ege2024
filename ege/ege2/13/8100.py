import ipaddress as ip

for i in range (33):
    net = ip.ip_network(f'117.191.88.37/{i}', strict=False)
    print(net, net.netmask)