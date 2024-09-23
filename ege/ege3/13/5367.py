import ipaddress as ip


for i in range (33):
    net  = ip.ip_network(f'194.128.208.64/{i}', strict=False)
    print(net, net.netmask)