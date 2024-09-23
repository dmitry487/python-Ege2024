import ipaddress as ip

for i in range (33):
    net = ip.ip_network(f'224.9.195.133/{i}', strict=False)
    print(net, net.netmask)

    