import ipaddress as ip

for i in range(0, 33):
    net = ip.ip_network(f'119.83.200.27'/[i], strict=False)
    print(net.network_address, net.netmask)