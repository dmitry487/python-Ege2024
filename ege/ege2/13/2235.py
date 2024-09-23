addr = [bin(int(i))[2:].zfill(8) for i in str('255.255.224.0').split('.')]
addr_ip = [bin(int(i))[2:].zfill(8) for i in str('206.158.124.67').split('.')]
print(addr)
print(addr_ip)
r = int('1110001000011', 2)
print(r)