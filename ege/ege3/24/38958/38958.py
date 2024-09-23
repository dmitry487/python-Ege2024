f = open('ege3/24/38958/24.txt').read()


f = f.split('A')

max_len = 0

for i in range (len(f) - 1):
    

    max_len = max(max_len, len(f[i]) + len(f[i + 1]) + 1)
    

print(max_len)
    
