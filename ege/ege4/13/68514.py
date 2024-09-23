from ipaddress import ip_network
couter = 0
for ipNet in ip_network('122.159.136.144/255.255.255.248'):
    ip = [bin(int(i))[2:] for i in str(ipNet).split('.')]
    ip = ''.join(ip)

    if ip.count('1')%4 != 0:
        couter += 1



print(couter)

    