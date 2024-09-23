def f19(s1, s2, step = 1): #1p 2v 3p 4v 5p
    if s1 + s2 >= 231 and step == 3:
        return True
    elif ((s1 + s2 >= 231 and step != 3) or 
    (s1 + s2 < 231 and step == 3)):
        return False 
    

    return (
        f19(s1 + 4, s2, step + 1) or
        f19(s1, s2 + 4, step + 1) or
        f19(s1 * 3, s2, step + 1) or
        f19(s1, s2 * 3, step + 1)
    )



for s2 in range (1, 218):
    if f19(10, s2):
        print(s2)
        break


print('------------------')



def f20(s1, s2, step = 1): #1p 2v 3p 4v 5p
    if s1 + s2 >= 231 and step == 4:
        return True
    elif ((s1 + s2 >= 231 and step != 4) or 
    (s1 + s2 < 231 and step == 4)):
        return False 
    

    if step%2 == 1:
        return (
        f20(s1 + 4, s2, step + 1) or
        f20(s1, s2 + 4, step + 1) or
        f20(s1 * 3, s2, step + 1) or
        f20(s1, s2 * 3, step + 1)
    )
    return (
        f20(s1 + 4, s2, step + 1) and
        f20(s1, s2 + 4, step + 1) and
        f20(s1 * 3, s2, step + 1) and
        f20(s1, s2 * 3, step + 1)
    )



for s2 in range (1, 218):
    if f20(10, s2):
        print(s2)
        


print('---------------------')


def f21(s1, s2, step = 1): #1p 2v 3p 4v 5p
    if s1 + s2 >= 231 and step in (3, 5):
        return True
    elif ((s1 + s2 >= 231 and step != 5) or 
    (s1 + s2 < 231 and step == 5)):
        return False 
    

    if step%2 == 0:
        return (
        f21(s1 + 4, s2, step + 1) or
        f21(s1, s2 + 4, step + 1) or
        f21(s1 * 3, s2, step + 1) or
        f21(s1, s2 * 3, step + 1)
    )
    return (
        f21(s1 + 4, s2, step + 1) and
        f21(s1, s2 + 4, step + 1) and
        f21(s1 * 3, s2, step + 1) and
        f21(s1, s2 * 3, step + 1)
    )



for s2 in range (1, 218):
    if f21(10, s2):
        print(s2)