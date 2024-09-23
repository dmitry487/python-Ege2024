import ipaddress as ip


for i in range (33):
    net = ip.ip_network(f'129.130.131.128/{i}', strict=False)
    print(net, net.netmask)