import ipaddress as ip

for i in range (0, 33):
    net = ip.ip_network(f'119.83.208.27/{i}', strict = False)
    print(net, net.netmask)


num = bin(255)[2:]