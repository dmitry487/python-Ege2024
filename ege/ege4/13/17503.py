from ipaddress import IPv4Network

kolichestvo = 0
for ip in IPv4Network('122.159.68.144/255.255.255.240'):
    bin_ip = [bin(int(i))[2:].zfill(8) for i in str(ip).split('.')]
    bin_ip = ''.join(bin_ip)
    if bin_ip.count('0')%3 != 0:
        kolichestvo += 1



print(kolichestvo)