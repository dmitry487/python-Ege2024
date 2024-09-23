def f19(s1, s2, step = 1): #1p 2v 3p 4v 5p
    if (s1 + s2 >= 41) and (step == 3):
        return True
    elif ((s1 + s2 < 41 and step == 3) or
    (s1 + s1 >= 41 and step != 3)):
        return False
    