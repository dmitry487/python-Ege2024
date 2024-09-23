otvet = []
for n in range (1, 30, 2):
    for m in range (0, 30, 2):
        num = 2 ** m * 3 ** n

        if num in range (200_000_000, 400_000_000):
            otvet.append(num)
    
print(sorted(otvet))