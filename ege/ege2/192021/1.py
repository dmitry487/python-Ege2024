def f19(s1, step=1): #1p 2v 3p 4v 5p
    if ((s1 >= 45) and (step == 3)):
        return True
    elif ((s1 < 45) and (step == 3) or
          (s1 >= 45) and (step != 3)):
        return False
    
    return (
        f19(s1 + 1,step + 1) or
        f19(s1 + 2, step + 1) or
        f19(s1 * 2, step + 1) 
    )

for s1 in range (1, 29):
    if f19(s1):
        print(s1)
        break