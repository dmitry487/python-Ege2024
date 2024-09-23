f = open('ege3/26/6641/64956/26.txt')


n = 890

clients = [
    [int(i) for i in row.split()] for row in f
]

clients = sorted(clients, key = lambda x: x[0])

windows = {
    i:[] for i in range (1, 7)
}

ushel = 0
for prinhod, ojidat, okno in clients:
    if (not(windows[okno])):
        windows[okno].append(prinhod + ojidat)

    elif (windows[okno][-1] <= prinhod + 30):
        windows[okno].append((max(windows[okno][-1], prinhod)) + ojidat)

    else:
        ushel += 1


print(min([len(windows[i]) for i in range(1, 7)]))
print(ushel)
