def f20(s1, step= 1): #1p 2v 3p 4v 5p
    if ((s1 >= 48) and (step == 4)):
        return True
    elif (((s1 < 48) and (step == 4)) or
    ((s1 >= 48) and (step != 4))):
        return False
    
    if step%2 == 1:
        return (
        f20(s1 + 1, step + 1) or
        f20(s1 + 3,  step + 1) or 
        f20(s1 * 2, step + 1) 
        
        )
    return (
        f20(s1 + 1,  step + 1) and
        f20(s1 + 3,  step + 1) and 
        f20(s1 * 2,  step + 1) 

    )

for s1 in range (1, 48):
    if f20(s1):
        print(s1)