addr = [bin(int(i))[2:].zfill(8) for i in str('98.162.71.64').split('.')]
addr_ip = [bin(int(i))[2:].zfill(8) for i in str('98.162.71.94').split('.')]
print(addr)
print(addr_ip)

