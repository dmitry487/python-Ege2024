from ipaddress import ip_network

kolichestvo = 0
for ip in ip_network('112.208.0.0/255.255.128.0'):
    bin_ip = [bin(int(i))[2:] for i in str(ip).split('.')]
    bin_ip = ''.join(bin_ip)
    if bin_ip.count('1')%11 == 0:
        print(bin_ip)
        kolichestvo += 1


print(kolichestvo)