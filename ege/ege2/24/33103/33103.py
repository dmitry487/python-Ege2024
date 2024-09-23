f = open('ege2/24/33103/inf_22_10_20_24.txt').readlines()

max_posl = 0
for posl in f:
    if posl.count('A') > posl.count('Е'):
        max_posl = max(max_posl, len(posl))


print(max_posl)
