import ipaddress as ip


for i in range (33):
    net = ip.ip_network(f'93.138.70.47/{i}', strict=False)
    print(net, net.netmask)



n = 192
n_bin = bin(n)[2:]
print(n_bin + '1' * 16)
print((n_bin + '1' * 16).count('1'))