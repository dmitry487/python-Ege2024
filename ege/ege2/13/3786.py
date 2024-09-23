

ip = [255, 255, 240, 0]
ip_bin =[bin(i)[2:].zfill(8) for i in ip]

ad = [232,126,150,18]
ad_bin = [bin(i)[2:].zfill(8) for i in ad]

print(ip_bin)
print(ad_bin)

r = int('011000010010', 2)
print(r)