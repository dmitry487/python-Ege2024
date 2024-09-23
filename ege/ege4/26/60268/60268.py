f = open('ege4/26/60268/test.txt')

info = [[int(i) for i in row.split()] for row in f]
lastStop = 0
info = [sorted(info)]
res = []

for start, stop in info:
    if start >= lastStop:
        lastStop += stop

        res.append(info)

print(len(res))
