import ipaddress as ip

for i in range (33):
    net = ip.ip_network(f'142.9.199.145/{i}', strict=False)
    print(net, net.netmask)