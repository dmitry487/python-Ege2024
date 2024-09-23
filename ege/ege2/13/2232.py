import ipaddress as ip

for i in range (0, 33):
    net = ip.ip_network(f'10.18.134.220/{i}', strict=False)
    print(net, net.netmask)


print(2 ** 18)