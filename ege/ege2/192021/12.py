def f20(s1, s2, step= 1): #1p 2v 3p 4v 5p
    if ((s1 + s2 >= 49) and (step == 4)):
        return True
    elif (((s1 + s2 < 49) and (step == 4)) or
    ((s1 + s2 >= 49) and (step != 4))):
        return False
    
    if step%2 == 1:
        return (
        f20(s1 + 1, s2, step + 1) or
        f20(s1, s2 + 1, step + 1) or 
        f20(s1 * 3, s2, step + 1) or
        f20(s1, s2 * 3, step + 1)
        )
    return (
        f20(s1 + 1, s2, step + 1) and
        f20(s1, s2 + 1, step + 1) and 
        f20(s1 * 3, s2, step + 1) and
        f20(s1, s2 * 3, step + 1)
    )

for s2 in range (1, 43):
    if f20(5, s2):
        print(s2)
        