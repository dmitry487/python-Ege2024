f = open('ege4/24/10105/24_10105.txt').read()
t_index = []
for i in range (len(f)):
    if f[i] == 'T':
        t_index.append(i)

max_len = 0

for i in range (len(t_index) - 101):
    subs = f[t_index[i] + 1:t_index[i + 101]]
    max_len = max(max_len, len(subs))


print(max_len)