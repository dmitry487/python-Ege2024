def f19(s1, s2, step = 1):
    if s1 + s2 >= 231 and step == 3:
        return True
    if s1 + s2 >= 231 and step != 3 or s1 + s2 < 231 and step == 3:
        return False