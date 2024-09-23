def f19(s1, s2, step = 1):#1p 2v 3p 4v 5p
    if s1 + s2 >= 40 and step == 2:
        return True
    if ((s1 + s2 >= 40 and step != 2) or
         (s1 + s2 < 40 and step == 2)):
        return False
    
    if s1 <= s2:
        for i in range (1, s1 + 1):
            return(
                (s1 + i, s2, step + 1)
            )
        
    if s2 <= s1:
        for i in range (1, s2 + 1):
            return (
                (s1, s2 + i, step + 1)
            )
min_sum = 200000
for s1 in range (1, 100):
    for s2 in range (1, 100):
        if f19(s1, s2):
            min_sum = min(min_sum, s1 + s2)
            

print(min_sum)