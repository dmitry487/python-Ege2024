from ipaddress import IPv4Network

ip = IPv4Network('224.32.255.131/255.255.240.0', strict=False)

print(ip)
