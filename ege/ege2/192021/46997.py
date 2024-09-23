def f21(s1, step = 1): #1p 2v 3p 4v 5p

    if (s1 >= 26) and (step in (3, 5)):
        return True
    
    elif ((s1 < 26 and step == 5) or
    (s1 >= 26 and step != 5)):
        return False
    

    if step%2 == 0:
        return (
            f21(s1 + 1, step + 1) or
            f21(s1 + 2, step + 1) or
            f21(s1 * 2, step + 1)
        )
    
    return (
            f21(s1 + 1, step + 1) and
            f21(s1 + 2, step + 1) and
            f21(s1 * 2, step + 1)
        )

for s1 in range (1, 27):
    if f21(s1):
        print(s1)
        break