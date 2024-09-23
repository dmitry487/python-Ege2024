from ipaddress import IPv4Network

kolichestvo = 0
for ip in IPv4Network('192.168.32.160/255.255.255.240'):
    bin_ip = [bin(int(i))[2:].zfill(8) for i in str(ip).split('.')]
    bin_ip = ''.join(bin_ip)
    if bin_ip.count('1')%2 == 0:
        kolichestvo += 1


print(kolichestvo)