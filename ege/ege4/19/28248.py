def f19(s1, step = 1):
    if s1 >= 31 and step == 3:
        return True
    if ((s1 >= 31 and step != 3) or
         (s1 < 31 and step == 3)):
        return False
    
    