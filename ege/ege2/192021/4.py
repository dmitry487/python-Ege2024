def f19(s1, s2, step=1): #1p 2v 3p 4v 5p
    if ((s1 + s2 >= 107) and (step == 3)):
        return True
    elif ((s1 + s2 < 107) and (step == 3) or
          (s1 + s2 >= 107) and (step != 3)):
        return False
    
    return (
        f19(s1 + 1, s2, step + 1) or
        f19(s1, s2 + 1, step + 1) or
        f19(s1 * 2, s2, step + 1) or
        f19(s1, s2 * 2, step + 1) 
    )

for s2 in range (1, 93):
    if f19(13, s2):
        print(s2)
        break