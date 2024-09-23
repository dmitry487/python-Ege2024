def f19(s1, s2, step=1): #1p 2v 3p 4v 5p
    if ((s1 + s2 >= 86) and (step == 3)):
        return True
    elif (((s1 + s2 < 86) and (step == 3)) or
    ((s1 + s2 >= 86) and (step != 3))):
        return False
    
    return (
        f19(s1 + 1, s2, step + 1) or
        f19(s1, s2 + 1, step + 1) or 
        f19(s1 * 2, s2, step + 1) or
        f19(s1, s2 * 2, step + 1)
    )

for s2 in range (1, 72):
    if f19(14, s2):
        print(s2)
        break

print('---------------------------')

def f19(s1, s2, step=1): #1p 2v 3p 4v 5p
    if ((s1 + s2 >= 86) and (step == 4)):
        return True
    elif (((s1 + s2 < 86) and (step == 4)) or
    ((s1 + s2 >= 86) and (step != 4))):
        return False
    
    
    if step%2 == 1:
        return (
            f19(s1 + 1, s2, step + 1) or
            f19(s1, s2 + 1, step + 1) or 
            f19(s1 * 2, s2, step + 1) or
            f19(s1, s2 * 2, step + 1)
        )
    return (
        f19(s1 + 1, s2, step + 1) and
        f19(s1, s2 + 1, step + 1) and 
        f19(s1 * 2, s2, step + 1) and
        f19(s1, s2 * 2, step + 1)
    )

for s2 in range (1, 72):
    if f19(14, s2):
        print(s2)

print('------------------------')

def f19(s1, s2, step=1): #1p 2v 3p 4v 5p
    if ((s1 + s2 >= 86) and (step in (3, 5))):
        return True
    elif (((s1 + s2 < 86) and (step == 5)) or
    ((s1 + s2 >= 86) and (step != 5))):
        return False
    
    
    if step%2 == 1:
        return (
            f19(s1 + 1, s2, step + 1) and
            f19(s1, s2 + 1, step + 1) and 
            f19(s1 * 2, s2, step + 1) and
            f19(s1, s2 * 2, step + 1)
        )
    return (
        f19(s1 + 1, s2, step + 1) or
        f19(s1, s2 + 1, step + 1) or
        f19(s1 * 2, s2, step + 1) or
        f19(s1, s2 * 2, step + 1)
    )

for s2 in range (1, 72):
    if f19(14, s2):
        print(s2)
        break

