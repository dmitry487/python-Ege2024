import ipaddress as ip

for i in range (33):
    net = ip.ip_network(f'238.237.149.255/{i}', strict=False)

    print(net, net.netmask)
    


i = '252'
i_bin = bin(int(i))[2:]
print(i_bin)
