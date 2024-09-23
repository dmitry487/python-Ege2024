good_combos = []

for i in '13579':
    good_combos.append(i)

def check(num):
    pop = []
    for pop in num:
        if pop in good_combos and num.count(pop) == 2:
            return True
        return False
    



kolichestvo = 0
for a1 in '12345678':
    for a2 in '012345678':
        for a3 in '012345678':
            for a4 in '012345678':
                for a5 in '012345678':
                    for a6 in '012345678':
                        num = a1 + a2 + a3 + a4 + a5 + a6
                        if check(num) and num.count('4') == 1:
                            kolichestvo += 1

print(kolichestvo)