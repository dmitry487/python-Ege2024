import ipaddress as ip


for i in range (33):
    net = ip.ip_network(f'119.83.208.27/{i}', strict=False)
    print(net, net.netmask)




n = 224
n_bin = bin(n)[2:]
print(n_bin)