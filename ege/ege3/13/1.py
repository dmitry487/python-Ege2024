import ipaddress as ip

counter = 0
for i in ip.ip_network('192.168.32.160/255.255.255.240'):
    bin_ip = bin(int(i))[2:]
    if bin_ip.count('1')%2 == 0:
        counter += 1


print(counter)



