from ipaddress import ip_network
kolichestvo = 0

for ipAdr in ip_network('122.159.136.144/255.255.255.248'):
    
    
    ip = [bin(int(i))[2:] for i in str(ipAdr).split('.')]
    ip = ''.join(ip)
    # ip = bin(int(ipAdr))[2:]
    if ip.count('1')%4 != 0:
        
        kolichestvo += 1


print(kolichestvo)
