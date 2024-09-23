s1 = []
s2 = []
s3 = []
s4 = []
for i in range (1, 351):
    for a in range (1, 5):
        s1.append(a)
        s2.append([a ** 2])
        s3.append([a ** 3])
        s4.append([a ** 4])

        if s1 == 513 and s2 == 1097 and s3 == 3243:
            print(s4)
    