for n in range (1, 3):

    def f19(s1, s2, step= 1): #1p 2v 3p 4v 5p
        if ((s1 + s2 >= 48) and (step == 3)):
            return True
        elif (((s1 + s2 < 48) and (step == 3)) or
        ((s1 + s2 >= 48) and (step != 3))):
            return False
        
        if step%2 == 1:
            if (s1 > s2): return f19(s1 + n, s2, step + 1) or f19(s1, s2 * 3, step + 1)
            if (s2 > s1): return f19(s1, s2 + n, step + 1) or f19(s1 * 3, s2, step + 1)

        if (s1 > s2): return f19(s1 + n, s2, step + 1) or f19(s1, s2 * 3, step + 1)
        if (s2 > s1): return f19(s1, s2 + n, step + 1) or f19(s1 * 3, s2, step + 1)
        

    for s2 in range (1, 47):
        if f19(13, s2):
            print(s2)
            break
        

for n in range (1, 3):

    def f20(s1, s2, step= 1): #1p 2v 3p 4v 5p
        if ((s1 + s2 >= 48) and (step == 3)):
            return True
        elif (((s1 + s2 < 48) and (step == 3)) or
        ((s1 + s2 >= 48) and (step != 3))):
            return False
        
        if step%2 == 1:
            if (s1 > s2): return f20(s1 + n, s2, step + 1) or f20(s1, s2 * 3, step + 1)
            if (s2 > s1): return f20(s1, s2 + n, step + 1) or f20(s1 * 3, s2, step + 1)

        if (s1 > s2): return f20(s1 + n, s2, step + 1) or f20(s1, s2 * 3, step + 1)
        if (s2 > s1): return f20(s1, s2 + n, step + 1) or f20(s1 * 3, s2, step + 1)
        

    for s2 in range (1, 47):
        if f20(13, s2):
            print(s2)
            break