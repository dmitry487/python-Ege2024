import ipaddress as ip

for i in range (0, 33):
    net = ip.ip_network(f'162.198.0.157/{i}', strict=False)
    print(net, net.netmask)


n_bin = bin(224)[2:]
print(n_bin)