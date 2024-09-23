t = [0]*10000
for n in range(1,1000):
    s = bin(n)[2:] + bin(n%4)[2:]
    r = int(s,2)
    t[r] = 1
 
maxi = 0
for i in range(1000):
    maxi = max( maxi, sum(t[i : i + 49]))
 
print(maxi)  