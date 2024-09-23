import ipaddress as ip


for i in range(0, 33):
    net = ip.ip_network(f'192.168.32.160/{i}', strict=False)
    print(net.network_address, net.netmask)

        