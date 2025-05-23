def f19(s1, step = 1): #1p 2v 3p 4v 5p
    if (s1 >= 29) and (step == 4):
        return True
    elif ((s1 < 29) and (step == 4) or
    (s1 >= 29) and (step != 4)):
        return False
    
    return (
        f19(s1 + 1, step + 1) or
        f19(s1 + 2, step + 1) or 
        f19(s1 * 2, step + 1)
    )

for s1 in range (1, 29):
    if f19(s1):
        print(s1)
        break

print('--------------------')

def f20(s1, step = 1): #1p 2v 3p 4v 5p
    if (s1 >= 29) and (step == 5):
        return True
    elif ((s1 < 29) and (step == 5) or
    (s1 >= 29) and (step != 5)):
        return False
    
    if step%2 == 0:
        return (
        f20(s1 + 1, step + 1) or
        f20(s1 + 2, step + 1) or 
        f20(s1 * 2, step + 1)
       )
    return (
        f20(s1 + 1, step + 1) and
        f20(s1 + 2, step + 1) and 
        f20(s1 * 2, step + 1)
    )

for s1 in range (1, 29):
    if f20(s1):
        print(s1)
        