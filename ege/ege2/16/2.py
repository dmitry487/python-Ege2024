def f(n):
    if n == 0: return 0
    if n > 2 and n%2 == 0: return f(n/2)
    if n%2 != 0: return 1 + f(n - 1)


kolichestvo = 0
for n in range (1, 1001):
    if f(n) == 3:
        kolichestvo += 1

    

print(kolichestvo)