f = open('ege3/24/59729/1_24.txt').read()
min_ = 300434930930
res = []
kolichestvo = 0
for i in range (len(f) - 1):
    if f[i] + f[i + 1] == 'TT':
        res.append(i)


for j in range (0, len(res) - 149):
    kolichestvo = res[j + 149] - res[j] + 2

    min_ = min(min_, kolichestvo)


print(min_)

    
