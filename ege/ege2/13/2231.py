addr = [bin(int(i))[2:].zfill(8) for i in str('255.255.255.224').split('.')]
addr_ip = [bin(int(i))[2:].zfill(8) for i in str('162.198.0.157').split('.')]
print(addr)
print(addr_ip)
r = int('11101', 2)
print(r)