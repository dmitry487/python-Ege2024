def f20(s1, step= 1): #1p 2v 3p 4v 5p
    if ((s1 >= 67) and (step == 4)):
        return True
    elif (((s1 < 67) and (step == 4)) or
    ((s1 >= 67) and (step != 4))):
        return False
    
    if step%2 == 1:
        return (
        f20(s1 + 1, step + 1) or
        f20(s1 + 4,  step + 1) or 
        f20(s1 * 5, step + 1) 
        
        )
    return (
        f20(s1 + 1,  step + 1) and
        f20(s1 + 4,  step + 1) and 
        f20(s1 * 5,  step + 1) 

    )

for s1 in range (1, 68):
    if f20(s1):
        print(s1)