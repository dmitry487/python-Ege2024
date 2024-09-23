from ipaddress import IPv4Network

net = IPv4Network('229.37.229.32/255.255.224.0', strict=False)

print(net)