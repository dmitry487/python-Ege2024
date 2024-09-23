def f19(s1, step = 1): #1p 2v 3p 4v 5p
    if s1 >= 435 and step == 3:
        return True
    if ((s1 >= 435 and step !=3) or
         (s1 < 435 and step != 3)):
        return False
    
    if step%2 == 0:
        return (
            f19(s1 + 5, step + 1) or
            f19(s1 * 3, step + 1)
        )
    return (
            f19(s1 + 5, step + 1) and
            f19(s1 * 3, step + 1)
        )


for s1 in range (1, 435):
    if f19(s1):
        print(s1)
        break