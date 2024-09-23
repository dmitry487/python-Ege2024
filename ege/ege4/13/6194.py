import ipaddress as ip

for i in range (33):
    net = ip.ip_network(f'229.37.229.32/{i}', strict= False)
    print(net, net.netmask)