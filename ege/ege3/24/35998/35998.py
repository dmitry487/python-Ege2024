f = open('ege3/24/35998/inf_26_04_21_24.txt').readlines()


def check(posl):
    if posl.count('A') >= 25:
        return False
    else:
        for i in range(len(posl) - 1):
            if posl[i] == posl[i + 1]:
                ...