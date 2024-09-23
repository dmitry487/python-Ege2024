f = open('ege2/24/63073/24-7.txt').readline()

max_el = 0

for i in range (len(f)  - 1):
    c = 0
    d = 0
    kolichestvo = 0
    for j in range (i, len(f)):
        kolichestvo += 1
        if f[j] == "C":
            c += 1
        elif f[j] == "D":
            d += 1
        if c > 2 or d > 2:
            max_el = max(max_el, kolichestvo - 1)
            break


print(max_el)
