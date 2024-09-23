from ipaddress import ip_network
kolichestvo = 0
for ipAdr in ip_network('105.224.200.224/255.255.255.224'):
    
    ip = [bin(int(i))[2:] for i in str(ipAdr).split('.')]
    ip = ''.join(ip)
    # ip = bin(int(ipAdr))[2:]
    if ip.count('1')%4 == 0:
        print(ip)
        kolichestvo += 1



print(kolichestvo)