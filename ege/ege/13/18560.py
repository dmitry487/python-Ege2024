ip = [98, 162, 78, 139]
ip_bin = [bin((i))[2:].zfill(8) for i in ip]

ip2 = [98, 162, 78, 154]
ip2_bin = [bin((i))[2:].zfill(8) for i in ip2]

print(ip_bin)
print(ip2_bin)