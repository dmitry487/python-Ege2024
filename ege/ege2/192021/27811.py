def f19(s1, step = 1): #1p 2v 3p 4v 5p
    if (s1 >= 48 and step == 3):
        return True
    elif ((s1 < 48 and step == 3) or
    (s1 >= 48 and step != 3)):
        return False
    
    return (
        f19(s1 + 1, step + 1) or
        f19(s1 + 4, step + 1) or
        f19(s1 * 2, step + 1)
    )

for s1 in range (1, 47):
    if f19(s1):
        print(s1)
        break

print('---------------------')

def f19(s1, step = 1): #1p 2v 3p 4v 5p
    if (s1 >= 48 and step == 4):
        return True
    elif ((s1 < 48 and step == 4) or
    (s1 >= 48 and step != 4)):
        return False
    
    if step%2 == 1:
        return (
        f19(s1 + 1, step + 1) or
        f19(s1 + 4, step + 1) or
        f19(s1 * 2, step + 1)
        )
    return (
        f19(s1 + 1, step + 1) and
        f19(s1 + 4, step + 1) and
        f19(s1 * 2, step + 1)
    )

for s1 in range (1, 47):
    if f19(s1):
        print(s1)
        
print('-----------------')


def f19(s1, step = 1): #1p 2v 3p 4v 5p
    if (s1 >= 48 and (step in (3, 5))):
        return True
    elif ((s1 < 48 and step == 5) or
    (s1 >= 48 and step != 5)):
        return False
    
    if step%2 == 0:
        return (
        f19(s1 + 1, step + 1) or
        f19(s1 + 4, step + 1) or
        f19(s1 * 2, step + 1)
        )
    return (
        f19(s1 + 1, step + 1) and
        f19(s1 + 4, step + 1) and
        f19(s1 * 2, step + 1)
    )

for s1 in range (1, 47):
    if f19(s1):
        print(s1)
        break