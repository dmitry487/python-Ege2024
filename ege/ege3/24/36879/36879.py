f = open('ege3/24/36879/inf_26_04_21_24.txt')


def check(posl):
    return posl.count('G') < 25

max_posl = 0
for posl in f:
    if check(posl):
        for i in range (len(posl) - 1):
            for j in range (len(posl) - 1, 0, -1):
                if posl[i] == posl[j]:
                    substing = posl[i:j + 1]
                    max_posl = max(max_posl, len(substing) - 1)
                    
    
print(max_posl)

