def f19(s1, step=1):
    if s1 >= 129 and step == 3:
        return True
    if ((s1 >= 129 and step != 3) or
         (s1 < 129 and step == 3)):
        return False
    
    if step%2 == 1:
        return (
            f19(s1 + 1, step + 1) and
            f19(s1 * 2, step + 1)
        )
    return (
        f19(s1 + 1, step + 1) or
        f19(s1 * 2, step + 1)
    )


for s1 in range (1, 129):
    if f19(s1):
        print(s1)
        break


print('------------------')



def f20(s1, step=1):
    if s1 >= 129 and step == 4:
        return True
    if ((s1 >= 129 and step != 4) or
         (s1 < 129 and step == 4)):
        return False
    
    if step%2 == 1:
        return (
            f20(s1 + 1, step + 1) or
            f20(s1 * 2, step + 1)
        )
    return (
        f20(s1 + 1, step + 1) and
        f20(s1 * 2, step + 1)
    )


for s1 in range (1, 129):
    if f20(s1):
        print(s1)
        

print('----------------------------')


def f21(s1, step=1):
    if s1 >= 129 and step in (3, 5):
        return True
    if ((s1 >= 129 and step != 5) or
         (s1 < 129 and step == 5)):
        return False
    
    if step%2 == 0:
        return (
            f21(s1 + 1, step + 1) or
            f21(s1 * 2, step + 1)
        )
    return (
        f21(s1 + 1, step + 1) and
        f21(s1 * 2, step + 1)
    )


for s1 in range (1, 129):
    if f21(s1):
        print(s1)
        break