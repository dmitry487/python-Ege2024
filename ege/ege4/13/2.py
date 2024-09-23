from ipaddress import ip_network
counter = 0

for IpNet in ip_network('192.168.76.160/255.255.255.240'):
    counter += 1
    ip = [bin(int(i))[2:] for i in str(IpNet).split('.')]
    ip = ''.join(ip)
    if (ip[-8:]).count('1')%2 == 0 and counter%2 == 0:
        print(ip)