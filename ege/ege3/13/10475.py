import ipaddress as ip


for i in range (33):
    net = ip.ip_network(f'119.167.50.77/{i}',strict=False)
    print(net, net.netmask)