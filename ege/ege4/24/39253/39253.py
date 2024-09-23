f = open('ege4/24/39253/24.txt').read()
counter = 0
max_counter = 0
for i in range (len(f) - 1):
    for j in range (i + 1, len(f)):
        if f[i:j+1].count('D') <= 1:
            max_counter = max(max_counter, len(f[i:j+1]))

print(max_counter)