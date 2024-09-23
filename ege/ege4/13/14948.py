from ipaddress import ip_network

counter = 0
for ipAdr in ip_network('192.168.32.128/255.255.255.192'):
    ip = [bin(int(i))[2:] for i in str(ipAdr).split('.')]
    ip = ''.join(ip)
    

    if ip.count('1')%2 == 0:
        counter += 1


print(counter)